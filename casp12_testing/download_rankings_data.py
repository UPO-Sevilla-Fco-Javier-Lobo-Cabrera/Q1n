import os

#Read the file containing the targets:
f = open("list_of_targets.txt", "r")
lines = f.readlines()
f.close()

#Create directory for storing the rankings:
os.system("mkdir rankings_data/")

#Download the rankings and store them in the rankings_data directory:
for i in lines:
    os.system("wget http://predictioncenter.org/download_area/CASP12/SUMMARY_TABLES/" + i.split()[1] + " -O rankings_data/" + i.split()[1])
