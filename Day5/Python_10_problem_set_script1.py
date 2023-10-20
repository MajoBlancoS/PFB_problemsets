#! /usr/bin/env python3
import re
import sys
# Create a function to format a string of DNA so that each line is no more than 60 nt long
# INPUT a string of DNA without newlines
# OUTPUT a string of DNA with lines no more than 60 nucleoties long

dna = "GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT"

dna = '''GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC
GTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACG
CTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATG
CCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
GTCATCTTCT'''

file = sys.argv[1]
width = int(sys.argv[2])
my_dict = { }

def format_DNA_seq(dna, width):
	# Modify your function so that it will work whether the DNA string does or does not have newlines.
	dna_string = ''
	if "\n" in dna:
		for (upstream, downstream) in re.findall(r"(\w*)\n(\w*)",dna):
			up = upstream + downstream
			#print(f'upstream {upstream} \ndownstream: {downstream} \nTherefore, up: {up}')
			dna_string += up
		#print(f'dna without new line: {dna_string}\n')
	else:
		dna_string = dna
		#print(f'No need to delete space: {dna_string}')
	count = 0
	while count < len(dna_string):
		print(''.join([str(x) for x in dna_string[count:count+width]]))
		count += width
		#f"{'   '.join([str(x) for x in my_dict[header][frame_key]])}"
	return

# Now a function to calculate GC CONTENT
def gc_content(dna):
	c_count = dna.count("C")
	g_count = dna.count("G")
	dna_len = len(dna)
	gc_content = (c_count + g_count) / dna_len
	return gc_content

# Fucntion rev complement of a sequence
def reverse_complement(dna):
	complement_seq = dna.replace("A","M").replace("T","A").replace("G","x").replace("C","G").replace("M","T").replace("x","C")	
	
	reverse_complement = complement_seq[::1]
	return reverse_complement

# Opening the file and actually calling the functions
with open(file,"r") as fasta_read:
	for line in fasta_read:
		line = line.rstrip()
		found = re.search(r">(\S+)\s?.*",line)
		if found:
			seq_id = found.group(1)
			my_dict[seq_id] = { }
			my_dict[seq_id]['sequence'] = ''
		else:
			my_dict[seq_id]['sequence'] += line	
		
for header in my_dict:
	print(f'\n\n{header}')
	DNA_seq =  my_dict[header]['sequence']
	format_DNA_seq(DNA_seq, width)
	dna_gc = gc_content(DNA_seq)
	print(f'This sequence is {dna_gc:.2%} GC')
	rev_compl = reverse_complement(DNA_seq)
	print(f'Reverse complement:\n {rev_compl}')
