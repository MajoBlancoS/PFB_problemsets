#! /usr/bin/env python3
import re

# fin all header lines in fasta

with open("Python_07.fasta","r") as fasta_read:
	for line in fasta_read:
		for found in re.finditer(r">(\S+)\s?(.*)",line):
			print(f'id: {found.group(1)} desc: {found.group(2)}')
