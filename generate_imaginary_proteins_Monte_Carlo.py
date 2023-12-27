#This function serves to generate imaginary proteins. Residue cluster size of approximately 10 residues
#is shown in this way to render a Q1 equation with approximately the same slop as that identified
#in real proteins.

import random
import math
import sys


def obtain_types_and_coordinates_imaginary_protein():
    '''Generates a list cointaing the residues' types and coordinates of an imaginary protein'''
	

    ########################################################################################
    #Creation of amino acids in the cubic space:

	#List of (OX, OY, OZ) positions of the already included amino acids:
    list_positions_residues = []


	#Maximum and minimum coordinates of the 3D space (in Angstroms):
    limit_a_OX = 0
    limit_b_OX = 80
    limit_a_OY = 0
    limit_b_OY = 80
    limit_a_OZ = 0
    limit_b_OZ = 80
    
    # Number of residues per cluster:
    residues_per_cluster = 10
    # Initialize also auxiliary variables:
    #Counter of current total residues:
    counter_list_positions_residues = 0
    #Counter of current residues in the cluster being created:
    aux_counter_residues_in_cluster = 0
    #List of spatial positions of the residues in the cluster being created:
    list_positions_residues_in_cluster = []
    #List that will store for each cluster its respective list of spatial
    #positions of the residue:
    list_of_lists_positions_residues_in_cluster = []


	#Calculation of expected number of residues in the cubic space given the 3D cubic volume
	#and the expected residue density. 
    volume_3D_space = (limit_b_OX - limit_a_OX) * (limit_b_OY - limit_a_OY) * (limit_b_OZ - limit_a_OZ)
	#print("Volume of 3D space: " + str(volume_3D_space))
	
	#Calculation of expected density. The density is chosen
	#from a symmetric distribution with maximum probability at 0.001185 and lower probability
	#proportionally to the difference with 0.001185. The value of maximum  probability (0.001185) is the 
	#observed average density in cube of proteins from the PDB and the ends are the Q1 and Q3
	# cuartiles:
    possible_expected_densities = [0.000814 + x * (0.001507 - 0.000814) / (19) for x in range (0, 20)]
    #print(possible_expected_densities)
    weight_possible_expected_densities = [1 - (abs(0.001185 - value)/ 0.001185) for value in possible_expected_densities]
    #print(weight_possible_expected_densities)
    expected_density = random.choices(possible_expected_densities, weights=weight_possible_expected_densities, k=1)
    expected_density = expected_density[0]
	#print("Expected density: " + str(expected_density))
	#Calculation of expected number of residues according to the cubic volume and expected density:
    expected_number_residues = round(volume_3D_space * expected_density, 0)
	
	#print("Expected number of residues: " + str(expected_number_residues))


	#Now proceed with the calculation of the imaginary proteins knowing that the number of residues
	#generated in the cubic space must correspond to the expected density:
    while (counter_list_positions_residues < expected_number_residues):
        position_OX = random.uniform(limit_a_OX, limit_b_OX)
        position_OY = random.uniform(limit_a_OY, limit_b_OY)
        position_OZ = random.uniform(limit_a_OZ, limit_b_OZ)        

        possible_new_residue = (position_OX, position_OY, position_OZ)
		
		#If it is the first residue in the protein (and logically also the first
	    #residue of the first cluster):
        if (counter_list_positions_residues == 0):
            list_positions_residues_in_cluster.append(possible_new_residue)
            aux_counter_residues_in_cluster += 1
            list_positions_residues.append(possible_new_residue)
            counter_list_positions_residues += 1

		#If it is not the first residue in the protein:
        else:    
	
    	    #But if it is the first residue in the cluster being created:
            if (aux_counter_residues_in_cluster == 0):
		        #The only the condition to meet is that the distance with any
		        # of the already existing amino acids is at least 2.4 Angstroms:
                flag_distance = 0
                for position_existing_residue in list_positions_residues:
                    x1, y1, z1 = possible_new_residue
                    x2, y2, z2 = position_existing_residue
                    distance_check = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
                    if distance_check < 2.4:
                        flag_distance = 1
                        break
                #If the condition has been fulfilled then add it as a new residue:        
                if (flag_distance == 0):
                    list_positions_residues_in_cluster.append(possible_new_residue)
                    aux_counter_residues_in_cluster += 1
                    list_positions_residues.append(possible_new_residue)
                    counter_list_positions_residues += 1

            #If it is not the first residue in the cluster being created:
            else:
                #If it is the second residue in the cluster:
                if (aux_counter_residues_in_cluster == 1):
                    #Two conditions must be met:
                    flag_distance = 1

                    #i)
                    #Check that the distance with the other already existing
                    #amino acid in the cluster is lower than 3.8 Angstroms:
                    x1, y1, z1 = possible_new_residue
                    x2, y2, z2 = list_positions_residues_in_cluster[0]
                    distance_check = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
                    if (distance_check < 3.8):
                        flag_distance = 0
                                

                    #ii)
	    	        #Check that the distance with any of the already existing amino acids
	    	        #is at least 2.4 Angstroms:
                    if (flag_distance == 0):    
                        for position_existing_residue in list_positions_residues:
                            x1, y1, z1 = possible_new_residue
                            x2, y2, z2 = position_existing_residue
                            distance_check = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
                            if (distance_check < 2.4):
                                flag_distance = 1
                                break

        		    #If the possible new residue has fulfilled both conditions then add it 
	        	    #as a new residue:
                    if (flag_distance == 0):
                        
                        list_positions_residues_in_cluster.append(possible_new_residue)
                        aux_counter_residues_in_cluster += 1
                        list_positions_residues.append(possible_new_residue)
                        counter_list_positions_residues += 1
                         
                        #If the cluster has already been completed:
                        if (aux_counter_residues_in_cluster == residues_per_cluster):
                            #Update list_of_lists_positions_residues_in_cluster: 
                            list_of_lists_positions_residues_in_cluster.append(list_positions_residues_in_cluster)
                            #Update list_positions_residues_in_cluster: 
                            list_positions_residues_in_cluster = []
                            #Update counter of residues in the current cluster:
                            aux_counter_residues_in_cluster = 0
           
                #If it is the third or more residue in the cluster:                  
                else:                  
                    #Two conditions must be met:
                    flag_distance = 1
                    flag_2_distance = 0

                    #i)
                    #Check that the distance with at least two of the other already
                    #existing amino acids in the cluster is lower than 3.8 Angstroms:
                    for position_residue_in_cluster in list_positions_residues_in_cluster:
                        x1, y1, z1 = possible_new_residue
                        x2, y2, z2 = position_residue_in_cluster
                        distance_check = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
                        if (distance_check < 3.8):
                            flag_2_distance += 1
                        if (flag_2_distance == 2):
                            flag_distance = 0  
                            break  
                                    

                    #ii)
	    	        #Check that the distance with any of the already existing amino acids
	    	        #is at least 2.4 Angstroms:
                    if (flag_distance == 0):    
                        for position_existing_residue in list_positions_residues:
                            x1, y1, z1 = possible_new_residue
                            x2, y2, z2 = position_existing_residue
                            distance_check = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
                            if (distance_check < 2.4):
                                flag_distance = 1
                                break

        		    #If the possible new residue has fulfilled both conditions then add it 
	        	    #as a new residue:
                    if (flag_distance == 0):
                        list_positions_residues_in_cluster.append(possible_new_residue)
                        aux_counter_residues_in_cluster += 1
                        list_positions_residues.append(possible_new_residue)
                        counter_list_positions_residues += 1
                         
                        #If the cluster has already been completed:
                        if (aux_counter_residues_in_cluster == residues_per_cluster):
                            #Update list_of_lists_positions_residues_in_cluster: 
                            list_of_lists_positions_residues_in_cluster.append(list_positions_residues_in_cluster)
                            #Update list_positions_residues_in_cluster: 
                            list_positions_residues_in_cluster = []
                            #Update counter of residues in the current cluster:
                            aux_counter_residues_in_cluster = 0                         
                         
    
    # Select percentage of clusters not to include (to create voids in the cubic space):
    percen_not_to_include = float(random.uniform(0, 30))
    # Number of clusters not to include (to create voids in the cubic space):
    num_clusters_not_to_include = round(len(list_of_lists_positions_residues_in_cluster) * percen_not_to_include / 100, 0)
    #Eliminate those clusters:
    clusters_not_to_include = []
    while (len(clusters_not_to_include) < num_clusters_not_to_include):
        aux_cluster_not_to_include = random.randint(0, len(list_of_lists_positions_residues_in_cluster))
        if (aux_cluster_not_to_include not in clusters_not_to_include):
            clusters_not_to_include.append(aux_cluster_not_to_include)
            
    list_of_lists_positions_residues_in_cluster_new = []
    for i_aux in range(0, len(list_of_lists_positions_residues_in_cluster)):
        if (i_aux not in clusters_not_to_include):
            list_of_lists_positions_residues_in_cluster_new.append(list_of_lists_positions_residues_in_cluster[i_aux])    
    list_of_lists_positions_residues_in_cluster = list_of_lists_positions_residues_in_cluster_new        

	#print("----------------------")
	# print(len(list_positions_residues))
	#for m in list_positions_residues:
	#  print(m)                        
		                                            
	###########################################################################################
	 
	#Generation of a internal 3D subshape of radius x_radius in the OX axis, 
	#y_radius in the OY axis and z_radius in the OZ_axis (for the case
	#of an sphere x_radius = y_radius = z_radius):
	
	# First create a list that contains the residues to be considered (those
	# that have not been eliminated previously):
    residues_to_consider = []
	# For every non-eliminated cluster:
    for aux_list_of_lists in list_of_lists_positions_residues_in_cluster:
        # Add every residue in the cluster to residues_to_consider:
        for aux_2_list_of_lists in aux_list_of_lists:
            residues_to_consider.append(aux_2_list_of_lists)
            
   
    #Flag to indicate if the generated structure is ok:        
    #Structure is ok if:
    #i)the 3D subshape is within the cubic space,
    #ii)the density of the 3D subshape is within the normal range, and
    #iii)the proportion of hydrophobic residues in the 3D subshape
    #after carrying out the generation of the hydrophobic core is 
    #approximately 37.772% (in the range [32.772%, 42.772%])
    flag_structure_ok = 0
    while (flag_structure_ok == 0):
    	
        #Creation of the 3D subshape:        
		                   
        x_radius = random.uniform(12, 60)
        y_radius = random.uniform(12, 60)
        z_radius = random.uniform(12, 60)

        #print("X radius of subshape: " + str(x_radius))
    	#print("Y radius of subshape: " + str(y_radius))
    	#print("Z radius of subshape: " + str(z_radius))
    
        #Flag to indicate whether or not the whole internal 3D subshape would be 
        #within the cubic space:
        flag_sphere = 0
        while (flag_sphere == 0):
		
	    	#Generate coordinates of the center of the possible internal 3D subshape:
            position_OX_center_subshape = random.uniform(limit_a_OX, limit_b_OX)
            position_OY_center_subshape = random.uniform(limit_a_OY, limit_b_OY)
            position_OZ_center_subshape = random.uniform(limit_a_OZ, limit_b_OZ) 
		
	    	#Check that the whole internal 3D subshape would be whithin the cubic space:
            flag_aux = 0
            if (position_OX_center_subshape - x_radius > limit_a_OX):      
                flag_aux = 1
            if (position_OX_center_subshape + x_radius > limit_b_OX):
                flag_aux = 1
            if (position_OY_center_subshape - y_radius > limit_a_OY):      
                flag_aux = 1    
            if (position_OY_center_subshape + y_radius > limit_b_OY):
                flag_aux = 1    
            if (position_OZ_center_subshape - z_radius > limit_a_OZ):      
                flag_aux = 1    
            if (position_OZ_center_subshape + z_radius > limit_b_OZ):    
                flag_aux = 1
            
            
            if flag_aux == 0:    
                flag_sphere = 1
            
            
	    #Generate imaginary protein using the points within the sphere:
        list_positions_residues_imaginary_protein = []
        for m in residues_to_consider:
            x, y, z = m
            if (x >= (position_OX_center_subshape - x_radius)):
                if (x <= (position_OX_center_subshape + x_radius)):
                    if (y >= (position_OY_center_subshape - y_radius)):
                        if (y <= (position_OY_center_subshape + y_radius)):
                            if (z >= (position_OZ_center_subshape - z_radius)):
                                if (z <= (position_OZ_center_subshape + z_radius)):    
                                    list_positions_residues_imaginary_protein.append(m)

        #Check if the new density (the density of the 3D subshape) is within the normal range:
        volume_3D_subshape = 4 * 3.1416 * x_radius * y_radius * z_radius / 3
        density_3D_subshape = len(list_positions_residues_imaginary_protein) / volume_3D_subshape    
        #If too low density the structure is not valid:
        if (density_3D_subshape < min(possible_expected_densities)):
            continue
        #If too high density the structure is not valid:            
        if (density_3D_subshape > max(possible_expected_densities)):                            
            continue


        #print("#############################")
             
    	#Assign of a type (hidrophobic, polar, acidic, basic or special) to each residue.
	    #The expected frequency of each amino acid is calculated based on the number of codons that
	    #code it. For example, if a residue is coded by 4 different codons, since there are 61 different
	    #codons the expected frequency of that amino acid is 4/61. With this, the expected frequency
    	#of each group of amino acids can be calculated:
    	#Since Aspartate and Glutamate are acidic --> probability of neg = 3.28 + 3.28 = 6.56%.
    	#Since Arginine, Histidine and Lysine are basic --> probability of pos =  9.84 + 3.28 + 3.28 = 16.39%.
	    #Since Serine, Threonine, Asparagine and Glutamine are polar --> probability of polar = 9.84 + 6.56 + 3.28 + 3.28 = 22.95%.
    	#Since Alanine, Valine, Isoleucine, Leucine, Methionine, Phenylalanine,
	    #Tyrosine and Triptophane are hydrophobic --> probability of hydrophobic = 6.56 + 6.56 + 4.92 + 9.84 + 1.64 + 3.28 + 3.28 + 1.64 = 37.72%
    	#Since Cysteine, Glycine and Proline are special --> probability of special = 3.28 + 6.56 + 6.56 =16.39%.

        ###################################################################################
        #Emulation of the hydrophobic core:
        #Generate random number of hydrophobic core clusters. Note: although it is random, later the ratio
        #total number of hydrophobic residues/total number of residues is calculated to verify that it 
        #is in the range 37.772 +- 5 %. If the obtained ratio is not obtained then another structure 
        #is generated
        num_clusters_hydrophobic_core = int(round(len(list_of_lists_positions_residues_in_cluster) * random.uniform(0.07, 0.15), 0))
    
        #Obtain average distance to the center of the 3D subshape for each cluster:
        average_distance_to_center_of_clusters = []
        for aux_clusters_distance in list_of_lists_positions_residues_in_cluster:
            distances_to_center = []
            for residue_in_cluster in aux_clusters_distance:
                x, y, z = residue_in_cluster
                distance_of_residue_to_3D_subshape_center = math.sqrt((x - position_OX_center_subshape)**2 + (y - position_OY_center_subshape)**2 + (z - position_OZ_center_subshape)**2)
                distances_to_center.append(distance_of_residue_to_3D_subshape_center)
            
            average_distance_to_center_of_clusters.append(sum(distances_to_center) / len(distances_to_center))        


        #Obtain indices of the num_clusters_hidrofobic_core clusters closest to the center
        #of the 3D internal subshape:   
        indices_hydrophobic_clusters = []
        while (len(indices_hydrophobic_clusters) < num_clusters_hydrophobic_core):
            #Find out the index of the minimum value:
            min_average_distances = min(average_distance_to_center_of_clusters)
            for j_aux in range(0, len(average_distance_to_center_of_clusters)):
                if ((average_distance_to_center_of_clusters[j_aux] - min_average_distances) < 0.0000001):
                    min_index = j_aux
                    break
            indices_hydrophobic_clusters.append(min_index)
            #Assign a high value to the minimum so that it is no longer the minimum element:
            average_distance_to_center_of_clusters[min_index] = 9999999999999999
 
     
    
        #Obtain the indices of the rest of clusters (clusters that will not be hydrophobic):
        indices_non_hydrophobic_clusters = []
        for aux_indices_cluster in range(0, len(list_of_lists_positions_residues_in_cluster)):
            if (aux_indices_cluster not in indices_hydrophobic_clusters):
                indices_non_hydrophobic_clusters.append(aux_indices_cluster)
            
        #Assign specific type to each non hydrophobic cluster according to their expected 
        #weights:
        available_types_of_non_hydrophobic_residue = ["polar", "neg", "pos", "special"]
        weights_of_types_non_hydrophobic_residue = [22.95, 6.56, 16.39, 16.39]
        indices_polar_clusters = []
        indices_neg_clusters = []
        indices_pos_clusters = []
        indices_special_clusters = []

        for aux_indices_non_hydrophobic in indices_non_hydrophobic_clusters:
            type_of_cluster = random.choices(available_types_of_non_hydrophobic_residue, weights=weights_of_types_non_hydrophobic_residue, k=1)
            type_of_cluster = type_of_cluster[0]
            if (type_of_cluster == "polar"):
                indices_polar_clusters.append(aux_indices_non_hydrophobic)
            else:
                if (type_of_cluster == "neg"):
                    indices_neg_clusters.append(aux_indices_non_hydrophobic)
                else:
                    if (type_of_cluster == "pos"):
                        indices_pos_clusters.append(aux_indices_non_hydrophobic)
                    else:
                        indices_special_clusters.append(aux_indices_non_hydrophobic)    
    

        #Generate list of tuples with residue and its type based on the cluster it belongs. These
        #are not necessarily the residues in the 3D subshape, but rather of the entire cubic space:
        list_tuples_residue_type = []
        for i in range(0, len(list_of_lists_positions_residues_in_cluster)):
            for j in list_of_lists_positions_residues_in_cluster[i]:
                 if (i in indices_hydrophobic_clusters):
                     list_tuples_residue_type.append((j, "hydrophobic"))
                 else:
                     if (i in indices_polar_clusters):   
                         list_tuples_residue_type.append((j, "polar"))
                     else:
                         if (i in indices_neg_clusters):   
                             list_tuples_residue_type.append((j, "neg"))
                         else:
                             if (i in indices_pos_clusters):   
                                 list_tuples_residue_type.append((j, "pos"))
                             else:
                                 list_tuples_residue_type.append((j, "special"))

        number_hydrophobic_residues = 0
        number_non_hydrophobic_residues = 0
                                                  
        #print(list_tuples_residue_type)
        #Assign type to each residue in the 3D internal subshape based on 
        # the cluster it belongs:
        list_of_type_and_positions_residues_imaginary_protein = []
        for r in list_positions_residues_imaginary_protein:
    
            # Identify the cluster to which that residue belongs:
            for s in range(0, len(list_tuples_residue_type)):
                x1, y1, z1 = r
                x2, y2, z2 = list_tuples_residue_type[s][0]
                distance_check_identify = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
                if (distance_check_identify < 0.01):
                    type_of_residue = list_tuples_residue_type[s][1]
                    if (type_of_residue == "hydrophobic"):
                        number_hydrophobic_residues += 1
                    else:   
                        number_non_hydrophobic_residues += 1 
                    break
                
            list_result = []
        
            list_result.append(type_of_residue)
        
        
            for e in r:
                list_result.append(e)

            list_of_type_and_positions_residues_imaginary_protein.append(list_result)
        	
        ratio_non_hydrophobic_hydrophobic = 100 * number_hydrophobic_residues / (number_hydrophobic_residues + number_non_hydrophobic_residues)
        if (ratio_non_hydrophobic_hydrophobic >= 32.772):
            if (ratio_non_hydrophobic_hydrophobic <= 42.772):
                flag_structure_ok = 1
                
    
	#Return result:
    return (list_of_type_and_positions_residues_imaginary_protein)
 

                
            

