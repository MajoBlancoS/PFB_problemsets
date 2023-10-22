#! /usr/bin/env python3

### CLASES Problem set ###

# Create a DNA sequence class that will contain a sequence, its name, and it's organism of origin. Do this by creating an __init__ function

class DNA_sequence_class(object):

	# Define class attributes
	def __init__(self, gene_sequence, gene_name, organism):
		self.gene_sequence = gene_sequence
		self.gene_name = gene_name
		self.organism = organism

	# Define methods
	# GC content method
	def get_GT(self):
		length = len(self.gene_sequence)
		g_count = self.gene_sequence.count("G")
		c_count = self.gene_sequence.count("C")
		gc_content = (g_count + c_count)/ length
		return gc_content

	# Add a method to your class that caclulates and returns the length of the sequence
	def length(self):
		length = len(self.gene_sequence)
		return length
	
	# Add in a method that caclulates and returns the nucleotide composition
	def nucleotide_composition(self):
		a_count = self.gene_sequence.count("A") /len(self.gene_sequence)
		t_count = self.gene_sequence.count("T")/len(self.gene_sequence)
		g_count = self.gene_sequence.count("G")/len(self.gene_sequence)
		c_count = self.gene_sequence.count("C")/len(self.gene_sequence)
		return a_count, t_count, g_count, c_count

	# FASTA formatter method
	# Add in a method that returns the sequence record in FASTA format.
	def get_FASTA(self):
		header = ">" + self.gene_name + " " + self.organism
		sequence = self.gene_sequence
		return header, sequence

# Write some some lines of code, outside your class (in your main program) that sets the name, DNA sequence, and organism for a gene
dna_rec_obj_1 = DNA_sequence_class("ATGCTAGCTAGATCGATGTGTAAAT","TARA","Drosophila melanogaster")
dna_rec_obj_2 = DNA_sequence_class("ATGTCGATCGATGCGATTATTATCGT","DDX24","Homo sapiens")

# Write some some lines of code, outside your class that
	# uses the object sequence attribute to retrieve and print the sequence
	# uses the object name attribute to retrieve and print the name
	# uses the object organism attribute to retrieve and print the organism
for rec in [dna_rec_obj_1, dna_rec_obj_2]:
	print(f'Sequence: {rec.gene_sequence}\nName: {rec.gene_name}\n Organism: {rec.organism}')	
	# Write some some lines of code, outside your class (in your main program) that gets and prints the sequence length using your new method
	print(f'Length: {rec.length()}')
	# Write some some lines of code, outside your class (in your main program) that gets and prints the sequence nucleotide compositio using your new method
	a_comp = float(rec.nucleotide_composition()[0])
	t_comp = float(rec.nucleotide_composition()[1])
	g_comp = float(rec.nucleotide_composition()[2])
	c_comp = float(rec.nucleotide_composition()[3])
	print(f"Nucleotide composition: A:{a_comp:.2%}, T:{t_comp:.2%}, G:{g_comp:.2%}, C:{c_comp:.2%}")
	# Write some some lines of code, outside your class (in your main program) that gets and prints the sequence GC content using your new method
	print(f"Therefore, GC content = {float(rec.get_GT()):.2%}")
	# Write some some lines of code, outside your class (in your main program) that gets and prints the sequence in FASTA format using your new method
	print(f"FASTA FILE:\n{rec.get_FASTA()[0]}\n{rec.get_FASTA()[1]}")
