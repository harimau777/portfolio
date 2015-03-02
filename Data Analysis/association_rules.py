#! /usr/bin/python

#This program generates every possible association rule that can be derived from a set of transaction.

import sys
from itertools import combinations
from itertools import permutations

#Parse command line arguments:
if len(sys.argv) < 2:
	print "Error: Please include an input filename."

#Generate all unique itemsets:
f_in = open(sys.argv[1], "r")				#Open the input file for reading.
itemset = set()						#Holds unique itemsets from the transactions.
for transaction in f_in:				#Loop through each itemset in the input file.
	transaction = transaction.strip("\n")
	for length in range(2, len(transaction) + 1):		#Search for itemsets of length 2 through the length of the transaction.
		for items in combinations(transaction, length):	#Loop through each permutation of itemsets of a given length in the transaction.
			itemset.add(''.join(items))		#Store the itemset.
f_in.close()	#Close the input file.

#Generate all unique rules:
ruleset = set()						#Holds unique rules generated from the itemsets.
for items in itemset:	#Loop through each itemset.
	for length in range(2, len(items) + 1):
		for p in permutations(items, length):	#Generate each permutation of the current itemset.
			p_str = ''.join(p)
			for i in range(1, length):
				ruleset.add(p_str[:i] + "-->" + p_str[i:])
for i in sorted(ruleset):
	print i

