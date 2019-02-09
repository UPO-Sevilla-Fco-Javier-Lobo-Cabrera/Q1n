from Bio.PDB import *

def residue_3d_boxes_residues_centroid_coordinates(pdb_file_path):
    '''Generates a list cointaing the residues'  centroid coordinates (one per residue) of each 3D box '''
    #Each residue's 3D box is constructed using the most extreme atom coordinates of the residue.

    #The goal of this function is to: 
    #Generate a list (lista_ res) where each element is itself a list containing 
    #three elements: i)the OX coordinates, ii)the OY coordinates, and iii)the OZ 
    #coordinates of the centroid of the rectangular 3D box constructed using the most
    #extreme OX, OY and OZ coordinates of the atoms in the residue:
    lista_res = []


    #Preparation for the use of Bio.PDB module (see http://biopython.org/wiki/The_Biopython_Structural_Bioinformatics_FAQ):
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

        #Finally, the addition of a new element to lista_res 
        #(inside a try statement to avoid residue types such as H0H):
        try:
            lista_res.append([(residue_OX_most_negative +  residue_OX_most_positive) / 2,  (residue_OY_most_negative + residue_OY_most_positive) / 2, (residue_OZ_most_negative + residue_OZ_most_positive) / 2]) 
        except:
            pass

    #Return the results:
    return(lista_res)










