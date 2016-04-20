# EECS 498 Final Project

Developed by Alex Quinlan, Daniel Wilson, Alex Ottenwess, and Rishin Doshi. This application scrapes tweets, classifies them for political leaning between republican and democratic. A nodejs web server displays a visualization of the results. 

![Political Tweet Visualization](https://raw.githubusercontent.com/daniellytle/final_proj/master/Screen%20Shot%202016-04-19%20at%2010.18.28%20PM.png)

# Running the Application

### Requirements

You'll need Nodejs installed.

### Overview

The Application is a built from a web server which listens for tweet requests from a python script. In order to view the demo we presented in class:

* Start the server
* Run the scripts

# Starting the Server

First get all necessary packages

```
$ npm install
```

Then start the server.

```
$ node server.js
```

The live map should now be running at `localhost:8888`

# Running the Python Scripts

We have provided training data and the dataset (found in tweets.json)

### To parse, classify, and send results to server:

python handleTweets.py input.json url-name
    
    ex: python handleTweets.py tweets.json http://localhost:8888/api/tweet

After running this command you can watch the map live update at `localhost:8888`.

## If you would like to gather your own dataset and training data, see below

## Collecting training data

In order to collect the republican and democratic training data, run the following:

```
$ python train.py
```

## Collecting live tweets for n seconds:

To run a live Twitter stream for tweets, run the following:

```
python live.py n > output.json
```    
    ex: python live.py 60 > tweets.json
