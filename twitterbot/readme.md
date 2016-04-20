# Politibot

A twitter bot focusing on parsing twitter data which is then classified for sentiment.

# To run:

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
