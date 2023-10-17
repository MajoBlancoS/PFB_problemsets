#! /usr/bin/env/ python3
import sys

#This is the answer to Part 2: Use text editor

#Question 1
#Using a text editor write a script that asigns a value to a variable
variable_to_test = sys.argv[1]
variable_to_test = int(variable_to_test)  

#Question 9.Print a statement that reminfs the user what number is being tested
print(f"The number you are testing is: {variable_to_test}")

#Question 2
# Has a if/else statement in which it prints out a confirmation of true "Aye captain"
if variable_to_test > 0 :
#Question 5. Add more nested tests to your script
  if variable_to_test < 50:
    #Question 6. if it is smaller than 50, test if the numbner is even
    if variable_to_test % 2 == 0 :
      print("It is an even number that is smaller than 50")
    else :
      print("the variable is positive AND smaller than 50 BUT is NOT even")
  #Question 7. If it is larger than 50, test if the number is divisible by 3.
  #Question 8. test if the number equals 50
  elif variable_to_test == 50:
    print("variable is equal to 50")
  elif variable_to_test % 3 == 0:
    print("it is larger than 50 and divisible by 3")
  else:
    print("it is larger than 50 but not divisible by 3") 
# Question 4 add elif to test if the number is equal to 0.
elif variable_to_test == 0:
  print("The variable is equal to zero")
else :
  print("The variable to test is a negative number")

