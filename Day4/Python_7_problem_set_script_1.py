#! /usr/bin/env python3
import re

# Find occurrence nobody and print out position
# Replace Nobody with favorite name and output in file with name.txt
with open("Python_07_nobody.txt","r") as text, open("Sean.txt","w") as text_write:
	for line in text:
		for nobody in re.finditer(r"(Nobody)", line):
			new_phrase = re.sub(r"Nobody", r"Sean", line)
			text_write.write(f'{new_phrase}\n')
			#print(f'Found "Nobody" in position {start} of line: {line} ')
			print(new_phrase)


