#!/usr/bin/env python

import sys
from math import sqrt

def checkPrime(number):
        number = abs(number)

        if (number % 2 == 0) and (number != 2):         #If the number is even and greater than 2 then it is not prime.
                return False
        for i in xrange(3, int(sqrt(number)) + 2, 2):   #If the number is evenly divisible by an odd number less than sqrt(number) then it is not prime.
                if number % i == 0:
                        return False
        return True

mySum = 0
myCount = 0

for line in sys.stdin: #Get the data from stdin
	mySum += int(line.strip())
	myCount += 1
	if checkPrime(int(line.strip())):
		print '%s\t%s' % ('primes', line.strip())

print '%s\t%s' % ('sum', mySum)
print '%s\t%s' % ('count', myCount)

