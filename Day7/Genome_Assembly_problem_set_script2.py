#! /usr/bin/env python3

## Problem B write a script that parses a fasta file of Dmelanogaster chromosome assembly, and identify the following:
	# How many contigs?
	# Nucleotide content
		# masked and unmasked
	# Proportion of the genome that is comprised of gaps

import re

def nuc_content(dna):
	C_count = dna.count("C")
	G_count = dna.count("G")
	dna_len = len(dna)
	A_count = dna.count("A")
	T_count = dna.count("T")
	c_count = dna.count("c")
	g_count = dna.count("g")
	a_count = dna.count("a")
	t_count = dna.count("t")
	N_count = dna.count("N")
	return A_count, T_count, C_count, G_count, a_count, t_count, c_count, g_count, N_count, dna_len


my_dict ={ }
file = "D_melanogaster_genomic.fna"
count = 0
A = 0
T = 0
C = 0
G = 0
a = 0
t = 0
c = 0
g = 0
N = 0
dna_len = 0

with open(file, "r") as file_read:
	for line in file_read:
		line = line.rstrip()
		found = re.search(r">(\S+)\s?.*",line)
		if found:
			count += 1
		else:
			nuc_contente = nuc_content(line)
			#print(nuc_contente[0])
			A += nuc_contente[0]
			T += nuc_contente[1]
			C += nuc_contente[2]
			G += nuc_contente[3]
			a += nuc_contente[4]
			t += nuc_contente[5]
			c += nuc_contente[6]
			g += nuc_contente[7]
			N += nuc_contente[8]
			dna_len += nuc_contente[9]
			
print(count)
gaps = N/dna_len
print(f"A number: {A}\nG number: {G}\nC: {C}\nT: {T}\na: {a}\ng: {g}\nc: {c}\nt: {t}\n total_dna: {dna_len}")
print(f"proportion gaps {gaps:.2%}")
