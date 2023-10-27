#! /usr/bin/env python3

## INSTRUCTIONS
"""
There are 4 sets of results for each of the two searching algorithms, ssearch and blastp., a set of searches with one random sequence, either 200 aa or 800 aa long with either ssearch (ss_rand5-) or blastp(blast_rand5-), using one of 7 scoring matrices for ssearch and one of 4 for blastp. In addition, there are the same set of searches using 10 query sequences (randall instead of only one (rand5 -- the fifth random sequence).

Your goal this afternoon will be to write a script that reads each of the sets of data from either the SSEARCH or BLASTP outputs and produces a table with each of the scoring matrices as row, and the percent identity, alignment length, and E()-values for columns, for the top hit from each of the searches.

Write a program that will take take an argument from the command line, which you can use to specify either rand5-200 or rand5-800, and concatenate it with a scoring matrix name (BL50, BP62, etc. for SSEARCH, BLOSUM62, BLOSUM80, etc. for BLASTP, so that you can open and each result file and associate the results with a scoring matrix.

To parse the BLASTP tabular output file, you must:
remove the newline character
skip lines beginning with "#"
use line.split('\t') to break each result line into its parts, which are: qseqid, sseqid, percid, alen, mismat, gaps, q_start, q_end, s_start, s_end, evalue, bits 
consider breaking the line up and saving the results to a dictionary with:
this_data=dict(zip(field_names, line.split('\t')))


As soon as you have a result line, save this_data, close the file, and move to the next result file.
Save the results in a dictionary using the matrix name as the key, and then print out the values you want ('percid', 'alen', and 'evalue').
Does the alignment length, percent identity, or evalue depend on the query sequence length?
Compare the SSEARCH results with the BLAST results. Which program gives a better range of alignment lengths and percent identities?
For a more challenging exercise, parse the results from the ss_randall-200... and ss_randall-800... searches, which give the results for 10 random query sequences. Calculate the median percid, alen, and evalue from the 10 results for each scoring matrix.
"""

matrix_dict = { }
file_name = "ss_rand5-200_v_qfo_"
list_files = ["BL50", "BP62", "VT10", "VT160", "VT20", "VT40", "VT80"]
evale_sorted = 500
best_hit = ""
for file in list_files:
	input_file = file_name+file+".txt"
	print(input_file)
	with open(input_file,"r") as file_read:
		for line in file_read:
			line.rstrip()
			evale_sorted = 500
			if line.startswith("#"):
				#print(f"{input_file} line: {line}")
				continue
			else:
				qseqid, sseqid,percid, alen, mismat, gaps, q_start, q_end, s_start, s_end, evale, bits = line.split("\t")
				#matrix_dict[file]={ }
				#matrix_dict[file]["best_hit"] = { }
				print(f"input file {input_file}, evalue: {evale}")
				if evale_sorted > float(evale):
					evale_sorted = float(evale)
					matrix_dict[file]={ }
					matrix_dict[file]["best_hit"] = { }
					matrix_dict[file]["best_hit"]["id"]=sseqid
					matrix_dict[file]["best_hit"]["identity"]=percid
					matrix_dict[file]["best_hit"]["eval"]=evale_sorted
					matrix_dict[file]["best_hit"]["alen"]=alen
					print(f"filename:{input_file} {matrix_dict}")
#for name in list_files:
#	print(f"Identity: {matrix_dict[name]["best_hit"]["identity"]}\tE-value: {matrix_dict[name]["best_hit"]["eval"]}\tAlignemnet length: {matrix_dict[name]["best_hit"]["alen"]}")
print(matrix_dict)		
