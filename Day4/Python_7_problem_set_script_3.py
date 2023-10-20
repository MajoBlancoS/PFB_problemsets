#! /usr/bin/env python3
import re

# Apoi = R^ATTY where R and Y are degenerate IUPAC
# Write reg expre to find and print all ocurrences in Python_07_ApoI.fasta

# R -> A or G
# Y -> C or T

string = ''
with open("Python_07_ApoI.fasta","r") as fasta_read:
	for line in fasta_read:
		found = re.search(r">(\S+)\s?.*", line)
		if found:
			continue
			#print(f'seq id: {seq_id}')
		else:

			line = line.rstrip()
			#print(f'Found line {line}')
			string += line
#print(string[3])
#apo_sites = re.findall(r"[AG]ATT[CT]",string)
#print(apo_sites)

for found in re.finditer(r"([AG])(ATT[CT])",string):
	#print(f'group1: {found.group(1)}, group2: {found.group(2)}')
	tial = found.group(1) + "^" + found.group(2) 
	#print(tial)
	#print("\n")
new_string = re.sub(r"([AG])(ATT[CT])",tial,string)
#print(f'new string: {new_string}')


# convert the string into a list based on ^ and then sort based on len (electrophoresis problem)
my_list = new_string.split("^")
print(my_list)
print("\n")
my_list.sort(key=len)
print(my_list) 
