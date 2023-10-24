#!/usr/bin/env python

import os, sys
import math
from sequence_to_kmer_list import *
from fastq_file_to_sequence_list import *


## method: count_kmers(kmer_list)
##
##  Counts the frequency of each kmer in the given list of kmers
##
##  input parameters:
##
##  kmer_list : list of kmers (type: list)
##               ie.  ["GATC", "TCGA", "GATC", ...]
##
##
##  returns kmer_counts_dict : dict containing ( kmer : count )
##                    ie.  {  "GATC" : 2,
##                            "TCGA" : 1,
##                             ...       }


def count_kmers(kmer_list):

    kmer_count_dict = dict()
    flat_list = []
    ##################
    ## Step 2:
    ## begin your code
    # Counting the number of times a kmer appears in list and saving it into a dictionary, key is the kmer:value
    for lis in kmer_list:
        for kmer in lis:
            flat_list.append(kmer)

    for element in flat_list:
        if element not in kmer_count_dict:
            kmer_count_dict[element] = 0
            #print(f"kmer {element} added to dict") #sanity check
        kmer_count_dict[element] += 1
        #print(f"counting +1 in {element}")
    ## end your code
    ################

    return kmer_count_dict


def Shan_entropy(kmer):
    length = len(kmer)
    countA = kmer.count("A")
    countC = kmer.count("C")
    countT = kmer.count("T")
    countG = kmer.count("G")
    Shan = 0
    if countA:
        f_A = countA/length
        #print(f"fA {f_A}")
        log = math.log2(f_A)
        #print(f"log {log}")
        HA = (countA * f_A * log)
        #print(f"HA {HA}") #sanity check
        Shan += HA
    if countC:
        f_C = countC/length
        log = math.log2(f_C)
        HC = (countC * f_C * log)
        #print(f"HC {HC}") #sanity check
        Shan += HC
    if countT:
        f_T = countT/length
        log = math.log2(f_T)
        HT = (countT * f_T * log)
        #print(f"HT {HT}")
        Shan += HT
    if countG:
        f_G = countG/length
        log = math.log2(f_G)
        HG = (countG * f_G * log)
        #print(f"HG {HG}")
        Shan += HG
    Shan = -1 * Shan
    return Shan


def main():

    progname = sys.argv[0]

    usage = "\n\n\tusage: {} filename.fastq kmer_length num_top_kmers_show\n\n\n".format(
        progname
    )

    if len(sys.argv) < 4:
        sys.stderr.write(usage)
        sys.exit(1)

    # capture command-line arguments
    fastq_filename = sys.argv[1]
    kmer_length = int(sys.argv[2])
    num_top_kmers_show = int(sys.argv[3])

    seq_list = seq_list_from_fastq_file(fastq_filename)

    all_kmers = list()

    #######################
    ## Step 1:
    ## begin your code, populate 'all_kmers' list with the
    ## collection of kmers from all sequences
    for seq in seq_list:
        kmer_list = sequence_to_kmer_list(seq,kmer_length)
        #print(kmer_list) #sanity check
        all_kmers.append(kmer_list)
    #print(all_kmers) #sanity check
    ## end your code
    #######################

    kmer_count_dict = count_kmers(
        all_kmers
    )  # see step 2 above. You implement this. :-)
    #print(kmer_count_dict) #sanity check
    unique_kmers = list(kmer_count_dict.keys())
    #print(f"unique kmers: {unique_kmers}") #sanity check
    #########################
    ## Step 3: sort unique_kmers by abundance descendingly
    ## (Note, you can run and test without first implementing Step 3)
    ## begin your code       hint: see the built-in 'sorted' method documentation
    #intento = {"ACTG":1, "TGCC":4, "GGCT":3}
    unique_kmers = sorted(unique_kmers, key=lambda kmer: kmer_count_dict[kmer], reverse=True)
    """ Sanity checks
    print(intento_sorted)
    print(f"ultimo item: {kmer_count_dict[intento_sorted[-1]]}\nprimero: {kmer_count_dict[intento_sorted[0]]}")
    print(f"segundo: {kmer_count_dict[intento_sorted[1]]}\ntercero: {kmer_count_dict[intento_sorted[2]]}")
    print(f"penultimo: {kmer_count_dict[intento_sorted[-2]]}\n antepen: {kmer_count_dict[intento_sorted[-3]]}")
    print(f"medio: {kmer_count_dict[intento_sorted[int(len(intento_sorted)/2)]]}")
    """
	## end your code

    ## printing the num top kmers to show
    top_kmers_show = unique_kmers[0:num_top_kmers_show]

    for kmer in top_kmers_show:
        print("{}: {} {}".format(kmer, kmer_count_dict[kmer],Shan_entropy(kmer)))
    #sanity check
    #print(Shan_entropy("TTTTTT"))
    
    sys.exit(0)  # always good practice to indicate worked ok!


if __name__ == "__main__":
    main()
