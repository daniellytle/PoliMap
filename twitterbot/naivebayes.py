# Daniel Wilson
# wilsoda

import sys
import os
import re
from collections import defaultdict
from porterStemmer import *
import operator

class naiveBayes:

	Stemmer = PorterStemmer()

	# Tokenizes input
	def tokenizeText(self, s):
		s = s.lower()
		reg = re.compile("\w+[-\']\w+|[\w]+")
		tokens = reg.findall(s)
		return tokens

	# Remove stop words
	def removeStopwords(self, t):
		stopwords = ['a', 'all', 'an', 'and', 'any', 'are', 'as', 'at', 'be', 'been', 'but', 'by', 'few', 'from', 'for', 'have', 'he', 'her', 'here', 'him', 'his', 'how', 'i', 'in', 'is', 'it', 'its', 'many', 'me', 'my', 'none', 'of', 'on', 'or', 'our', 'she', 'some', 'the', 'their', 'them', 'there', 'they', 'that', 'this', 'to', 'us', 'was', 'what', 'when', 'where', 'which', 'who', 'why', 'will', 'with', 'you', 'your']
		for w in t:
			if w in stopwords:
				t.remove(w)
		return t

	# Stem words
	def stemWords(self, t):
		for w in range(0,len(t)):
			t[w] = self.Stemmer.stem(t[w], 0, len(t[w]) - 1)
		return t

	# Preprocess text
	def preprocess(self, t):
		t = self.tokenizeText(t)
		# t = removeStopwords(t)
		# t = stemWords(t)
		return t

	def bayes(self, inclass, count, vocab):
		return float(inclass + 1) / float(count + vocab)

	def trainNaiveBayes(self, aTitle, aFiles, bTitle, bFiles):
		model = {}
		model["labelA"] = aTitle
		model["labelB"] = bTitle
	 	model[aTitle] = {}
		model[bTitle] = {}
		model['total'] = {}
		model['total'][aTitle] = model['total'][bTitle] = 0
		model['priors'] = {}
		model['priors'][aTitle] = model['priors'][bTitle] = 0.0
		model['v'] = {}

		for file in aFiles:
			type = aTitle
			model['priors'][type] += 1
			f = open(aTitle + file, 'r')
			text = f.read()
			text = self.preprocess(text)
			for token in text:
				model['v'][token] = 1
				model['total'][type] += 1
				if token not in model[type]:
					model[type][token] = 0
				model[type][token] += 1

		for file in bFiles:
			type = bTitle
			model['priors'][type] += 1
			f = open(bTitle + file, 'r')
			text = f.read()
			text = self.preprocess(text)
			for token in text:
				model['v'][token] = 1
				model['total'][type] += 1
				if token not in model[type]:
					model[type][token] = 0
				model[type][token] += 1

		# Calculate Priors
		model['priors'][aTitle] /= len(aFiles)
		model['priors'][bTitle] /= len(bFiles)

		return model

	def testNaiveBayes(self, file, m):
		valA = 1.0
		valB = 1.0
		f = open(file, 'r')
		text = f.read()
		text = self.preprocess(text)
		for token in text:

			if token not in m[m["labelA"]]:
				m[m["labelA"]][token] = 0
			valA *= self.bayes(m[m["labelA"]][token], m['total'][m["labelA"]], len(m['v']))

			if token not in m[m["labelB"]]:
				m[m["labelB"]][token] = 0
			valB *= self.bayes(m[m["labelB"]][token], m['total'][m["labelB"]], len(m['v']))

		valA *= m['priors'][m["labelA"]]
		valB *= m['priors'][m["labelB"]]
		# print m['labelA'], valA, m['labelB'], valB

		answer = m["labelA"] if valA > valB else m["labelB"]
		return answer

	def run(self, aFolder, bFolder, testFile):

		# Main program
		aFiles = os.listdir(aFolder)
		bFiles = os.listdir(bFolder)

		# Train Model
		Model = self.trainNaiveBayes(aFolder, aFiles, bFolder, bFiles)
		prediction = self.testNaiveBayes(testFile, Model)

		return prediction


