#! /usr/bin/env python3
import sys

# construct a dictionary of your favorite things
my_favorite_things = { 'Song' : 'Will You Be There','Artist' : 'Michael Jackson', 'Color' : 'Tale'}

# print your favorite song
key_song = 'Song'
#print(my_favorite_things[key_song])

# Add fav organism to dictionary. new key = fav_thing
# input user to pick
x = input('Enter a category of things you like, namely book, song,etc... :')
print(f'Enter your favorite {x} : ')
y = input()
print(f'Is your favorite {x} {y} ? (y/n)')
confirmation = input()

if confirmation == "y":
	fav_thing = x
	my_favorite_things[fav_thing] = y
	#print(my_favorite_things[fav_thing])

	# Use for to print each key and value
	for key in my_favorite_things:
		print(key, my_favorite_things[key], sep = "\t")
else :
	print(f"I didn'd add your favorite {x}")
