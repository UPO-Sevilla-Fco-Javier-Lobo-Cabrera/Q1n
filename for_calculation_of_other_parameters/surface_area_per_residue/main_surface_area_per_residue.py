#This script receives as parameter the path to the pdb_entry_type.txt
#file and proceeds as follows:
#0)Creates a file named "pdb_id_and_obtained_surf_area_per_res.txt".
#1)Reads a line (starting with the first) of the pdb_entry_type.txt file.
#2)If the line is that corresponding to a protein --i.e if the line
#contains the word "prot"-- then the pdb code contained in that line
#is downloaded from the RCSB database. Then the pdb file is checked
#to determine whether it has been resolved by X-Ray diffraction, and
#if so, the surface area per residue is calculated.
#The protein in the pdb code is assessed using software from
#Nucleic Acids Res. 2010 Jul 1 38 (Web Server issue): W555-562 to
#calculate the surface area per residue of the protein (without the
#solvent, ions and heteroatoms).
#3)The pdb code along with the surface area per residue ratio of
#the protein without heteroatoms are appended to the
#pdb_id_and_obtained_surf_area_per_res.txt file.
#4)Proceeds in the same manner with the rest of lines of the
#pdb_entry_type.txt file.

import os
import sys
import math
import obtain_number_of_residues

#0)Creates a file named "pdb_id_and_obtained_surf_area_per_res.txt":
f = open("pdb_id_and_obtained_surf_area_per_res.txt", "w+")

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
            #Calculate the surface area per residue:
            ###I)Creation of a pdb file without heteroatoms:
            os.system('''egrep "^ATOM  " ''' + pdb_id_of_j + '''.pdb > ''' + pdb_id_of_j + '''-no_hetatoms.pdb''')
            ###II)Creation of a xyzr file from the pdb file without heteroatoms:
            os.system('''./pdb_to_xyzr ''' + pdb_id_of_j + '''-no_hetatoms.pdb > ''' + pdb_id_of_j + '''-no_hetatoms.xyzr''')
            ###III)Execute the Volume.exe program to generate an auxiliary output file
                # containing the surface area:
            os.system('''./Volume.exe -i ''' + pdb_id_of_j + '''-no_hetatoms.xyzr -p 1.5 -g 0.5 >aux_output_file_''' + pdb_id_of_j + '''.txt''')           
            ###IV)Extract the surface area from the auxiliary output file:
            g2 = open("aux_output_file_" + pdb_id_of_j + ".txt", "r")
            info_of_aux_output_file_txt = g2.readlines()
            g2.close()
            surface_area_of_protein = float(info_of_aux_output_file_txt[0].split()[3])
            ###V)Calculation of the surface area per residue:  
            num_residues = obtain_number_of_residues.obtain_num(pdb_id_of_j + '''-no_hetatoms.pdb''')
            surf_area_per_res_to_write = surface_area_of_protein/num_residues
            #3)If the calculation of the surface area per residue works, then the pdb and its 
            #correspondant surface area per residue are appended to 
            #the pdb_id_and_obtained_surf_area_per_res.txt file:
            f.write(str(pdb_id_of_j) + "\t" + str(surf_area_per_res_to_write) + "\n")
            
        except:
            pass         

        #Remove the temporary files:
        os.system("rm " + pdb_id_of_j + ".pdb")
        os.system("rm " + pdb_id_of_j + "-no_hetatoms.pdb")
        os.system("rm " + pdb_id_of_j + "-no_hetatoms.xyzr")
        os.system("rm " + "aux_output_file_" + pdb_id_of_j + ".txt")

f.close()


