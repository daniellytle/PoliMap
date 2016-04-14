import os
import sys

directory = sys.argv[1]

files = os.listdir(directory)

wordCount = 0
averageWords = 0.0

for f in files:
    words = open(directory + '/' + f)
    words = words.read().split()
    for w in words:
        wordCount += 1
        
averageWords = float(wordCount) / float(len(files))

print wordCount, "words"
print averageWords, "per tweet"
