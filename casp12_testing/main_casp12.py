import os
from calculate_Q1 import obtain_Q1
from obtain_number_of_residues import obtain_num

#Create directory for storing rankings and associated deviations from
#expected Q1 values given the Q1 proportion:
try:
    os.system("mkdir rankings_and_deviations_from_expected/")
except:
    #(The directory was already created).
    pass

#Generate input file from the rankings_data directory. This input file will
#contain the names of the sub-input files. Each sub-input file contains for one given
#protein the different predictions ranked according to their accuracy:
os.system("ls rankings_data >temp_file.tmp")
f = open("temp_file.tmp", "r")
lines = f.readlines()
f.close()
#Remove temporary file:
os.system("rm temp_file.tmp")

#Parse input file:
for i in lines:
    try:
        #If "-D" in i then there are no sub-input files associated:
        if ("-D" not in i):
            #Read sub-input file:
            g = open("rankings_data/" + i.split()[0], "r")
            lines_of_g = g.readlines()
            g.close()
            #Open one output file:
            f2 = open("rankings_and_deviations_from_expected/" + i.split()[0][0 : 5] + "_ranking_and_deviation_from_expected.txt", "wt")    
            #Parse sub-input file:
            #raiz is the name of the protein:
            raiz = i.split()[0][0 : 5]
            for j in lines_of_g:
                try: 
                    #If it is a line of the sub-input file with relevant information:
                    if raiz in j:
                        #Extract the ranking and the name of the pdb file:
                        ranking = j.split()[0]      
                        nombre_fichero = j.split()[1]
                        #Generate the path of the pdb file:
                        path_of_pdb_file = "predictions_data/" + raiz + "/" + raiz + "/" + nombre_fichero
                        #Calculate Q1 and number of residues:
                        value_of_Q1 = float(obtain_Q1(path_of_pdb_file))
                        num_residues = obtain_num(path_of_pdb_file)
                        #Calculate expected value of Q1 given the Q1 proportion:
                        expected_value = -0.5863 + float(num_residues) * 0.431 + float(num_residues * num_residues) * 0.00003254
                        #Calculate absolute difference from expected value:
                        abs_diff_from_expected_value = abs(expected_value - value_of_Q1)
                        #Write in the correspondant output file:
                        f2.write(ranking + "\t" + str(abs_diff_from_expected_value) + "\n")
                except:
                    print j + " could not be analyzed"
                    pass

            f2.close()
 
    except:
        pass



