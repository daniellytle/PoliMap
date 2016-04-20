# EECS 498 Final Project

Developed by Alex Quinlan, Daniel Wilson, Alex Ottenwess, and Rishin Doshi. This application scrapes tweets, classifies them for political leaning between republican and democratic. A nodejs web server displays a visualization of the results. 

# Running the Application

### Requirements

You'll need Nodejs installed.

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

## to parse, classify, and send results to server:
python handleTweets.py input.json url-name
    
    ex: python handleTweets.py tweets.json http://localhost:8888/api/tweet

#If you would like to gather your own dataset and training data, see below

## to collect training data
python train.py

## to collect live tweets for n seconds:
python live.py n > output.json
    
    ex: python live.py 60 > tweets.json
