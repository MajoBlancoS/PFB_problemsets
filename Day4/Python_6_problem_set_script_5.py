#! /usr/bin/env python3

# Go through each line of the file
# Count the number of lines and the number of characters per line
# Report total number of lines, characters and average line length

number_of_lines = 0
number_of_characters = 0
average_line_length = 0

with open("Python_06.fastq", "r") as fasta_read:
	for line in fasta_read:
		number_of_lines += 1
		char = len(line)
		number_of_characters += char
print(f'Total number of lines: {number_of_lines}')
print(f'Total number of characters: {number_of_characters}')
average_line_length = number_of_characters / number_of_lines
print(f'Therefore, average line length: {average_line_length}')
