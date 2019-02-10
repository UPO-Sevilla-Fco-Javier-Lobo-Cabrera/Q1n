Just open a terminal session in this directory and execute:
python main_casp12.py
(Note: Biopython needs to be installed).

As a result of the execution of main_casp12.py in the rankings_and_deviations_from_expected directory output files will be created. Each of these output files will contain for a protein target the rankings of the different simulations and their absolute deviation from the expected value according to the Q1n function.

predictions_data and rankings_data are directories containing necessary input files for the execution of main_casp12.py . To create these directories the scripts download_predictions_data.py and download_rankings_data.py are available.

Already computed results are available in the already_computed_results 
directory.
