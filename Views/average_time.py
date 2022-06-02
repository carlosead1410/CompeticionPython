from Controller import clear_screen


def average_time(dic:dict)->dict:
    print("**********   PROMEDIO DE TIEMPO DE CADA GRUPO  **********\n")
    average_time_junior_mens = dic["average_time_junior_mens"]
    average_time_junior_womens = dic["average_time_junior_womens"]
    
    average_time_senior_mens = dic["average_time_senior_mens"]
    average_time_senior_womens = dic["average_time_senior_womens"]
    
    average_time_master_mens = dic["average_time_master_mens"]
    average_time_master_womens = dic["average_time_master_womens"]
    
   
    # Imprimiendo Encabezado
    print ("-------------------------------------------------")
    print ("|{:15}|{:15}|{:15}|".format('Grupo'.center(15),'Masculino'.center(15), 'Femenino'.center(15)))
    print ("-------------------------------------------------")

    #Imprimiendo Promedio Junior
    print ("|{:15}|{:15}|{:15}|".format('Juniors'.center(15),str(average_time_junior_mens).center(15),str(average_time_junior_womens).center(15)))
    print ("-------------------------------------------------")

    #Imprimiendo Promedio Senior
    print ("|{:15}|{:15}|{:15}|".format('Senior'.center(15),str(average_time_senior_mens).center(15),str(average_time_senior_womens).center(15)))
    print ("-------------------------------------------------")
    
    #Imprimiendo Promedio Master
    print ("|{:15}|{:15}|{:15}|".format('Master'.center(15),str(average_time_master_mens).center(15),str(average_time_master_womens).center(15)))

    print ("-------------------------------------------------")


    wait = input("\nPresione una tecla para continuar")
    clear_screen()
    return dic