#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 10:43:31 2021

@author: lillycummins
"""

#Motive: given a pan_genome_reference.fa file with numerical identifiers as headers, 
#go into the corresponding gene_data.csv to retrieve the unique geneID relating to a numerical identifier
#to then search for that gene ID in the gene_presence_absence.csv to find the appropriate 
#group name to replace the numerical identifier with.

import argparse
import os
import time
import csv
import subprocess
import sys

parser = argparse.ArgumentParser(description='Replaces numeric identifiers with group names.')
parser.add_argument("--reference", "-i", type=str, required=True) #pan_ref file with numerical identifiers
parser.add_argument("--matrix", "-m", type=str, required=True) #gene p/a matrix
parser.add_argument("--gene", "-g", type=str, required=True) #gene_data file
parser.add_argument("--output", "-o", type=str, required=True) #name of newly labelled pan_ref file to output
args = parser.parse_args()

#check user input
if not os.path.isfile(args.reference):
    print('Cannot find input fasta file.')
    print('Exiting')

if not os.path.isfile(args.matrix):
    print('Cannot find input matrix file.')
    print('Exiting')
    
if not os.path.isfile(args.gene):
    print('Cannot find input gene data file.')
    print('Exiting')

#if output is left empty make file name with time stamp
if args.output == None:
    args.output = os.path.join(os.getcwd(),'pan_reference_'+time.strftime('%Y%m%d_%H%M')) + os.sep
elif not os.path.isdir(args.output):
    os.makedirs(args.output)

print("Reading...")    
with open(args.gene) as gene_data: #head -n 100 gene_data.csv > gene_data.small
    ident_dict = {}
    reader = csv.reader(gene_data, delimiter=',')
    next(reader) #skip header line
    for line in gene_data:
    #ESC_AA7740AA_AS,gnl|Centre|ESC_AA7740AA_AS_3,0_0_0,ESC_AA7740AA_AS_00001,MSDDISLAMEGALAVIAVVGVYCLVVFLMDRLGN,ATGTCGGATGATATTTCACTGGCAATGGAAGGTGCGCTGGCTGTTATTGCTGTTGTGGGCGTTTACTGCCTGGTTGTGTTTTTGATGGATCGACTAGGGAACTGA,,hypothetical protein
        linearr = line.split(",")
        ident = linearr[2]
        geneID = linearr[3]
        if ident not in ident_dict:
            ident_dict[ ident ] = [ geneID ] #ident_dict[ ident ].append(geneID)
        else:
            print("Warning: this identifier has been seen multiple times.")
            
print("Finished reading "+args.gene+".")

print("Assigning...")
for ident in ident_dict: #https://realpython.com/iterate-through-dictionary-python/#iterating-through-keys-directly
  geneIDoi = ident_dict[ ident ]
  genecluster_line = subprocess.getoutput("grep \"" +geneIDoi[0]+"\" "+args.matrix+"")
  genecluster = genecluster_line.split(",")[0] #cluster name is first entry in p/a matrix
  ident_dict[ ident ].append(genecluster)

print("Finished assigning cluster names to all numerical identifiers.")

print("Writing...")
output = open(args.output+'.fasta', 'w')
with open(args.reference) as pan_ref: #, open(args.gene) as gene_data:
    #ident_dict={} #initialise dictionary
    for line in pan_ref:        
        if line.startswith(">"): #its a fasta header
            ident = line[1:].rstrip() #e.g. 0_1_0
            if ident in ident_dict.keys(): #try/catch
            #try{
            	genecluster = ident_dict[ ident ][1] #ident isn't in the dictionary?
            #} catch Exception:
            #  print("Error..")
             # }
            else:
              print("Error: " +ident+ " not found in " +args.gene+"")
              sys.exit()
            output.write(">"+genecluster+"\n")
        else:
          output.write(line) #\n?
        #quit() \n?            

print("Complete.")            
