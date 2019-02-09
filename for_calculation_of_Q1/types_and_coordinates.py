from Bio.PDB import *

def obtain_types_and_coordinates(pdb_file_path):
    '''Generates a list cointaing the residues' types and coordinates'''

    #Generation of a dictionary for the chemical type associated for
    #each amino acid:
    aa_dictionary = {"ARG" : "pos", "HIS" : "pos", "LYS" : "pos", "ASP" : "neg", "GLU" : "neg" , "SER" :    "polar", "THR" : "polar", "ASN" : "polar", "GLN" : "polar", "CYS" : "special", "SEC" : "special", "GLY" : "special", "PRO" : "special", "ALA" : "hydrophobic", "VAL" : "hydrophobic", "ILE" : "hydrophobic", "LEU" :  "hydrophobic", "MET" : "hydrophobic", "PHE" : "hydrophobic", "TYR" : "hydrophobic", "TRP" : "hydrophobic"} 


    #The goal of this function is to: 
    #Generate a list (lista_res) where each element is itself a list containing 
    #four elements: i)the type of residue and ii), iii) and iv) the OX,OY and OZ 
    #coordinates of the centroid of the rectangular 3D box constructed using the most
    #extreme OX, OY and OZ coordinates of the atoms in the residue:
    lista_res = []


    #Preparation for the use of Bio.PDB module (see http://biopython.org/wiki/  The_Biopython_Structural_Bioinformatics_FAQ):
    parser = PDBParser()

    #Obtain the structure object:
    estructura = parser.get_structure('X', pdb_file_path)

    #Obtain the residues object:
    residuos = estructura.get_residues()

    #For every residue:
    for res in residuos:
        #Flag to determine whether the atom under analysis is the first to be
        #analyzed or not in the residue under analysis:
        first_atom_flag = 0
        #Obtain the atoms of the residue:
        atomos_res = Selection.unfold_entities(res, 'A')
        #For every atom in the residue:
        for j in atomos_res:
            #Atom coordinates:
            atom_coordinates = j.get_coord()
            #If it is the first atom analyzed of the residue being studied
            #then the most extreme residue coordinates have to be initialized
            #with its coordinates:
            if first_atom_flag == 0:
                residue_OX_most_negative = atom_coordinates[0]
                residue_OX_most_positive = atom_coordinates[0]
                residue_OY_most_negative = atom_coordinates[1]
                residue_OY_most_positive = atom_coordinates[1]
                residue_OZ_most_negative = atom_coordinates[2]
                residue_OZ_most_positive = atom_coordinates[2]
                #Change first_atom_flag: 
                first_atom_flag = 1
            else:
            #Update (if necessary) the most extreme coordinates of the residue:
                if atom_coordinates[0] < residue_OX_most_negative:
                    residue_OX_most_negative = atom_coordinates[0]
                if atom_coordinates[0] > residue_OX_most_positive:
                    residue_OX_most_positive = atom_coordinates[0]
                if atom_coordinates[1] < residue_OY_most_negative:
                    residue_OY_most_negative = atom_coordinates[1]
                if atom_coordinates[1] > residue_OY_most_positive:
                    residue_OY_most_positive = atom_coordinates[1]
                if atom_coordinates[2] < residue_OZ_most_negative:
                    residue_OZ_most_negative = atom_coordinates[2]
                if atom_coordinates[2] > residue_OZ_most_positive:
                    residue_OZ_most_positive = atom_coordinates[2]     

        #Finally, the identification of the residue type and the addition
        #of a new element to lista_res (inside a try statement to avoid
        #non valid residue types such as H0H):
        try:
            residue_type = aa_dictionary[res.get_resname()]
            lista_res.append([residue_type, (residue_OX_most_negative +  residue_OX_most_positive) / 2,  (residue_OY_most_negative + residue_OY_most_positive) / 2, (residue_OZ_most_negative + residue_OZ_most_positive) / 2]) 
        except:
            pass

    #Return the results:
    return(lista_res)



