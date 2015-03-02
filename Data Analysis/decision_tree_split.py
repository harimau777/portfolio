#!/usr/bin/python

#This program calculates the optimal place to split a group of points when creating a decision tree.
#The optimal split location is considered the location which produces the greatest information gain when
#the data is split.

import math

#Get the data
f = open("./seedsCol1.csv", "r")
myList = []
for l in f:
	myElement = l.strip().split(",")
	myList.append([float(myElement[0]), int(myElement[1])])

def split(splitPnt, data, bndHigh, bndLow):
	cntTotal = [0, 0, 0]
	cntHigh = [0, 0, 0]
	cntLow = [0, 0, 0]
	entTotal = 0.0	#The entropy of the unsplit data.
	entHigh = 0.0	#The entropy of the high side of the split.
	entLow = 0.0	#The entropy of the low side of the split.

	#Split the data:
	for i in data:
		#Count the total number of points:
		cntTotal[(i[1] - 1)] += 1
		#Assign point to high side of split:
		if(i[0] > splitPnt):
			cntHigh[(i[1] - 1)] += 1
		#Assign point to low side of split:
		elif(i[0] <= splitPnt):
			cntLow[(i[1] - 1)] += 1
	#Calculate entropy:
	entTotal = entropy(cntTotal)
	entHigh = entropy(cntHigh)
	entLow = entropy(cntLow)

	#Calculate information gain:
	infoGainHigh = entTotal - entHigh
	infoGainLow = entTotal - entLow

	return [infoGainHigh, infoGainLow, splitPnt]

def entropy(cnt):
	ent = 0.0
	mySum = sum(cnt)
	#Calculate the entropy:
	for i in cnt:
		if(i != 0):
			ent += (float(i) / mySum) * math.log((float(i) / mySum), 2)
	ent *= -1
	return ent

ansList = []
for i in myList:
	ansList.append(split(i[0], myList, 21.18, 10.59))

print "Information Gain High * Information Gain Low * Split Point"
maxList = []
pntList = []
for i in ansList:
	print i
	if not maxList:
		maxList.append(i[0])
		maxList.append(i[1])
		pntList.append(i[2])
		pntList.append(i[2])
	if(i[0] > maxList[0]):
		maxList[0] = i[0]
		pntList[0] = i[2]
	if(i[1] > maxList[1]):
		maxList[1] = i[1]
		pntList[1] = i[2]

print "********************"
print "Maximum values (High, Low): " + str(maxList) + " Maximum Points (High, Low): " + str(pntList)
