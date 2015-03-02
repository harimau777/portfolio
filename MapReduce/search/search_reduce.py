#!/usr/bin/env python

import sys
import hashlib

hash_len = 1000000
bloom = ["0"] * hash_len

for line in sys.stdin:	#Get the key values from stdin.
	if len(line) == 0:
		continue
	(key, val) = line.strip().split('\t', 1)	#Split at the first tab.
	#Combine the bloom filters:
	for i in xrange(0,len(val)):
		if val[i] == "1":
			bloom[i] = "1"
text_filter = "".join(bloom)
print text_filter

