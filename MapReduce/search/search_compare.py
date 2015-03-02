#!/usr/bin/env python

import sys
import hashlib

hash_len = 1000000

#Get text bloom filter:
text_file = open('part-00000', 'r')
text_filter = text_file.read()
text_file.close()

while (True):
	#Get user input
	message = raw_input("Enter word to search for: ").lower()
	if message == "exit":
		break

	#Perform the hashes:
	md5 = int(hashlib.md5(message).hexdigest(), 16) % hash_len
	sha1 = int(hashlib.sha1(message).hexdigest(), 16) % hash_len
	sha224 = int(hashlib.sha224(message).hexdigest(), 16) % hash_len

	if text_filter[md5] == "0" or text_filter[sha1] == "0" or text_filter[sha224] == "0":
		print "Not found"
		print md5
		print sha1
		print sha224
	else:
		print "Found"

