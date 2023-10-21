#! /usr/bin/env python3
import sys
import re

# take multi fasta file Python_08.fasta and calculate the nucleotide composition for each sequenc
# use data structure to keep count
# Print out each sequence name and its composition 

# File is user input
#file = sys.argv[1]

#Add in exception handling to a script from Problem Set 8 or any script you have written that uses I/O to open and read a FASTA file
# Throw and handle (try/except) the exception
"""
if no input is provided
if the file cannot be opened
if the file does not end in '.fasta' or '.fa' or '.nt'
if a non ATGCN charcter is found in the sequence"""

try:
	file = sys.argv[1]
	print("User provided file", file)
	if not file.endswith(['.fa','.nt','.fasta']):
		raise ValueError("Not a FASTA or nt file")
except IndexError:
	print("Please provide a file name")
except IOError as ex:
	print("Cant find file", file, ': ', ex.strerror)


#TODO LO QUE ESTA AQUI DEBAJO DEBE DE IR DENTRO DE TRY!!!!!!!!
my_dict ={ }
string = [ ]
with open(file,"r") as fasta_read:
	for line in fasta_read:
		#print(f'This is a line in the file: {line}')
		line = line.rstrip()
		found = re.search(r">(\S+)\s?.*",line)
		if found:
			#print(f"this is header,save as key and continue to another line")
			seq_id = found.group(1)
			my_dict[seq_id] = { }
			my_dict[seq_id]['sequence'] = ''
			my_dict[seq_id]['nt_count'] = { }
			#continue
		else:
			#print(f'this is sequence: {line}')
			my_dict[seq_id]['sequence'] += line
#print(f'This is the final dictionary {my_dict}')

#now that I constructed a dictionary within a dictionary saving headers and sequences, I COUNT

#my_dict['c257_g1_i1']['A'] = 0
#print(my_dict['c257_g1_i1']['A'])

#I tested that I can add letters inside the dictionary with the key fof each header
# I will create it and count at the same time like the T shirt example in book

#print(my_dict['c257_g1_i1'])

for header in my_dict:
	DNA_seq_uniq = set(my_dict[header]['sequence'])	
	for nt in DNA_seq_uniq:
			count = my_dict[header]['sequence'].count(nt)
			my_dict[header]['nt_count'][nt] = count
	print(f"{header}\tA_count:{my_dict[header]['nt_count']['A']}\tT_count:{my_dict[header]['nt_count']['T']}\tG_count:{my_dict[header]['nt_count']['G']}\tC_count:{my_dict[header]['nt_count']['C']}\n\n")
#print(my_dict['c257_g1_i1'])
