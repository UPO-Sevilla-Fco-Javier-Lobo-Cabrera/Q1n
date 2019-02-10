#This script receives as parameters i)the path to the
#pdb_entry_type.txt file and ii) the path to the
#BRENDA Database* (brenda_download.txt file) and proceeds as follows:
#0)Creates a file named "pdb_id_and_obtained_system_temperature.txt".
#1)Reads a line (starting with the first) of the pdb_entry_type.txt file.
#2)If the line is that corresponding to a protein --i.e if the line
#contains the word "prot"-- then the pdb code contained in that line
#is downloaded from the RCSB database. Then the pdb file is checked
#to determine whether it has been resolved by X-Ray diffraction, and
#if so, the system temperature for the organism of which the protein
#belongs is calculated.
#3)Then, the pdb code and the correspondant system temperature are
#appended to the pdb_id_and_obtained_system_temperature.txt file.
#4)Proceeds in the same manner with the rest of lines of the
#pdb_entry_type.txt file.

#(*)BRENDA in 2017: new perspectives and new tools in BRENDA 
#Placzek S., Schomburg I., Chang A., Jeske L., Ulbrich M., Tillack J.,
#Schomburg D., Nucleic Acids Res.,45:D380-388 (2017) 
#www.brenda-enzymes.org)

import os
import sys
from calculate_organism_optimum_temperature import species_optimum_temperature

#List of name of species along with their system temperature. This is a list
#of lists, where each sublist contains the species name and the associated
#system temperature:
list_of_species_and_temper = []

#List of species whose system temperature cannot be calculated:
list_of_species_not = []

#0)Creates a file named "pdb_id_and_obtained_system_temperature.txt":
f = open("pdb_id_and_obtained_system_temperature.txt", "w+")

#1)Reads a line (starting with the first) of the pdb_entry_type.txt file:
g = open(sys.argv[1], "r")
lines_of_pdb_entry_type_txt = g.readlines()
g.close()
for j in lines_of_pdb_entry_type_txt:    
    #Reset species name and system temperature to a default value 
    #in case there is an error:
    name_of_species = "--"
    system_temperature = "--"
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
            #Extract the name of the species that produces that protein:
            name_of_species = ""
            g2 = open(pdb_id_of_j + ".pdb", "r")
            lines_of_g2 = g2.readlines()
            g2.close()
            #Remove the temporary file:
            os.system("rm " + pdb_id_of_j + ".pdb")    
            try:         
                #Start the extraction of the species name itself:
                auxiliary_flag = 0
                for w in lines_of_g2:
                    if "ORGANISM_SCIENTIFIC:" in w:
                        aux_variable_2 = 3
                        while aux_variable_2 < len(w.split()):
                            name_of_species = name_of_species + w.split()[aux_variable_2] + " "
                            aux_variable_2 += 1
                        name_of_species = name_of_species[0 : (len(name_of_species )-2)] 
                        name_of_species  = name_of_species.capitalize()
                    
                        auxiliary_flag = 1
                    if auxiliary_flag == 1:
                        break
                #Calculate system temperature:
                #First look in the already analyzed species in case the species has already
                #been analyzed (i.e look in list_of_species_and_temper):
                auxiliary_flag_2 = 0
                for q in list_of_species_and_temper:
                    if name_of_species == q[0]:
                        system_temperature = q[1]
                        auxiliary_flag_2 = 1
                        break
                #Look in list_of_species_not in case it was already tried to calculate the
                #system temperature for that organism and was not possible:
                for r in list_of_species_not:
                    if name_of_species == r:
                        auxiliary_flag_2 = 2

                #If it was not found in list_of_species_and_temper nor in list_of_species_not
                #then calculate the temperature and add the information 
                #to list_of_species_and_temper:
                if auxiliary_flag_2 == 0:
                    system_temperature = species_optimum_temperature(sys.argv[2], name_of_species)
                    list_of_species_and_temper.append([name_of_species, system_temperature])
 
                #3)If the system temperature could be calculated, then the pdb and its 
                #correspondant system temperature are appended to the
                #pdb_id_and_obtained_system_temperature.txt file:
                if auxiliary_flag_2 != 2:
                    f.write(str(pdb_id_of_j) + "\t" + str(system_temperature) + "\n")
               
            except:
                #If the temperature could not be calculated then the species name 
                #is added to list_of_species_not:
                list_of_species_not.append(name_of_species)
        except:
            pass

f.close()



