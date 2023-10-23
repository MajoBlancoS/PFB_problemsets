#! /usr/bin/env python3
import re
import sys

# takes fasta from user input
# breaks each sequence into codons in just the first reading frame

# Now reverse complement each seq and print out all six reading frames to a file called
# Python_08.codons-6frames.nt
# Translate each of the six reading frames into amino acids
# Python_08.translated.aa
# File is user input
file = sys.argv[1]
my_dict ={ }
file_out = open("Python_08.codons-6frames.nt", "w")
file_out_aa = open("Python_08.translated.aa","w")
file_out_longest = open("Python_08.translated-longest.aa","w")
file_out_longest_orf_all_frames = open("Python_08.translated-longest-orf-frame.aa","w")

translation_table = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}

translated_string = ''

with open(file,"r") as fasta_read:
	for line in fasta_read:
		line = line.rstrip()
		found = re.search(r">(\S+)\s?.*",line)
		if found:
			seq_id = found.group(1)
			my_dict[seq_id] = { }
			my_dict[seq_id]['sequence'] = ''
			my_dict[seq_id]['frame1'] = { }
			my_dict[seq_id]['frame1']['codons'] = [ ]
			my_dict[seq_id]['frame1']['translation'] = ''
			my_dict[seq_id]['frame1']['peptides'] = [ ]
			my_dict[seq_id]['frame2'] = { }
			my_dict[seq_id]['frame2']['codons'] = [ ]
			my_dict[seq_id]['frame2']['translation'] = ''
			my_dict[seq_id]['frame2']['peptides'] = [ ]
			my_dict[seq_id]['frame3'] = { }
			my_dict[seq_id]['frame3']['codons'] = [ ]
			my_dict[seq_id]['frame3']['translation'] = ''
			my_dict[seq_id]['frame3']['peptides'] = [ ]
			my_dict[seq_id]['frame4'] = { }
			my_dict[seq_id]['frame4']['codons'] = [ ]
			my_dict[seq_id]['frame4']['translation'] = ''
			my_dict[seq_id]['frame4']['peptides'] = [ ]
			my_dict[seq_id]['frame5'] = { }
			my_dict[seq_id]['frame5']['codons'] = [ ]
			my_dict[seq_id]['frame5']['translation'] = ''
			my_dict[seq_id]['frame5']['peptides'] = [ ]
			my_dict[seq_id]['frame6'] = { }
			my_dict[seq_id]['frame6']['codons'] = [ ]
			my_dict[seq_id]['frame6']['translation'] = ''
			my_dict[seq_id]['frame6']['peptides'] = [ ]
		else:
			my_dict[seq_id]['sequence'] += line


# Create another dictionary to store the id, the frame, and the position of the longest orf
orf_dir = { }
long_orf = 0
#this created the dictionary with the sequence
# now divide each into codons.

for header in my_dict:
	DNA_seq =  my_dict[header]['sequence']
	#here first I need to reverse complement each sequence
		
	complement_seq = DNA_seq.replace("A","%temporaryA%").replace("T","A").replace("G","%temporaryG%").replace("C","G").replace("%temporaryA%","T").replace("%temporaryG%","C")
	
	#Reverse Complement : {"5'": ^15}{complement_of_test_string[::-1]} 3'""")
	rev_complement_seq = complement_seq[::1]

	my_dict[header]['frame1']['codons'] = re.findall(r"(.{3})", rev_complement_seq)
	print(f"{header}-frame-1-codons")
	file_out.write(f"{header}-frame-1-codons\n")
	file_out_aa.write(f"{header}-frame-1-translation\n")
	file_out_longest.write(f"{header}-frame-1-translation\n")
	print(f"{'   '.join([str(x) for x in my_dict[header]['frame1']['codons']])}")
	file_out.write(f"{'   '.join([str(x) for x in my_dict[header]['frame1']['codons']])}\n")

	# Translation
	for codon in my_dict[header]['frame1']['codons']:
#		my_dict[header]['frame1']['translation'].append(translation_table[codon])
		# convert list of translation into string
		my_dict[header]['frame1']['translation']+=translation_table[codon]
