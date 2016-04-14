# classifyTweets.py #
# Alex Quinlan (quinlal) #

import sys, os, json, time, ast, requests
from naivebayes import naiveBayes
from textblob import TextBlob

tweets = open(sys.argv[1], 'r')

bayes = naiveBayes()

democrat = os.listdir('democrat/')
republican = os.listdir('republican/')

# train on scraped deomcrat and republican tweets #
training = bayes.trainNaiveBayes('democrat', democrat, 'republican', republican)

for tweet in tweets:
	t = json.loads(tweet)
	allTweets = ast.literal_eval(t)

# democrat = 1.0 #
# republican = -1.0 #

for x in allTweets:
	#string = "tweets from " + x + ": "
	state = x
	for y in allTweets[x]:
		tweet = allTweets[x][y]
		sentiment = TextBlob(tweet)
		polarity = sentiment.sentiment.polarity
		classification = bayes.testNaiveBayes(tweet, training)
		result = 0.0
		if polarity > 0.0 and classification == 'republican':
			result = -1.0
		elif polarity > 0.0 and classification == 'democrat':
			result = 1.0
		elif polarity < 0.0 and classification == 'republican':
			result = 1.0
		elif polarity < 0.0 and classification == 'democrat':
			result = -1.0

		z = {'state': state, 'pol': result, 'text': tweet}
		r = requests.post('http://104.236.24.198:8888/api/tweet', z)
		#time.sleep(3)

		#print "RESULT: " + bayes.testNaiveBayes(tweet, training) + "\n\n", "text: " + tweet + '\n\n'
