import sys
import os
from naivebayes import naiveBayes

classifier = naiveBayes()
files = os.listdir('realDonaldTrump')
for file in files:
    f = open('realDonaldTrump/' + file, 'r')
    print ""
    print f.read()
    print classifier.run('GOP/', 'TheDemocrats/', 'realDonaldTrump/'+file)
