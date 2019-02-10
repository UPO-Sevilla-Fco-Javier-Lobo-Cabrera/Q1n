import os

def obtain_percentage(pdb_file_path):
    '''Calculates percentage of residues in beta strand of a pdb file'''

    #Use the program mkdssp and redirect result to an auxiliary temporary file:
    #(References to mkdssp: A series of PDB related databases for everyday needs.
    #Wouter G Touw, Coos Baakman, Jon Black, Tim AH te Beek, E Krieger, Robbie P Joosten, 
    #Gert Vriend.#Nucleic Acids Research 2015 January; 43(Database issue): D364-D368.
    #Dictionary of protein secondary structure: pattern recognition of hydrogen-bonded 
    #and geometrical features. Kabsch W, Sander C, Biopolymers. 1983 22 2577-2637.
    #PMID: 6667333; UI: 84128824).
 
    os.system("mkdssp " + pdb_file_path + " >aux_file_" + pdb_file_path[0:4] + ".tmp")
    #Read the temporary file created:
    f = open("aux_file_" + pdb_file_path[0:4] + ".tmp", "r")
    lines_of_aux_file = f.readlines()
    f.close()
    #Remove temporary file:
    os.system("rm " + "aux_file_" + pdb_file_path[0:4] + ".tmp")

    #Calculation of number of residues in beta strand and total number of residues:
    #Auxiliary variable:
    i = 0
    #Initialize residues in beta strand and total number of residues:
    residues_in_beta_strand = 0.0
    num_total_of_residues = 0.0
    #Flag variable:
    bandera = 0
    #For every line of the temporary file:
    while i < len(lines_of_aux_file):
        #Update residues_in_beta_strand and num_total_of_residues:
        if "#  RESIDUE AA STRUCTURE BP1" in lines_of_aux_file[i]:
            bandera = 1
        else:
            if bandera == 1:
                if lines_of_aux_file[i].split()[4] == "E":
                    residues_in_beta_strand = residues_in_beta_strand + 1
                num_total_of_residues = num_total_of_residues + 1
        i += 1

    #Compute percentage:
    percent_r_b_s = (residues_in_beta_strand / num_total_of_residues) * 100 
    
    #Return result:
    return percent_r_b_s






