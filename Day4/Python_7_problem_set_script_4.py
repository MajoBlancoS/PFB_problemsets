#! /usr/bin/env python3
import re

# Read list of enzymes and cut sites from bionet.txt
# read file and fill a dictionary with enzymes paired with their recognition patterns

enzy_dict = { }
ref = {
	"Y":"[CT]",
	"N":"[ATCG]",
	"M":"[AC]",
	"K":"[GT]",
	"R":"[AG]",
	"B":"[GCT]",
	"D":"[AGT]",
	"V":"[ACG]",
	"H":"[ACT]",
	"S":"[GC]",
	"W":"[AT]",
}

string = ""

with open("bionet.txt","r") as bionet_read:
	for line in bionet_read:
		#print(line)
		line = line.rstrip()
		line = line.upper()
		if line.count("("):
			found = re.search(r"(\w*)\s*(\(\w*\))\s*(\S*)",line) #problem is that some enzymes in the list do not have alias in parenthesis
			#enzyme,description = line.split()
			if found:
				enz_id = found.group(1)
				#print("group1",found.group(1)) #I have the name before parenthesis stored here now
				#search as group(2) the name in parenthesis
				#print("group2",found.group(2))
				enz_name = found.group(2)
				enzy_dict[enz_name] = ""
				#search other sets of spaces
				#search as gorup(3) the sequence
				#print("group3",found.group(3))
				enz_seq = found.group(3)
				enzy_dict[enz_name] = enz_seq 
		else:
			#print("no parenthesis in this line")
			found = re.search(r"(\w*)\s*(\S*)",line)
			if found:
				enz_name = found.group(1)
				enz_seq = found.group(2)
				enzy_dict[enz_name] = ""
				enzy_dict[enz_name] = enz_seq

		#enz_name,pattern = line.split("              ")

#print(f"ref\n{ref}")
#print(f"db {enzy_dict}")
		#print(f'This is enzyme name: {enzyme} \n This is description in parenthesis: {description}')


for enzyme in enzy_dict:
	seq = enzy_dict[enzyme]
	fount = re.search(r"[YNMKRBDVHSW]", seq)
	if found:
		n = 0
		while n < len(seq):
			if (seq[n] == "A") or (seq[n] == "C") or (seq[n] == "T") or (seq[n] == "G") or (seq[n] == "^"):
				n +=1
				#print("ACTG or ^")
				continue
			else:
				replacement = ref[seq[n]]
				#print("replacement",replacement, "original", enzy_dict[enzyme],"nt", seq[n])
				rep =enzy_dict[enzyme].replace(seq[n],replacement)
				#print("rep", rep)
				enzy_dict[enzyme] = rep
				#print("new", enzy_dict[enzyme])
				n += 1

#print(f"\n\n{enzy_dict}")


with open("Python_07_ApoI.fasta","r") as fasta_read:
	for line in fasta_read:
		found = re.search(r">(\S+)\s?.*", line)
		if found:
			continue
		else:
			line = line.rstrip()
			string += line




count = 0
enzyme = "(APOI)"
motif = enzy_dict[enzyme]
problem = motif.count("^")
if problem:
	motif1,motif2 = motif.split("^")
	motif = "("+motif1+")" + "("+motif2+")"
	for found in re.finditer(r"."+motif,string):
		tial = found.group(1) + "^" + found.group(2)
		print("tial",tial)
		new_string = re.sub(r"([AG])(ATT[CT])",tial,string)
		count +=1
	print(f"FOUND {count} for enzyme {enzyme} and motif {motif}")
else:
	motif = "("+motif+")"
	for found in re.finditer(r"."+motif,string):
		tial = found.group(1)
		print("tial",tial)
		count +=1
	print(f"FOUND {count} for enzyme {enzyme} and motif {motif}")
print(motif)

my_list = new_string.split("^")
print(my_list)
print("\n")
my_list.sort(key=len)
print(my_list)		
