# live.py #
# get a live stream of tweets with political tweets #
# Alex Quinlan (quinlal) #

# edit the list 'keywords' to edit the search query #

import sys, json, time
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

if len(sys.argv) != 2:
    print 'wrong number of arguments. proper usage: python live.py <time-to-run-in-secs> > tweets.json'
    sys.exit(0)

timeToRun = sys.argv[1]

consumer_key = "aWVOGpooY0fUdsM6kWmRPlzLn"
consumer_secret = "aoqWgsg4DNLfZhXb6DbOe1kXDyHbsSmkDQiy6idZnZnhmVwtJT"

access_token = "1718069682-gv4wz2OZYr68lfvF4TzKwsc9atMNy5WYZemKshy"
access_token_secret = "fxE3ZOIHjWCmCHegy9AaVM89f4YULZe8oniSZWjj8qfh7"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):

        # this writes to a json file but no newlines or anything so trying the txt thing again #
        
        #with open('tweets.json', 'w') as f:
        #   json.dump(data+'\n',f,indent=1)
        
        # try print json to a file again #
        print (data)
        return True

    def on_error(self, status):
        print(status)

#state_locations = {'California': [-124.415165,32.5342643,-114.1313926,42.0095169], 'Nevada': [-120.0064729,35.001857,-114.0396479,42.002207]}

keywords = ['donald trump', 'trump', 'trump2016', 'makeamericagreatagain', 'john kasich', 'kasich', 'kasich2016', 'cruz', 'ted cruz', 'cruz2016', 
    'bernie sanders', 'sanders', 'sanders2016', 'feelthebern', 'clinton', 'hillary clinton', 'clinton2016', 'imwithher', 'republican'
    'democrat', 'gop', 'dnc']

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    tweets = stream.filter(track=keywords, languages=['en'], async=True)
    time.sleep(int(timeToRun))
    stream.disconnect()
    #tweets.filter(locations=[-124.77,24.52,-66.95,49.38])

'''

So the above part sets up the stream and reads in tweets, filtered by language, keywords, and then by location (within the US).
The stuff below was my attempt to get it to return a limited number tweets. 
or like one tweet every few seconds but I couldn't figure it out. I think it has something to do with setting async=True in filter()
but like idk how exactly. If you can figure it out that would be dank

'''

'''
        #tweet = json.loads(data)
        #text = ''
        #if tweet.get('text'):
        #    text = tweet['text'].encode('ascii', 'ignore') + 
        #if tweet.get('place'):
        #    print "LOCATION: ", tweet['place'], 
        #location = tweet['location'].encode('ascii', 'ignore') + 
        #print text#, location, 
        # allTweets.append(tweet)
'''


'''
	while True:
		if stream.running is True:
			stream.disconnect()
			print allTweets.pop()
		else:
			print 'Streaming'
			stream.filter(languages=['en'], track=['trump', 'makeamericagreatagain', 'cruz', 'trump2016', 'kasich'], async=True)
			print 'here?'
			#tweets.filter(locations=[-124.77,24.52,-66.95,49.38], async=True)
		time.sleep(2)
'''
