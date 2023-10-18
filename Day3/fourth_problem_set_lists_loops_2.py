#! /usr/bin/env python3

# Answers to the second part of Python 4 Problem Sets Loops and lists
# Write a script that uses a while loop to print out the numbers 1 to 100
#count = 1
#while count < 101:
#	print(count)
#	count+=1
#print("Done")

# While loop to calculate the factorial of 1000
factorial = 1000
result = factorial * (factorial-1)
#print(result)
while factorial > 2:
	result = result *(factorial-2)
	factorial-=1
	#print(result)
print(result)
