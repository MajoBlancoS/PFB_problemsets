#! /usr/bin/env python3

# Reverse compement of each sequence in Python_06.seq.txt
# Print output in FASTA format seq name and a note in description that this is rev complement
# Print stdout and capture output into a file in comman line redirect >

with open("Python_06.seq.txt","r") as seq_file_obj:
	for line in seq_file_obj:
		line_to_upper = line.upper()
		line_to_upper = line_to_upper.rstrip()
		# since each line comes with name and then sequence, I will split the elements first
		gene_id,seq = line_to_upper.split("\t")
		complement = seq.replace("A","%temporaryA%").replace("T","A").replace("G","%temporaryG%").replace("C","G").replace("%temporaryA%","T").replace("%temporaryG%","C")
		reverse_complement = complement[::-1]
		print(f'>{gene_id} reverse_complement\n{reverse_complement}')
