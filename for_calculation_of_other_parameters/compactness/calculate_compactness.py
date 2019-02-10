from Bio.PDB import *
from obtain_number_of_residues import obtain_num
import math

def obtain_compactness(pdb_file_path):
    '''Calculates the residue density in the sphere containing all the atoms of the protein'''

    ##FIRST, the 3D box of each residue is going to be generated:
    #Each residue's 3D box is constructed using the most extreme atom coordinates of the residue.

    #Generate lists where each element is the extreme (minor major) OX,OY and OZ coordinates of the atoms in the residue:
    list_of_extreme_minor_OX_coordinates_of_residues = []
    list_of_extreme_major_OX_coordinates_of_residues = []
    list_of_extreme_minor_OY_coordinates_of_residues = []
    list_of_extreme_major_OY_coordinates_of_residues = []
    list_of_extreme_minor_OZ_coordinates_of_residues = []
    list_of_extreme_major_OZ_coordinates_of_residues = []


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

        #Update the list of the extreme coordinates:
        try:
            list_of_extreme_minor_OX_coordinates_of_residues.append(residue_OX_most_negative) 
            list_of_extreme_major_OX_coordinates_of_residues.append(residue_OX_most_positive)
            list_of_extreme_minor_OY_coordinates_of_residues.append(residue_OY_most_negative)
            list_of_extreme_major_OY_coordinates_of_residues.append(residue_OY_most_positive)
            list_of_extreme_minor_OZ_coordinates_of_residues.append(residue_OZ_most_negative)
            list_of_extreme_major_OZ_coordinates_of_residues.append(residue_OZ_most_positive)
        except:
            pass

    ##SECOND, Obtain the diameter necessary for a sphere containing 
    #all the atoms in the protein:
    minimum_OX_coordinate = min(list_of_extreme_minor_OX_coordinates_of_residues)
    maximum_OX_coordinate = max(list_of_extreme_major_OX_coordinates_of_residues)
    difference_between_OX_extreme_coordinates = maximum_OX_coordinate - minimum_OX_coordinate

    minimum_OY_coordinate = min(list_of_extreme_minor_OY_coordinates_of_residues)
    maximum_OY_coordinate = max(list_of_extreme_major_OY_coordinates_of_residues)
    difference_between_OY_extreme_coordinates = maximum_OY_coordinate - minimum_OY_coordinate    

    minimum_OZ_coordinate = min(list_of_extreme_minor_OZ_coordinates_of_residues)
    maximum_OZ_coordinate = max(list_of_extreme_major_OZ_coordinates_of_residues)
    difference_between_OZ_extreme_coordinates = maximum_OZ_coordinate - minimum_OZ_coordinate  
 
    list_of_differences = [difference_between_OX_extreme_coordinates, difference_between_OY_extreme_coordinates, difference_between_OZ_extreme_coordinates]
    
    diameter_of_sphere = max(list_of_differences)

    ##THIRD, Obtain number of residues:
    num_residues = obtain_num(pdb_file_path)
    ##FOURTH, Calculate residue density in the sphere:
    volume_of_sphere = (4.0/3.0)*math.pi*math.pow((diameter_of_sphere/2), 3)
    residue_density = num_residues / volume_of_sphere

    print "minimum_OX_coordinate, maximum_OX_coordinate, minimum_OY_coordinate, maximum_OY_coordinate, minimum_OZ_coordinate, maximum_OZ_coordinate, diameter_of_sphere, num_residues, volume_of_sphere, residue_density"
    print minimum_OX_coordinate, maximum_OX_coordinate, minimum_OY_coordinate, maximum_OY_coordinate, minimum_OZ_coordinate, maximum_OZ_coordinate, diameter_of_sphere, num_residues, volume_of_sphere, residue_density
    return residue_density




