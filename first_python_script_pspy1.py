#! /usr/bin/env python3
import sys #imports to use sys.argv to retrieve name, color activity and animal from command line

#problem set answers
#printing multiple variables into the screen
my_name = "Maria Jose Blanco Salazar"
print("My name:", my_name)
my_favorite_color = "Tale"
print("My favorite color:", my_favorite_color)
my_favorite_activity = "Dancing to latin music"
print("My favorite activity:", my_favorite_activity)
my_favorite_animal = "Dog"
print("My favorite animal:", my_favorite_animal)

#trying with f string formatting
print(f'My name: {my_name}')
print(f'My favorite color: {my_favorite_color}')
print(f'My favorite activity: {my_favorite_activity}')
print(f'My favorite animal: {my_favorite_animal}')

#trying to retrieve as arguments form command line
my_name = sys.argv[1]
my_favorite_color = sys.argv[2]
my_favorite_activity = sys.argv[3]
my_favorite_animal = sys.argv[4]
print(f'My name: {my_name}\nMy favorite color: {my_favorite_color}\nMy favorite activity: {my_favorite_activity}\nMy favorite animal: {my_favorite_animal}')
