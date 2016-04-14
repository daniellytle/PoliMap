# Twitter Scraper for political tweets
import tweepy
import sys
import os

userId = sys.argv[1]
party = sys.argv[2]
limit = sys.argv[3]
startNum = sys.argv[4]

consumer_key = "aWVOGpooY0fUdsM6kWmRPlzLn"
consumer_secret = "aoqWgsg4DNLfZhXb6DbOe1kXDyHbsSmkDQiy6idZnZnhmVwtJT"

access_token = "1718069682-gv4wz2OZYr68lfvF4TzKwsc9atMNy5WYZemKshy"
access_token_secret = "fxE3ZOIHjWCmCHegy9AaVM89f4YULZe8oniSZWjj8qfh7"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.user_timeline(screen_name=userId, count=limit)
#os.makedirs(userId)
for index, tweet in enumerate(public_tweets):
    f = open(party + '/' + str(int(index) + int(startNum)), 'w+')
    f.write(tweet.text.encode('utf-8')) 
