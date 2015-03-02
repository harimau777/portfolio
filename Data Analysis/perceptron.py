#!/usr/bin/python

#This program trains the weights in a perceptron.

weights = [0, 0, 0, 0, 0]
training_set = [[[5, 7, 3, 9, 1], 1], [[6, 9, 12, 7, 1], 1], [[2, -2, 3, 4, 1], 0], [[-3, 4, 4, 0, 1], 0], [[7, 5, 3, 5, 1], 1], [[4, 1, 0, 3, 1], 0]]
#Uncomment to use training set for part c of the question:
#training_set.append([[3, 1, 3, 2, 1], 0])
#training_set.append([[5, 8, 6, 9, 0], 1])
#weights.append(0)
#weights.append(0)

def dot_product(values, weights):
	return sum(value * weight for value, weight in zip(values, weights))

threshold = 0
cntPass = 0
myDot = 0
iterations = 0
outStr = ""

print "Data * Weights * Dot Product * Error? * Adjusted Weights"
while iterations <= 32:
	print "****************************************"
	for vector in training_set:	#Get each line of the training set.
		#Find the dot product:
		myDot = dot_product(vector[0], weights)
		outStr = str(vector[0]) + " * " + str(weights) + " * " + str(myDot) + " * "

		#Check the classification:
		#If the current data is in class 0:
		if vector[1] == 0:
			#Check if the data is classifed correctly:
			if myDot < threshold:
				cntPass += 1
				outStr += "N * " + str(weights)
			#Adjust the weight down:
			elif myDot >= threshold:
				weights = [a - b for a, b in zip(weights, vector[0])]
				cntPass = 0
				outStr += "Y * " + str(weights)
		#If the current data is in class 1:
		elif vector[1] == 1:
			#Check if the data is classified correctly:
			if myDot > threshold:
				cntPass += 1
				outStr += "N * " + str(weights)
			#Adjust the weight up:
			elif myDot <= threshold:
				weights = [a + b for a, b in zip(weights, vector[0])]
				cntPass = 0
				outStr += "Y * " + str(weights)
		#Print the current information:
		print outStr

		#Check if we are finished:
		if cntPass == len(training_set):
			break
	if cntPass == len(training_set):
		break
	iterations += 1
	if iterations > 32:
		print "No convergence"
print "****************************************"
print "Final Weights: " + str(weights)

