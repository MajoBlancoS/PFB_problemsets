#! /usr/bin/env python3
import re
import sys

# takes fasta from user input
# breaks each sequence into codons in just the first reading frame

# Now reverse complement each seq and print out all six reading frames to a file called
# Python_08.codons-6frames.nt
# File is user input
file = sys.argv[1]
my_dict ={ }
file_out = open("Python_08.codons-6frames.nt", "w")
with open(file,"r") as fasta_read:
	for line in fasta_read:
		line = line.rstrip()
		found = re.search(r">(\S+)\s?.*",line)
		if found:
			seq_id = found.group(1)
			my_dict[seq_id] = { }
			my_dict[seq_id]['sequence'] = ''
			my_dict[seq_id]['frame1'] = [ ]
			my_dict[seq_id]['frame2'] = [ ]
			my_dict[seq_id]['frame3'] = [ ]
			my_dict[seq_id]['frame4'] = [ ]
			my_dict[seq_id]['frame5'] = [ ]
			my_dict[seq_id]['frame6'] = [ ]
		else:
			my_dict[seq_id]['sequence'] += line

#this created the dictionary with the sequence
# now divide each into codons.

for header in my_dict:
	DNA_seq =  my_dict[header]['sequence']
	#here first I need to reverse complement each sequence
		
	complement_seq = DNA_seq.replace("A","%temporaryA%").replace("T","A").replace("G","%temporaryG%").replace("C","G").replace("%temporaryA%","T").replace("%temporaryG%","C")
	
	#Reverse Complement : {"5'": ^15}{complement_of_test_string[::-1]} 3'""")
	rev_complement_seq = complement_seq[::1]

	my_dict[header]['frame1'] = re.findall(r"(.{3})", rev_complement_seq)
	print(f"{header}-frame-1-codons")
	file_out.write(f"{header}-frame-1-codons\n")
	print(f"{'   '.join([str(x) for x in my_dict[header]['frame1']])}")
	file_out.write(f"{'   '.join([str(x) for x in my_dict[header]['frame1']])}\n")
	
	#I can delete the first letter of the string 5 times
	num = 1
	while num <6:
		frame2_seq = rev_complement_seq[num:]
		frame_key = "frame"+str(num+1)
		my_dict[header][frame_key] = re.findall(r"(.{3})", frame2_seq)
		print(f"{header}-{frame_key}-codons")
		file_out.write(f"{header}-{frame_key}-codons\n")
		print(f"{'   '.join([str(x) for x in my_dict[header][frame_key]])}")
		file_out.write(f"{'   '.join([str(x) for x in my_dict[header][frame_key]])}\n\n")
		num +=1
#print(my_dict['c257_g1_i1'])
file_out.close()
