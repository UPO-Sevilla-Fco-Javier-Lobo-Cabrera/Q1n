import math

#The following function receives a list generated by coordinates_Q2.py 
#.It returns the score of that list:
def score_list(list_residues):
    '''Return score given a coordinates_Q2.py list'''
    
    #Variable to store the obtained result (score):
    result_score = 0.0

    #Index to select each residue of residue of list_residues:
    i = 0    

    #Until every residue has been analyzed:
    while i < len(list_residues):
        #Save the index of the residue in order not to make calculations
        #later on with itself:
        j = i
    
        #Another index to select each residue of residue of list_residues:
        k = 0

        while k < len(list_residues):
            #If the residue is not itself:
            if k != j:
                #Calculate the Euclidean distance between the centroid 
                #of the rectangular 3D box of each of the pair of 
                #residues (indexed by i and k, respectively):
                euclid_dist = math.sqrt(((list_residues[i][1] - list_residues[k][1])**2) + ((list_residues[i][2] - list_residues[k][2])**2) + ((list_residues[i][3] - list_residues[k][3])**2))                      
                #Update result_score:
                result_score = result_score + (1 / (euclid_dist**2))


            #Proceed to next residue:
            k += 1

        #Proceed to next residue:
        i += 1

    #Return result:
    return(result_score)



