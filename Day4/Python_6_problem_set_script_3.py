#! /usr/bin/env python3

# Write script to open and read the contents of Python_06.txt
# open and read the contents
# Uppercase each line
# Print each line to stdout

with open("Python_06.txt","r") as text_file_obj:
	for line in text_file_obj:
		upper_line = line.upper()
		upper_line = upper_line.rstrip()
		#print(upper_line)

# Modify to write a new file the output
with open("Python_06.txt","r") as text_read_file_obj, open("Python_06_uc.txt","w") as text_write:
	for line in text_read_file_obj:
		upper_line = line.upper()
		upper_line = upper_line.rstrip()
		text_write.write(f'{upper_line}\n')
print("wrote file")
