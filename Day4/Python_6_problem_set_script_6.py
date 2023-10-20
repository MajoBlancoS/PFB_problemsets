#! /usr/bin/env python3

# Python_06_revcompl.seq.fasta
# FASTA parser script
# Reads FASTA file and stores each record separately for easy access for future analysis
fasta_dir = { }
key = [ ]
sequences = [ ]

import re
# fin all header lines in fasta
 
with open("Python_07.fasta","r") as fasta_read:
	for line in fasta_read:
		line = line.rstrip()
		found = re.search(r">(\S+)\s?.*",line)
		
		if found:
			#for found in re.finditer(r"(>\S+\s?.*)",line):
			print(f'id: {found.group(1)}')
			seq_id = found.group(1)
			fasta_dir[seq_id] = ""			
#key.append(found.group(1))
		else:
			fasta_dir[seq_id]+=line
			#print("not found")
#print(key)
print(fasta_dir)
