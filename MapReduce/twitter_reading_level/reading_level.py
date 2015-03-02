#! /usr/bin/env python

import sys
import string
from string import translate
import pickle
import unicodedata

class reading_level:
	def __init__(self):
		f = open('syl_dict.p', 'rb')
		self.syl_dict = pickle.load(f)
		f.close()
	def get_level(self, sentence):
		#Split the sentence into words:
		#http://stackoverflow.com/questions/1207457/convert-unicode-to-a-string-in-python-containing-extra-symbols
		words = unicodedata.normalize('NFKD', sentence.strip()).encode('ascii','ignore').lower().translate(None, string.punctuation).split()
		#Count the number of syllables:
		num_syl = 0	#Number of syllables in the sentence.
		for word in words:
			num_syl += self.get_syl(word)
		#Calculate the reading level:
		if len(words) == 0:
			return 0
		else:
			return (.39 * len(words)) + (11.8 * (num_syl / len(words))) - 15.59

	def check_spelling(self, sentence):
		misspell_count = 0	#The number of misspelled words in the sentence.

		#Split the sentence into words:
		words = unicodedata.normalize('NFKD', sentence.strip()).encode('ascii','ignore').lower().translate(None, string.punctuation).split()

		#Check the spelling of each word:
		for word in words:
			if word not in self.syl_dict:
				misspell_count += 1
		return misspell_count

	def get_syl(self, word):
		try:
			return self.syl_dict[word]
		except KeyError:
			return 1


def main(argv):
	leveler = reading_level()
#	print leveler.get_level(argv[1])
	print leveler.get_syl(argv[1])

if __name__ == '__main__':
	main(sys.argv)
