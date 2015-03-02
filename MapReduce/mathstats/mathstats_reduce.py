#!/usr/bin/env python

import sys

mySum = 0
myCount = 0
myPrimeCount = 0
#myPrimes = []

for line in sys.stdin:  #Get the key values from stdin.
	(key, val) = line.strip().split('\t', 1)	#Split at the first tab.
	if key == 'sum':
		mySum += int(val)
	if key == 'count':
		myCount += int(val)
	if key == 'primes':
		myPrimeCount += 1
#		myPrimes.append(val)

print "Sum: " + str(mySum)
print "Count: " + str(myCount)
print "Prime Count: " + str(myPrimeCount)
#print "Primes: " + str(myPrimes)

