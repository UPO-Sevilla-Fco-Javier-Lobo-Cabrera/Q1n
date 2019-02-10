Just execute main_surface_area_per_residue.py on a terminal.
For example, if the terminal session is in the present directory, it would work with the instruction:
python main_surface_area_per_residue.py pdb_entry_type.txt
(Note: The pdb_entry_type.txt file* from ftp://ftp.wwpdb.org/pub/pdb/derived_data/pdb_entry_type.txt
would need to be copied before to the present directory).
(Note: the software vossolvox (Nucleic Acids Res. 2010 Jul 1 38 (Web Server issue): W555-562)
needs to be installed, and its files i)pdb_to_xyzr, ii)atmtypenumbers and iii)Volume.exe need
to be present in the same directory where main_surface_area_per_residue.py is located).


Explanation:
The script main_surface_area_per_residue.py receives as parameter 
the path to the pdb_entry_type.txt file and proceeds as follows:
0)Creates a file named "pdb_id_and_obtained_surf_area_per_res.txt".
1)Reads a line (starting with the first) of the pdb_entry_type.txt file.
2)If the line is that corresponding to a protein --i.e if the line
contains the word "prot"-- then the pdb code contained in that line
is downloaded from the RCSB database. Then the pdb file is checked
to determine whether it has been resolved by X-Ray diffraction, and
if so, the surface area per residue is calculated.
The protein in the pdb code is assessed using software from
Nucleic Acids Res. 2010 Jul 1 38 (Web Server issue): W555-562 to
calculate the surface area per residue of the protein (without the
solvent, ions and heteroatoms).
3)The pdb code along with the surface area per residue ratio of
the protein without heteroatoms are appended to the
pdb_id_and_obtained_surf_area_per_res.txt file.
4)Proceeds in the same manner with the rest of lines of the
pdb_entry_type.txt file.

Already computed results are available in the already_computed_results 
directory.

(*)
Berman, H. et al. The Protein Data Bank. Nucleic Acids Res 28, 235-242 (2000).
RCSB PDB: Homepage. Rcsb.org (2018) at <http://www.rcsb.org/> .
