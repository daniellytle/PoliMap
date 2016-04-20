# train.py #
# Alex Quinlan (quinlal) #

import tweepy, sys, os

consumer_key = "aWVOGpooY0fUdsM6kWmRPlzLn"
consumer_secret = "aoqWgsg4DNLfZhXb6DbOe1kXDyHbsSmkDQiy6idZnZnhmVwtJT"

access_token = "1718069682-gv4wz2OZYr68lfvF4TzKwsc9atMNy5WYZemKshy"
access_token_secret = "fxE3ZOIHjWCmCHegy9AaVM89f4YULZe8oniSZWjj8qfh7"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def scrape(userId, limit, party, startNum):
	public_tweets = api.user_timeline(screen_name=userId, count=limit)
	#os.makedirs(userId)
	for index, tweet in enumerate(public_tweets):
	    f = open(party + '/' + str(int(index) + int(startNum)), 'w+')
	    f.write(tweet.text.encode('utf-8')) 

def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)

ensure_dir('republican/')
ensure_dir('democrat/')

republican = ['gop', 'housegop', 'senategop']
democrat = ['thedemocrats', 'housedemocrats', 'senatedems']

startNum = 0
for x in republican:
	scrape(x, 1000, 'republican', startNum)
	startNum += 1000
startNum = 0
for x in democrat:
	scrape(x, 1000, 'democrat', startNum)
	startNum += 1000