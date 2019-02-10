#This script receives as parameter the path to the pdb_entry_type.txt 
#file, and proceeds as follows:
#0)Creates a file named "pdb_id_and_obtained_percent_beta.txt".
#1)Reads a line (starting with the first) of the pdb_entry_type.txt file.
#2)If the line is that corresponding to a protein --i.e if the line
#contains the word "prot"-- then the pdb code contained in that line
#is downloaded from the RCSB database. Then the pdb file is checked
#to determine whether it has been resolved by X-Ray diffraction, and
#if so, the percentage of residues in beta strand
#is calculated.
#3)Then, the pdb code and percentage are appended to the
#pdb_id_and_obtained_percent_beta.txt file.
#4)Proceeds in the same manner with the rest of lines of the
#pdb_entry_type.txt file.

import os
import sys
from calculate_percentage_beta_strand import obtain_percentage

#0)Creates a file named "pdb_id_and_obtained_percent_beta.txt":
f = open("pdb_id_and_obtained_percent_beta.txt", "w+")

#1)Reads a line (starting with the first) of the pdb_entry_type.txt file:
g = open(sys.argv[1], "r")
lines_of_pdb_entry_type_txt = g.readlines()
g.close()
for j in lines_of_pdb_entry_type_txt:    
    #2)If the line is that corresponding to a protein (not to a nucleic
    #acid or a protein-nucleic acid complex) and has been determined
    #by diffraction then the pdb code contained 
    #in that line is downloaded from the RCSB database:
    words_of_j = j.split()
    if ((words_of_j[1] == "prot") and (words_of_j[2] == "diffraction")):
        #Extract pdb ID from the line:
        pdb_id_of_j = words_of_j[0]
        #Download that pdb from the RCSB database:
        try:
            os.system("wget https://files.rcsb.org/view/" + pdb_id_of_j + ".pdb")
            #Calculate percentage:
            perc_beta_to_write = obtain_percentage(pdb_id_of_j + ".pdb")
            #3)If the obtain_percentage function works, then the pdb and its 
            #correspondant percentage of residues in beta strand are 
            #appended to the pdb_id_and_obtained_percent_beta.txt file:
            f.write(str(pdb_id_of_j) + "\t" + str(perc_beta_to_write) + "\n")
            #Remove the temporary file:
            os.system("rm " + pdb_id_of_j + ".pdb")             
        except:
            pass         

f.close()


