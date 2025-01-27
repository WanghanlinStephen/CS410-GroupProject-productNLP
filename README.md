# 410 Group Project: Commodity Trading Ranker System


Team Informations: <br/> 
Hanlin Wang - hanlinw4@illinois.edu <br/> 
Ruide Zhu - ruidezhu2000@gmail.com <br/> 
Haotian Wang - hw55@illinois.edu <br/> 
Huiyang Chi - huiyang_chi@outlook.com <br/> 
Mengchen Chou - mcqiu3@gmail.com <br/> 

Presentation video link: https://drive.google.com/file/d/1Q2_vmAq7uOQvTv8464Vb4CAq7GeZi5Zz/view?usp=sharing

## Background and Introduction
          
With the development of the internet, e-commercial system has become more and more common in people’s lives. And NLP has been widely used for this kind of system, especially for classifying products and searching products. search system is a system that when you type in the keyword, the system will return the related data, and the classify system is a system that when you type in a keyword, the system will return the product’s category. The products are gathered through the internet, and the document will describe how data is collected, how the backend and frontend is developed. To be specific, when searching, we can search a kind of CPU whose label is AMD Ryzen 5 1600 BOx, and the related information like category and title will be returned. when we are classifying, it will be classified as CPUs. Another important difference is that for search, there might be multiple results but there can only be one label for classifying.


## Application installation

We will use Python as development language and its flask as web-development framework. To be specific, almost all the important information is stored in app.py file like the file can tell you how to create index, how to classify the goods and how to search the goods. In detail, we use Metapy as the library to implement those function.
 
 
 

### Python
Here we use anaconda for python installation:
1.	`conda create -n <Environment Name> python=3.7`

2.	`activate < Environment Name>`

This is Command for python library installation:
3.	`Pip install <library name>`

libraries should be installed: Flask, metapy, pymongo, urllib, io, re

## How to run the App
1.	`conda activate python=3.7`

2.	`cd <to the folder where app.py is>`

3.	`python ./app.py`
Then go to the program’s corresponding URL(http://127.0.0.1:5000) to visit the website.

## Application usage

The user can click the switch botton in the search bar to decide whether he want to classify or search. 

When you are in the classify mode, You can type in M1 core CPU, then the output would be that it will be classified as CPU. 


When you are in the search mode, after inputting M1 core CPU, you will have 3 results from database, with it's category and title
<img width="616" alt="image" src="https://user-images.githubusercontent.com/54618402/206506926-e4049007-2269-44c2-8b67-9dd939e47cfe.png">

## Data Description

We collect the data from multiple datasets available in Kaggle, and all of the data we collected originates from real online electronic stores and product comparison platforms. We then conducted data cleaning and aggregatation using Pandas and Numpy to maximize classfication accuracy and efficiency so they are usable and meaningful to our project.

Specifically, `classifier.dat` contains the detailed descriptions of the products along with the categories that they belong to.  `classifier.dat.label` contains only the categories in order to generate the labels that can be used by MetaPy. Similiarly, `search.dat` contains product names, and `search.dat.label` contains the according categories that those products belong to.
