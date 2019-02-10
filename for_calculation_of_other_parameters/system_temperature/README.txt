Just execute main_system_temperature.py on a terminal.
For example, if the terminal session is in the present directory, it would work with the instruction: 
python main_system_temperature.py pdb_entry_type.txt brenda_download.txt
(Note: The pdb_entry_type.txt file* from ftp://ftp.wwpdb.org/pub/pdb/derived_data/pdb_entry_type.txt
would need to be copied before to the present directory).
(Note: The file brenda_download.txt from the BRENDA Database** needs to be present in this directory).

Explanation:
The script main_system_temperature.py receives as parameters i)the path to the
pdb_entry_type.txt file and ii) the path to the
BRENDA Database* (brenda_download.txt file) and proceeds as follows:
0)Creates a file named "pdb_id_and_obtained_system_temperature.txt".
1)Reads a line (starting with the first) of the pdb_entry_type.txt file.
2)If the line is that corresponding to a protein --i.e if the line
contains the word "prot"-- then the pdb code contained in that line
is downloaded from the RCSB database. Then the pdb file is checked
to determine whether it has been resolved by X-Ray diffraction, and
if so, the system temperature for the organism of which the protein
belongs is calculated.
3)Then, the pdb code and the correspondant system temperature are
appended to the pdb_id_and_obtained_system_temperature.txt file.
4)Proceeds in the same manner with the rest of lines of the
pdb_entry_type.txt file.

Already computed results are available in the already_computed_results 
directory.

(*)
Berman, H. et al. The Protein Data Bank. Nucleic Acids Res 28, 235-242 (2000).
RCSB PDB: Homepage. Rcsb.org (2018) at <http://www.rcsb.org/> .
(**)BRENDA in 2017: new perspectives and new tools in BRENDA 
Placzek S., Schomburg I., Chang A., Jeske L., Ulbrich M., Tillack J.,
Schomburg D., Nucleic Acids Res.,45:D380-388 (2017) 
www.brenda-enzymes.org)

