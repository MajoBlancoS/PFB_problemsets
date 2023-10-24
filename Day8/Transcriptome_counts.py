#! /usr/bin/env python3

# Write a python program that reads in the 'bowtie2.sam' file and generates a table containing the number of reads mapped to each gene.

import gzip
import re

my_dict = {}

f = gzip.open('bowtie2.sam.gz', 'r')
for line in f:
	line=str(line)
	line = line.rstrip()
	#print(line)
	found = re.search(r"\S*\\t{1}(\S*)\^{1}([F][B][t][r]\d*).*",line)
	if found:
		seq_id = found.group(1)
		transcript = found.group(2)
		if seq_id not in my_dict:
			my_dict[seq_id] = {}
			my_dict[seq_id][transcript] = 1
		else:
			if transcript not in my_dict[seq_id]:
				my_dict[seq_id][transcript] = 1
			else:
				my_dict[seq_id][transcript] += 1
	else:
		print("pattern not found")

for gene in my_dict:
	print(f"\nGene name: {gene}")
	for transcript in my_dict[gene]:
		print(f"\tTranscript {transcript} Read count:{my_dict[gene][transcript]}")
f.close()
