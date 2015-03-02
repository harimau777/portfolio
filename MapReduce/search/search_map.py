#!/usr/bin/env python

import sys
import string
from string import translate
import hashlib

hash_len = 1000000
bloom = ["0"] * hash_len

for line in sys.stdin:	#Get the data from stdin
	words = line.strip().lower().translate(None, string.punctuation).split()	#Get the words in the line.

	for word in words:	#Loop through the words
		#Perform the hashes:
		md5 = int(hashlib.md5(word).hexdigest(), 16) % hash_len
		sha1 = int(hashlib.sha1(word).hexdigest(), 16) % hash_len
		sha254 = int(hashlib.sha224(word).hexdigest(), 16) % hash_len

		#Form the bloom filter:
		bloom[md5] = "1"
		bloom[sha1] = "1"
		bloom[sha254] = "1"

#Output the bloom filter:
print '%s\t%s' % ("bloom", ("".join(bloom) ))

