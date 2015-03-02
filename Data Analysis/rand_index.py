#! /usr/bin/python

#This program calculated the Rand Index of two clusterings.
#It is designed to parse output files from the Orange application.

#Note: This program only works if the files containing both clusterings contain the points in the same order.

import sys
from itertools import combinations

e_distance = 2		#The distance used to define a points e neighborhood.
min_pnts = 3		#The minimum number of neighborhood points required to be considered a core point.

core_list = []		#Holds core points and the points in their neighborhood.
border_list = []	#Holds border points and the points in their neighborhood.
outlier_list = []	#Holds points that are neither core points or border points.
temp_list = []		#Holds points temporarily until we can determine if they are border or outlier
			#	points.

def read_data(filename):
	data = {}
	f = open(filename, "r")
	next(f)
	next(f)
	next(f)
	for i in f:
		line = i.strip().split('\t')
		key = "(" + line[0] + "," + line[1] + ")"
		data[key] = line[2]			#Create a dictionary using the tupple formed by the x and y coordinates as the key
							#	and the class as the value.
	return data

def get_pairs(data):
	pairs = list(combinations(data, 2))
	parsed_pairs = {}
	for i in pairs:
		key = (i[0], i[1])
		cluster1 = data[i[0]]
		cluster2 = data[i[1]]
		if cluster1 == cluster2:
			parsed_pairs[key] = "same"
		else:
			parsed_pairs[key] = "different"
	return parsed_pairs

#Read the clustering from the files:
data_a = read_data(sys.argv[1])
data_b = read_data(sys.argv[2])

#Get all pairs for both clusterings:
pairs_a = get_pairs(data_a)
pairs_b = get_pairs(data_b)

#Find a, b, c, and d:
a = 0	#Count of pairs whose points are in the same class in both clustering a and clustering b.
b = 0	#Count of pairs whose points are in different classes in both clustering a and clustering b.
c = 0	#Count of pairs whose points are in the same class in clustering a and different classes in clustering b.
d = 0	#Count of pairs whose points are in different classes in clustering a and the same class in clustering b.
for i in pairs_a:
	data1 = pairs_a[i]
	data2 = ""
	if i in pairs_b:
		data2 = pairs_b[i]
	elif (i[1], i[0]) in pairs_b:		#Check if the order of the combination might be different.
		data2 = pairs_b[(i[1], i[0])]
	else:
		print "Error " + str(i)
		continue

	if (data1 == "same") and (data2 == "same"):
		a += 1
	elif (data1 == "different") and (data2 == "different"):
		b += 1
	elif (data1 == "same") and (data2 == "different"):
		c += 1
	elif (data1 == "different") and (data2 == "same"):
		d += 1
	else:
		print "Error"
		sys.exit()

#Calculate the Rand Index:
rand_index = float((a + b)) / float((a + b + c + d))
print "a = " + str(a) + ", b = " + str(b) + ", c = " + str(c) + ", d = " + str(d) + ", Rand Index = " + str(rand_index)

