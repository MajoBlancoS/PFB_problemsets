#! /usr/bin/env python3

# List comprehension to print every number between 1 and 100

# Creating a list qith numbers between 1 and 100
my_list = [ ]
for number in range(1,100):
	my_list.append(number)
#print(my_list)

my_list2 = [ ]
#with comprehension
#[print(number) for number in range(1,100)]

[my_list2.append(number) for number in range(1,100)]
print(my_list2)
