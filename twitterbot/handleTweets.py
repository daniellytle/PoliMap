# handleTweets.py #
# Alex Quinlan (quinlal) #

import sys, json, os, requests, time
from naivebayes import naiveBayes
from textblob import TextBlob

if len(sys.argv) != 3:
	print 'wrong number of arguments. proper usage: python handleTweets.py <file-containing-tweets> <app-server>\nExample: python handleTweets.py tweets.json http://localhost:8888'
	sys.exit(0)

tweetFile = sys.argv[1]
server = sys.argv[2]

tweets = open(tweetFile, 'r')

bayes = naiveBayes()
democrat = os.listdir('democrat/')
republican = os.listdir('republican/')

# train on scraped deomcrat and republican tweets #
training = bayes.trainNaiveBayes('democrat', democrat, 'republican', republican)

states = {
		'AK': 1,'AL': 2,'AR': 3,'AZ': 4,'CA': 5,'CO': 6,'CT': 7,'DE': 8,'FL': 9,'GA': 10,'HI': 11,'IA': 12,'ID': 13,'IL': 14,'IN': 15,
        'KS': 16,'KY': 17,'LA': 18,'MA': 19,'MD': 20,'ME': 21,'MI': 22,'MN': 23,'MO': 24,
        'MS': 25,
        'MT': 26,
        'NC': 27,
        'ND': 28,
        'NE': 29,
        'NH': 30,
        'NJ': 31,
        'NM': 32,
        'NV': 33,
        'NY': 34,
        'OH': 35,
        'OK': 36,
        'OR': 37,
        'PA': 38,
        'RI': 39,
        'SC': 40,
        'SD': 41,
        'TN': 42,
        'TX': 43,
        'UT': 44,
        'VA': 45,
        'VT': 46,
        'WA': 47,
        'WI': 48,
        'WV': 49,
        'WY': 50
}
statesToAbbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}
idToAbbrev = {
47: "WA",
48: "WI",
49: "WV",
9: "FL",
50: "WY",
30: "NH",
31: "NJ",
32: "NM",
27: "NC",
28: "ND",
29: "NE",
34: "NY",
39: "RI",
33: "NV",
6: "CO",
5: "CA",
10: "GA",
7: "CT",
36: "OK",
35: "OH",
16: "KS",
40: "SC",
17: "KY",
37: "OR",
41: "SD",
8: "DE",
11: "HI",
43: "TX",
18: "LA",
42: "TN",
38: "PA",
45: "VA",
1: "AK",
2: "AL",
3: "AR",
46: "VT",
14: "IL",
15: "IN",
12: "IA",
4: "AZ",
13: "ID",
21: "ME",
20: "MD",
19: "MA",
44: "UT",
24: "MO",
23: "MN",
22: "MI",
26: "MT",
25: "MS",
}

stateIds = {
1: {},
2: {},
3: {},
4: {},
5: {},
6: {},
7: {},
8: {},
9: {},
10: {},
11: {},
12: {},
13: {},
14: {},
15: {},
16: {},
17: {},
18: {},
19: {},
20: {},
21: {},
22: {},
23: {},
24: {},
25: {},
26: {},
27: {},
28: {},
29: {},
30: {},
31: {},
32: {},
33: {},
34: {},
35: {},
36: {},
37: {},
38: {},
39: {},
40: {},
41: {},
42: {},
43: {},
44: {},
45: {},
46: {},
47: {},
48: {},
49: {},
50: {}
}

for tweet in tweets:

    tweet = tweet.strip()

    if tweet is not '':
        t = json.loads(tweet)
        place = ''
        text = ''
        id = -1

        if t.get('id'):
            id = t['id']

        if t.get('text'):
            text = t['text'].encode('ascii', 'ignore')

        if t.get('place'):
            if t['place']['country_code'].encode('ascii', 'ignore') == 'US':
                place = t['place']['full_name'].encode('ascii', 'ignore')
                space = place.rfind(' ') + 1
                locCode = place[space:]
                if len(locCode) == 3:
                    locCode = place[:space-2]
                location = locCode
                if locCode not in states:
                    if locCode not in statesToAbbrev:
                        continue
                    location = statesToAbbrev[locCode]
                if location in states:
                    locId = states[location]
                    stateIds[locId][id] = text
        else:
            continue

for x in stateIds:

    state = idToAbbrev[x]

    for y in stateIds[x]:
        print y
        tweet = stateIds[x][y]
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
        r = requests.post(server, z)