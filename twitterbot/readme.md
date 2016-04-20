# Politibot

A twitter bot focusing on parsing twitter data which is then classified for sentiment.

# To run:

## to collect training data
python train.py

## to collect live tweets for n seconds:
python live.py n > output.json
	
	ex: python live.py 60 > tweets.json

## to parse, classify, and send results to server:
python handleTweets.py input.json <server-name>
	
	ex: python handleTweets.py tweets.json http://localhost:8888/api/tweet
	ex: python handleTweets.py tweets.json http://104.236.24.198:8888/api/tweet
