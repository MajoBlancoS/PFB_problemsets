#! /usr/bin/env python3
import re
## Genome assembly problem set
# Using ecoli-0.75.contigs.fasta file, write a script that reports
	# The number of contigs in the file
	# Shortest contig
	# Longest contig
	# Total contig length
	#L50 and N50

# N50 (sort largest to smalles, 50% of the genome is N50 size)
# L50

file = "ecoli_0.25.contigs.fasta"
count = 0
my_dict = { }
length_longest = 0
length_shortest = 30
my_dict_shortest = { }
total_contig_count = 0
contig_len_list = [ ]
n = 0
suma = 0

with open(file,"r") as file_read:
	for line in file_read:
		line = line.rstrip()
		found = re.search(r">(\S+)\s?.*",line)
		if found:
			count += 1
			seq_id = found.group(1)
			continue
		else:
			total_contig_count += len(line)
			contig_len_list.append(len(line))
			if length_longest < len(line):
				my_dict[seq_id] = { }
				my_dict[seq_id]['sequence'] = line
				my_dict[seq_id]['length'] = len(line)
				length_longest = len(line)
			if length_shortest > len(line):
				my_dict_shortest[seq_id] = { }
				my_dict_shortest[seq_id]['sequence'] = line
				my_dict_shortest[seq_id]['length'] = len(line)
				length_shortest = len(line)
print(f"Cuenta: {count}\nlongest contig: {my_dict}\nShortest contigs: {my_dict_shortest}\nTotal contig length: {total_contig_count}")
contig_len_list.sort()
contig_len_list.reverse()
N50 = int(len(contig_len_list)/2)
print(N50)
print(f"N50: {contig_len_list[N50]}")
while n < N50:
	suma += contig_len_list[n]
	n +=1
print(f"L50 {suma}")
