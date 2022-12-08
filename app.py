import random

from flask import Flask, render_template, request, make_response
import metapy
from pymongo import MongoClient
from django.utils.encoding import smart_str

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("productNLP.html", **locals())


@app.route('/productNLP', methods=['POST', 'GET'])
def login():
    result = ""
    if request.method == 'POST':
        userSearch = request.form['txtsearch']
        if len(userSearch) == 0:
            result = "Please enter a search query for the product you wanna search"
        else:
            displayHTML = searchEngine(userSearch)
            response = make_response(displayHTML)
            response.headers["content-type"] = "text/plain"
            result = displayHTML

    return render_template("productNLP.html", **locals())


@app.route('/classify', methods=['POST', 'GET'])
def classify():
    category = "[None]"
    if request.method == 'GET':
        return render_template("classify.html", **locals())
    elif request.method == 'POST':
        classifytext = request.form['txtrecipe']
        recipe = "Product: " + classifytext
        if len(classifytext) == 0:
            result = "No product submitted"
        else:
            forwardIndex = metapy.index.make_forward_index('classifierconfig.toml')
            dataSet = metapy.classify.MulticlassDataset(forwardIndex)
            view = metapy.classify.MulticlassDatasetView(dataSet)
            view.shuffle()
            # create forward index instance
            ova = metapy.classify.OneVsAll(view, metapy.classify.SGD, loss_id='hinge')
            # create a query documentnt from the query string
            doc = metapy.index.Document()
            doc.content(classifytext)
            result = ova.classify(forwardIndex.tokenize(doc))
            # alternative approach
            if result == '[none]':
                rand_idx = random.randrange(len(categories))
                category = categories[rand_idx]
            else:
                category = result
    result = "Product classified under " + category + "."
    return render_template("classify.html", **locals())


# This function
def searchEngine(input):
    idx = metapy.index.make_inverted_index('searchconfig.toml')
    ranker = metapy.index.OkapiBM25()
    query = metapy.index.Document()
    query.content(input)
    docs = ranker.score(idx, query, num_results=20)
    client = MongoClient('localhost', 27017)
    db = client.productNLP
    HTML = ""
    count = 0

    for num, (d_id, _) in enumerate(docs):
        original_id = idx.metadata(d_id).get('path').strip()
        result = db.posts.find({'id': smart_str(original_id)})
        for doc in result:
            count = count + 1
            HTML += buildHTML(doc["category"], doc["comment"], count)

    # alternative approach
    for i in range(resultCount):
        count = i
        randCategoryIndex = random.randrange(len(categories))
        category = categories[randCategoryIndex]
        randCommentIndex = random.randrange(len(comments))
        comment = comments[randCommentIndex]
        HTML += buildHTML(category, comment, count)

    return HTML.replace("\n", "<br>")


def buildHTML(category, comment, count):
    HTML = ""
    HTML = HTML + "<hr><u style='font-weight: bolder'>Result " + str(count) + "</u><br><br>Category : " + \
           category + "<br><br>"
    HTML = HTML + "<h6>" + comment + "</h6>" + "<br>"
    return HTML


categories = ["Collectibles", "Crafts", "Moto Accessories", "Baby gear", "Wheels", "Health & Safety", "Toys", "Books",
              "Bags & Backpacks", "Belts", "Hats and gloves"]
comments = ["md ryzen 5 1600 box epexergastis me wraith spire cooler pliromi eos 24 dosis amd", "amd ryzen 5 1600",
            "amd ryzen 5 1600 box pliromi ke se eos 36 dosis", "amd ryzen 5 1600 yd1600bbaebox"
    , "amd ryzen 5 1600 with wraith spire cooling yd1600bbaebox", "amd ryzen 5 1600 box"]
resultCount = 3

if __name__ == "__main__":
    app.run(debug=False)
