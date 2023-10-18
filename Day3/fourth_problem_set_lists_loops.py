#! /usr/bin/env python3

# Answers to Python 4 Problem Set -- lists and loops
# Save the string sapiens, erectus, neanderthalensis as a variable named taxa
taxa = "sapiens, erectus, neandertahalensis"

# Print taxa
print(taxa)

# Print taxa[1]. What do you get?
print(taxa[1]) #a

# Print type(taxa). What is its type?
print(type(taxa))
# <class 'str'>

# Split taxa into individual words and print the result of the split
print(taxa.split(','))

# Store the result of the split in a new variable named species
species = taxa.split(',')

# Print species
print(species)

# Print the species[1]. What do you get?
print(species[1]) #erectus

# Print type(species). What is its type?
print(type(species)) # <class 'list'>

# Sort the list alphabetically and print
sorted_species = sorted(species, key = None, reverse= False)
print(sorted_species)

# Sort the list by length of each string and print
# Checkout documentation of the key argument
	#len list is sorted based on the length of the element, from the lowest count to the highest
sorted_species_length = sorted(species, key = len, reverse = False)
print(sorted_species_length)
