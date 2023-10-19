#! /usr/bin/env python3

#list of tuples

my_sequence = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
position = 0
my_list_of_tuples = [ ]

for seq in my_sequence:
	print(len(seq),seq, sep = "\t")
	my_tupple = (len(seq),seq)
	my_list_of_tuples.append(my_tupple)
	position += 1
print(my_list_of_tuples)
