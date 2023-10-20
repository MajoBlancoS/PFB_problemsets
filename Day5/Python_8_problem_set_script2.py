#! /usr/bin/env python3
import re
import sys

# takes fasta from user input
# breaks each sequence into codons in just the first reading frame

# File is user input
file = sys.argv[1]
my_dict ={ }
file_out = open("Python_08.codons-frame-1.nt", "w")
with open(file,"r") as fasta_read:
	for line in fasta_read:
		line = line.rstrip()
		found = re.search(r">(\S+)\s?.*",line)
		if found:
			seq_id = found.group(1)
			my_dict[seq_id] = { }
			my_dict[seq_id]['sequence'] = ''
			my_dict[seq_id]['codons'] = [ ]
		else:
			my_dict[seq_id]['sequence'] += line

#this created the dictionary with the sequence
# now divide each into codons.

for header in my_dict:
	DNA_seq =  my_dict[header]['sequence']
	my_dict[header]['codons'] = re.findall(r"(.{3})", DNA_seq)
	print(f"{header}-frame-1-codons")
	file_out.write(f"{header}-frame-1-codons\n")
	print(f"{'   '.join([str(x) for x in my_dict[header]['codons']])}")
	file_out.write(f"{'   '.join([str(x) for x in my_dict[header]['codons']])}\n")
#print(my_dict['c257_g1_i1'])
#Print with format

