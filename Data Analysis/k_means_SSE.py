#! /usr/bin/python

#This program calculated the sum of squares errors for clusters generated using k-means clustering.
#It was designed to parse output files from the Orange application.

import sys

#Read the data from the files:
data_list = []
data_file = open(sys.argv[1], "r")
next(data_file)
next(data_file)
next(data_file)
for i in data_file:
	data = i.strip().split('\t')
	data_list.append([int(data[0]), int(data[1]), data[2]])
data_file.close()

cent_list = []
cent_file = open(sys.argv[2], "r")
next(cent_file)
next(cent_file)
next(cent_file)
for i in cent_file:
	center = i.strip().split('\t')
	cent_list.append([int(center[0]), int(center[1]), center[2]])
cent_file.close()

#Calculate the SSE
sse_dict = {}				#Holds an SSE for each class.
for centroid in cent_list:
	class_name = centroid[2]	#Set the name of the current centroid's class.
	sse_dict[class_name] = 0	#Add a new element to the dictionary of SSEs.
	for point in data_list:
		if point[2] == class_name:
			sse_dict[class_name] += (point[0] - centroid[0])**2 + (point[1] - centroid[1])**2

#Display the SSEs:
for i in sorted(sse_dict):
	print i + " : " + str(sse_dict[i])

