from Bio.PDB import *

def obtain_num(pdb_file_path):
    '''Obtains number of residues of a protein'''
    #Preparation for the use of Bio.PDB module (see http://biopython.org/wiki/The_Biopython_Structural_Bioinformatics_FAQ):
    parser = PDBParser()

    #Obtain the structure object:
    estructura = parser.get_structure('X', pdb_file_path)

    #Obtain the residues object:
    residuos = estructura.get_residues()
    #Obtain a list with all the residues:
    list_residues = []
    for i in residuos:
        list_residues.append(i)
    return(len(list_residues))
