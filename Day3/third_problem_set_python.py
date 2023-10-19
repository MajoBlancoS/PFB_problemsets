#! /usr/bin/env python3
import sys

# Answers to problem set 3: Set --Strings
# Create a variable named 'DNA' which contains the sequence
DNA = "GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG"

# Count the number of As
#print(DNA.count("A")) #167

# Count the number of T's
#print(DNA.count("T")) #187

# Count the number of G's
#print(DNA.count("G")) #218

# Count the number of C's
#print(DNA.count("C")) #270

# Create a variable named bird with the contents "chicken"
bird = "chicken"

# Convert the contents of bird to be uppercase and print
#print(bird.upper())

# Create a script that counts the number of A's, T's, C's and G's irregardless of case
# Start with a posititve control that you know (above)
# Creating a positive control but with lower case to test all cases
positive_control = DNA.lower()
#print(f' This is your lowercase positive control: {positive_control}')

# Convert the string to upper
positive_control_to_upper = positive_control.upper()
#print(f'This is your positive control un upper: {positive_control_to_upper}')

# Count A 
number_of_A_in_string = positive_control_to_upper.count("A")
#print(f'This is the number of A in your string: {number_of_A_in_string}')

# Count T
number_of_T_in_string = positive_control_to_upper.count("T")
#print(f'This is the number of T in your string: {number_of_T_in_string}')

# Count G
number_of_G_in_string = positive_control_to_upper.count("G")
#print(f'This is the number of G in your string: {number_of_G_in_string}')

# Count C
number_of_C_in_string = positive_control_to_upper.count("C")
#print(f'This is the number of C in your string: {number_of_C_in_string}')

# Test your script with unkown sequence
test_string = sys.argv[1]
#test_string = "aattggcca"#positive control for AT content
#test_string = "AAaattggttggaaccttggtc" #positive control for extracting from 100 to 200, 22 characters
test_string = "ATGCAGGGGAAACATGATTCAGGAC" #positive control for reverse complement
test_string_to_upper = test_string.upper()
# Count A
number_of_A_in_string = test_string_to_upper.count("A")
# Count T
number_of_T_in_string = test_string_to_upper.count("T")
# Count G
number_of_G_in_string = test_string_to_upper.count("G")
# Count C
number_of_C_in_string = test_string_to_upper.count("C")

print(f"""This is the number of A in your string: {number_of_A_in_string}
This is the number of T in your string: {number_of_T_in_string}
This is the number of G in your string: {number_of_G_in_string}
This is the number of C in your string: {number_of_C_in_string} """)

# Find and replace all instances of T with U in this DNA sequence
positive_control_1_T = "AATCCG"
positive_control_2_T = "AATTGGcc"
positive_control_3_T = "AATTGGTCC"

test_sequence_to_upper = test_string.upper()
print(f"""U-changed sequence:{test_sequence_to_upper.replace("T","U")}""")

# Calculate AT content in this DNA string. AT content is the proportion of bases that are either A or T.
# my positive control is in lines above
proportion_of_AT_in_sequence = (number_of_A_in_string + number_of_T_in_string)/len(test_string)
print(f""" The proportion of AT in your sequence of length {len(test_string)}, is: {proportion_of_AT_in_sequence:.2f}""")

# Calculate GC content
proportion_of_GC_in_sequence = (number_of_G_in_string + number_of_C_in_string)/len(test_string)
print(f"The proportion of GC in your sequence of length {len(test_string)}, is: {proportion_of_GC_in_sequence:.2f} ")

# Extract and print the substring from nucleotide number 100 (not the same as its index) to nucleotide number 200 in this DNA sequence.
# starting small to extract from 10 to 20
substring_10_to_20 = test_string_to_upper[9:20]
#print(f"""Your original sequence: {test_string}
#Your 10 to 20 characters: {substring_10_to_20}""")

# substring 100 to 200 based on what I learned from positive control
substring_100_to_200 = test_string_to_upper[99:200]
print(f"your 100 to 200 characters in your sequence are: {substring_100_to_200}")

#Count the number of G in your substring
print(f'number of G in substring: {substring_100_to_200.count("G")}')

# Write a new script that prints out the reverse complement of the above DNA string.
# Use string formating for printing
#using a nested replace
complement_of_test_string = test_string_to_upper.replace("A","%temporaryA%").replace("T","A").replace("G","%temporaryG%").replace("C","G").replace("%temporaryA%","T").replace("%temporaryG%","C")
print(f"""Original Sequence : {"5'": ^15}{test_string_to_upper} 3'
Complement : {"5'": ^15}{complement_of_test_string} 3' 
Reverse Complement : {"5'": ^15}{complement_of_test_string[::-1]} 3'""")
