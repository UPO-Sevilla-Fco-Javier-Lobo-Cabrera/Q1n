import os
#Read file containing the targets:
f = open("list_of_targets.txt", "r")
lines = f.readlines()
f.close()

#Create directory for storing the predictions:
os.system("mkdir predictions_data/")

#Auxiliary counter:
j = 0 

#Download predictions and store them in the predictions_data directory:
while (j < len(lines)):
    os.system("mkdir predictions_data/" + lines[j].split()[1][0 : 5])

    os.system("wget http://predictioncenter.org/download_area/CASP12/predictions/" + lines[j].split()[1][0 : 5] + ".tar.gz -O predictions_data/" + lines[j].split()[1][0 : 5] + "/" + lines[j].split()[1][0 : 5] + ".tgz")

    os.system("tar xvf ficheros_predicciones/" + lines[j].split()[1][0 : 5] + "/" + lines[j].split()[1][0 : 5] + ".tgz --directory predictions_data/" + lines[j].split()[1][0 : 5] + "/")    

    j += 1