#	print(f"translation: {my_dict[header]['frame1']['translation']}")	
	#print(f"Tranlsation:\n{'-'.join([str(x) for x in my_dict[header]['frame1']['translation']])}")		
	#file_out_aa.write(f"Tranlsation:\n{'-'.join([str(x) for x in my_dict[header]['frame1']['translation']])}\n")	
	print(f"Translation: \n{my_dict[header]['frame1']['translation']}")
	
	#Search for Mto* peptide
	for match_seq in re.finditer(r"\w*(M\w*\*)",my_dict[header]['frame1']['translation']):
		#print(f'Found peptide: {match_seq.group(1)}')
		my_dict[header]['frame1']['peptides'].append(match_seq.group(1))
		#print(f"Found peptides: {my_dict[header]['frame1']['peptides']}")
	
	#sort by length
	my_dict[header]['frame1']['peptides'].sort(key=len)	
	#print(f"Found peptides:{my_dict[header]['frame1']['peptides']}")
	if my_dict[header]['frame1']['peptides']:
		print(f"Found longest peptide:{my_dict[header]['frame1']['peptides'][-1]}")
		file_out_longest.write(f"Found longest peptide:{my_dict[header]['frame1']['peptides'][-1]}\n")
		long_orf = len(my_dict[header]['frame1']['peptides'][-1])
		orf_dir[header] = { }
		orf_dir[header]['frame1'] = my_dict[header]['frame1']['peptides'][-1]
	else:
		print("No peptides generated in this frame")
		file_out_longest.write(f"No peptides generated in this frame\n")
	#I can delete the first letter of the string 5 times
	num = 1
	while num <6:
		frame2_seq = rev_complement_seq[num:]
		frame_key = "frame"+str(num+1)
		my_dict[header][frame_key]['codons'] = re.findall(r"(.{3})", frame2_seq)
		print(f"{header}-{frame_key}-codons")
		file_out.write(f"{header}-{frame_key}-codons\n")
		file_out_aa.write(f"{header}-{frame_key}-translation\n")
		print(f"{'   '.join([str(x) for x in my_dict[header][frame_key]['codons']])}")
		file_out.write(f"{'   '.join([str(x) for x in my_dict[header][frame_key]['codons']])}\n\n")
		
		#tranlation
		for codon in my_dict[header][frame_key]['codons']:
			#my_dict[header][frame_key]['translation'].append(translation_table[codon])
			my_dict[header][frame_key]['translation']+=translation_table[codon]
#		print(f"translation: {my_dict[header][frame_key]['translation']}")
		#print(f"Tranlsation:\n{'-'.join([str(x) for x in my_dict[header][frame_key]['translation']])}")
		#file_out_aa.write(f"Tranlsation:\n{'-'.join([str(x) for x in my_dict[header]['frame1']['translation']])}\n\n")
		print(f"Translation: \n{my_dict[header][frame_key]['translation']}")
		
		#	3search for MTO* Pepptide
		for match_seq in re.finditer(r"\w*(M\w*\*)",my_dict[header][frame_key]['translation']):
			my_dict[header][frame_key]['peptides'].append(match_seq.group(1))
			#print(f"Found peptides: {my_dict[header][frame_key]['peptides']}")
		#sort by length
		my_dict[header][frame_key]['peptides'].sort(key=len)
		#print(f"Found peptides:{my_dict[header][frame_key]['peptides']}")
		if my_dict[header][frame_key]['peptides']:
			print(f"Found longest peptide:{my_dict[header][frame_key]['peptides'][-1]}")
			file_out_longest.write(f"Found longest peptide:{my_dict[header][frame_key]['peptides'][-1]}\n")
			# measure the length of the longest peptide and store it in orf_dict with key and frame to keep track
			if long_orf < len(my_dict[header][frame_key]['peptides'][-1]):
				long_orf = len(my_dict[header][frame_key]['peptides'][-1])
				orf_dir[header] = { }
				orf_dir[header][frame_key] = my_dict[header][frame_key]['peptides'][-1]
			
		else:
			print("No peptides found in this frame")
			file_out_longest.write(f"No peptides found in this frame\n")
		num +=1

# determine which subset of codons produced the longest peptide for each sequence record. Print this to a fourth file in FASTA format (Python_08.orf-longest.nt)
print(f"\n\nOUPUT FILES CREATED")
for key in orf_dir:
	for frame in orf_dir[key]:
		file_out_longest_orf_all_frames.write(f"\n>{key} longest orf is found in frame {frame} and it sequence is:\n {orf_dir[key][frame]}\n")

#print(my_dict['c257_g1_i1'])
file_out.close()
file_out_aa.close()
file_out_longest.close()
file_out_longest_orf_all_frames.close()
