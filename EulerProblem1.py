#!/usr/bin/python -tt
# Lori-Anne Ashwood
# Using Python to solve Euler projects

#Euler projects
#https://projecteuler.net/

import sys
import time

#Euler Problem 1
# https://projecteuler.net/
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def sum_of_multiples(limit):
	total = 0
	for n in range (limit):
		if (n%3==0 or n%5==0):
			total+=n
	return total

def sum_of_mul_2 (limit):
	thislist = [n for n in range (limit) if n%3==0 or n%5==0]
	total = sum(thislist)
	return total

def timeitnow(fcnx):
	timestart = time.time()
	print "Sum is" , fcnx
	timeend = time.time()
	return timeend - timestart


def main():
	print "Euler Problem 1:"
	print sum_of_multiples(1000) #expect 23

	print "Take 2:"
	print sum_of_mul_2(1000) #expect 23

	print "Time it 1:"
	total1 = timeitnow (sum_of_multiples(1000))
	print total1

	print "Time it 2:"
	total2 = timeitnow (sum_of_mul_2(1000))

	print total2

	if total1<total2:
		print "range is faster"
	elif total2<total1:
		print "list is faster"
	else:
		print "they are equal!"






if __name__ == '__main__':
	main()
