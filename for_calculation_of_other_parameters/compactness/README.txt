Just execute main_compactness.py on a terminal.
For example, if the terminal session is in the present directory, it would work with the instruction:
python main_compactness.py pdb_entry_type.txt
(Note: The pdb_entry_type.txt file* from ftp://ftp.wwpdb.org/pub/pdb/derived_data/pdb_entry_type.txt
would need to be copied before to the present directory).

Explanation:
The script main_compactness.py receives as parameter the path to
the pdb_entry_type.txt file, and proceeds as follows:
0)Creates a file named "pdb_id_and_obtained_compactness.txt".
1)Reads a line (starting with the first) of the pdb_entry_type.txt file.
2)If the line is that corresponding to a protein --i.e if the line
contains the word "prot"-- then the pdb code contained in that line
is downloaded from the RCSB database. Then the pdb file is checked
to determine whether it has been resolved by X-Ray diffraction, and
if so, the compactness associated with that pdb id is calculated.
3)Then, the pdb code and the calculated compactness are are appended 
to the pdb_id_and_obtained_compactness.txt file.
4)Proceeds in the same manner with the rest of lines of the
pdb_entry_type.txt file.

Already computed results are available in the already_computed_results 
directory.

(*)
Berman, H. et al. The Protein Data Bank. Nucleic Acids Res 28, 235-242 (2000).
RCSB PDB: Homepage. Rcsb.org (2018) at <http://www.rcsb.org/> .
