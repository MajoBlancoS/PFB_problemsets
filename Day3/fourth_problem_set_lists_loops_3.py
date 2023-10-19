#! /usr/bin/env python3

# Answers to the fourth problem set of python, script 3
my_list = [101,2,15,22,95,33,2,27,72,15,52]
# Sort the elements of the above list
sor_my_list = sorted(my_list, key = None, reverse = False)

# Defining variables to use later
sum_even = 0
sum_not_even = 0

# iterate through each element of list with for loop
for element in sor_my_list:
	#print(element)
	# Print out only the values that are even
	if element % 2 == 0:
	#	print(element)
	# Calculate cumulative sum for even numbers
		sum_even = sum_even + element	
		#print(f'Sum of even numbers: {sum_even}')
	else :
		#print("Element is not even")
		#Calculate cumulative sum for not even numbers
		sum_not_even = sum_not_even + element
		#print(f'Sum of odds: {sum_not_even}')

#Print only the final sum
print(f"""Sum of even numbers: {sum_even}
Sum of odds: {sum_not_even}""")
