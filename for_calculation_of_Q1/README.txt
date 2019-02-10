Just execute main_Q1.py on a terminal (Note: Biopython needs to be installed).
For example, if the terminal session is in the present directory, it would
work with the instruction: python main_Q1.py pdb_entry_type.txt
(Note: The pdb_entry_type.txt file* from ftp://ftp.wwpdb.org/pub/pdb/derived_data/pdb_entry_type.txt
would need to be copied before to the present directory).

Explanation:
The main_Q1.py script receives as parameter the path to the
pdb_entry_type.txt file, and proceeds as follows:
0)Creates a file named "pdb_id_and_obtained_Q1.txt".
1)Reads a line (starting with the first) of the pdb_entry_type.txt file.
2)If the line is that corresponding to a protein --i.e if the line
contains the word "prot"-- then the pdb code contained in that line
is downloaded from the RCSB database.
3)The obtain_Q1 function from
calculate_Q1.py if invoked with a try()
statement, passing as argument the route of the downloaded pdb file.
4)If the obtain_Q1 function works, then the pdb code
and its corresponding Q1 value are appended to 
pdb_id_and_obtained_Q1.txt .
5)Proceed in the same manner with the rest of lines of the
pdb_entry_type.txt file.

Already computed results are available in the already_computed_results 
directory.

(*)
Berman, H. et al. The Protein Data Bank. Nucleic Acids Res 28, 235-242 (2000).
RCSB PDB: Homepage. Rcsb.org (2018) at <http://www.rcsb.org/> .
