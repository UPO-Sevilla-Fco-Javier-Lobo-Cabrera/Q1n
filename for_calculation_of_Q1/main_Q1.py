#This script receives as parameter the path to the pdb_entry_type.txt, 
#file, and proceeds as follows:
#0)Creates a file named "pdb_id_and_obtained_Q1.txt".
#1)Reads a line (starting with the first) of the pdb_entry_type.txt file.
#2)If the line is that corresponding to a protein --i.e if the line
#contains the word "prot"-- then the pdb code contained in that line
#is downloaded from the RCSB database.
#3)The obtain_Q1 function from
#calculate_Q1.py if invoked with a try()
#statement, passing as argument the route of the downloaded pdb file.
#4)If the obtain_Q1 function works, then the pdb code
#and its corresponding Q1 value are appended to 
#pdb_id_and_obtained_Q1.txt .
#5)Proceed in the same manner with the rest of lines of the
#pdb_entry_type.txt file.

import os
import sys
from calculate_Q1 import obtain_Q1

#0)Creates a file named "pdb_id_and_obtained_Q1.txt":
f = open("pdb_id_and_obtained_Q1.txt", "w+")

#1)Reads a line (starting with the first) of the pdb_entry_type.txt file:
g = open(sys.argv[1], "r")
lines_of_pdb_entry_type_txt = g.readlines()
for j in lines_of_pdb_entry_type_txt:    
    #Print the current line on the terminal:
    print j
    #2)If the line is that corresponding to a protein (not to a nucleic
    #acid or a protein-nucleic acid complex) then the pdb code contained 
    #in that line is downloaded from the RCSB database:
    words_of_j = j.split()
    if words_of_j[1] == "prot":
        #Extract pdb ID from the line:
        pdb_id_of_j = words_of_j[0]
        #Download that pdb from the RCSB database:
        try:
            os.system("wget https://files.rcsb.org/view/" + pdb_id_of_j + ".pdb")

            #3)The obtain_Q1 function from
            #calculate_Q1.py is invoked with a try()
            #statement, passing as argument the route of the downloaded pdb file:
            try:
                Q1_to_write = obtain_Q1(pdb_id_of_j + ".pdb")
                #4)If the obtain_Q1 function works, then the pdb code
                #and its corresponding Q1 value are appended to 
                #pdb_id_and_obtained_Q1.txt .
                f.write(str(pdb_id_of_j) + "\t" + str(Q1_to_write) + "\n")
            except:
                pass
              
            #Remove the temporary file:
            os.system("rm " + pdb_id_of_j + ".pdb")
        except:
            pass         

f.close()

g.close()




