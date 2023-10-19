#! /usr/bin/env python3

# for to iterate element and print each element
# print hte length of the sequence separated by tab

my_sequence = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
position = 0 
for seq in my_sequence:
	#modified, print position in the list
	print(position,len(seq),seq, sep = "\t")
	position += 1
