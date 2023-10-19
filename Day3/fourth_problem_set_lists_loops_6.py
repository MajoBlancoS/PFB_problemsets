#! /usr/bin/env python3
import sys

# Takes start and end values from command line and prints values between them 
my_list2 = [ ]
lower_range = int(sys.argv[1])
upper_range = int(sys.argv[2])

#with comprehension
[my_list2.append(number) for number in range(lower_range,upper_range) if number % 2 != 0]
#modify to only print if the number is odd
print(my_list2)
