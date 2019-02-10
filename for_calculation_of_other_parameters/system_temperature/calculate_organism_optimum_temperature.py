#This module contains a function that receives as parameters i) the
#absolute path of the BRENDA Database (brenda_download.txt file)
#and ii) the name of a species, and returns the approximate optimum
#temperature of that species (assuming that it corresponds to the
#average optimum temperature of the enzymes of that species registered
#in the BRENDA Database*).

#(*)BRENDA in 2017: new perspectives and new tools in BRENDA 
#Placzek S., Schomburg I., Chang A., Jeske L., lbrich M., Tillack J.,
#Schomburg D., Nucleic Acids Res.,45:D380-388 (2017) 
#www.brenda-enzymes.org)


def species_optimum_temperature(brenda_file, species_name):
    '''Calculates species optimum temperature'''
    #Store Brenda database:
    f = open(brenda_file, "r")
    lines_of_f = f.readlines()
    f.close()

    #List of temperatures:
    list_of_temperatures_in_celsius = []

    #Auxiliary flags:
    band = 0
    bandera = 0

    #Auxiliary variable to store the line index:
    aux_index = 0
    
    #Set of number associated with that species and the protein (this 
    #is because in one given species_name there may be different
    #strains):
    set_of_numbers_for_that_species = []

    #Parse the BRENDA Database to extract the average optimum
    #temperature:
    for i in lines_of_f:        
        #If there is a protein from the species_name:
        if ((("PR" + "\t" + "#") in i) and (species_name in i)):
            band = 1
            #Extract the number associated with that species for that 
            #protein and add it to the set of number associated with 
            #that species:
            number_for_that_species = ""
            for j in i.split()[1]:
                if j != "#": 
                    number_for_that_species = number_for_that_species + j
                    
            set_of_numbers_for_that_species.append(number_for_that_species)

        #If it is the header of a paragraph of lines containing 
        #optimum temperatures and for this protein there is a protein
        #from species_name:
        if (("TEMPERATURE_OPTIMUM" in i) and (band == 1)):
            #The auxiliary flag bandera becomes 1:
            bandera = 1
        else:
            pass
        
        #If it is a line containing data for optimum temperatures
        #(but not the header) and bandera == 1:
        if (("TEMPERATURE_OPTIMUM" not in i) and (bandera == 1)):
            #bandera becomes 0 and only if the next line contains
            #data for optimum temperatures it becomes 1 again (it
            #is necessary to proceed like this to avoid errors in
            #the execution of the program):
            bandera = 0
            try:
                #If the line contains any of the numbers associated
                #for that protein in that species then the 
                #temperature is extracted:
                for j in set_of_numbers_for_that_species: 
                    if ((("#" + j + ",") in i.split()[1]) or (("," + j + ",") in i.split()[1]) or (("," + j + "#") in i.split()[1])):
                        #Obtain temperature:
                        #If there is not a missing datum:
                        if i.split()[2] != "-999":
                            #Obtain the temperature:
                            temperature = i.split()[2]
                            #If temperature contains a dash ("-") then 
                            #an average has to be calculated:
                            for h in temperature:
                                if h == "-":
                                    temperature_a = float(temperature.split("-")[0]) 
                                    temperature_b = float(temperature.split("-")[1]) 
                                    temperature = (temperature_a + temperature_b) / 2
                            #Convert temperature to float in case it had not been
                            #done before:
                            temperature = float(temperature)
                            #Append to list of temperatures:
                            list_of_temperatures_in_celsius.append(temperature)

            #bandera had become 0 and only if the next line contains
            #data for optimum temperatures it becomes 1 again (it
            #is necessary to proceed like this to avoid errors in
            #the execution of the program):                
                if(lines_of_f[aux_index + 1].split()[0] == "TO"):
                    bandera = 1     
            except:
                pass

        #If it is a new protein then the auxiliary flag band needs to
        #be changed again to 0 and restart set_of_numbers_for_that_species:
        if "PROTEIN" in i:
            band = 0
            set_of_numbers_for_that_species = []

        #Increase the auxiliary variable that store the line index:
        aux_index += 1



    #Compute average temperature obtained:
    summatory_of_temperatures_in_celsius = 0.0
    for h in list_of_temperatures_in_celsius:
        summatory_of_temperatures_in_celsius = summatory_of_temperatures_in_celsius + h    
    average_temperature_obtained_in_celsius = summatory_of_temperatures_in_celsius / len(list_of_temperatures_in_celsius)
    #Transform to Kelvin:
    average_temperature_obtained_in_kelvin = average_temperature_obtained_in_celsius + 273

    #Return result:
    return average_temperature_obtained_in_kelvin
        
   



