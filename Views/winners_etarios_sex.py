from Controller import clear_screen


def winners_etarios_sex(dic:dict)->dict:
    print("**********   GANADORES POR GRUPO ETARIO Y SEXO   **********\n")
    
    juniors_mens = dic["juniors_mens"]
    juniors_womens = dic["juniors_womens"]
    
    seniors_mens = dic["seniors_mens"] 
    seniors_womens = dic["seniors_womens"]
    
    masters_mens = dic["masters_mens"]
    masters_womens = dic["masters_womens"]
    
    
    #Obtengo los ganadores por sexo de cada grupo etario
    junior_men_winner = juniors_mens[0]
    junior_women_winner = juniors_womens[0]
    
    seniors_men_winner = seniors_mens[0]
    seniors_women_winner = seniors_womens[0]
    
    master_men_winner = masters_mens[0]
    masters_women_winner = masters_womens[0]
    
    print ("-------------------------------------------------------------------------------------------------------------------------------------------------")
    # Imprimiendo Encabezado
    print ("|{:15}|{:63}|{:63}|".format(''.center(15),'Masculino'.center(63),'Femenino'.center(63)))
    print ("-------------------------------------------------------------------------------------------------------------------------------------------------")
    print ("|{:15}|{:10}|{:20}|{:20}|{:10}|{:10}|{:20}|{:20}|{:10}|".format('Grupo'.center(15),'Cedula'.center(10),'Primer Nombre'.center(20),
                                  'Primer Apellido'.center(20),'Tiempo'.center(10),'Cedula'.center(10),'Primer Nombre'.center(20),
                                  'Primer Apellido'.center(20),'Tiempo'.center(10)))
    print ("-------------------------------------------------------------------------------------------------------------------------------------------------")
    
    #Imprimiendo Ganador Juniors por Sexo
    print("|{:15}|{:10}|{:15}|{:15}|{:10}|{:10}|{:15}|{:15}|{:10}|".format('Junior'.center(15), str(junior_men_winner[0]).center(10), str(junior_men_winner[3]).center(20),
                                                    str(junior_men_winner[1]).center(20),str(junior_men_winner[10]).center(10), 
                                                    str(junior_women_winner[0]).center(10), str(junior_women_winner[3]).center(20),
                                                    str(junior_women_winner[1]).center(20),str(junior_women_winner[10]).center(10)))    
    print ("-------------------------------------------------------------------------------------------------------------------------------------------------")
    
    #Imprimiendo Ganador Seniors por Sexo
    print("|{:15}|{:10}|{:15}|{:15}|{:10}|{:10}|{:15}|{:15}|{:10}|".format('Senior'.center(15), str(seniors_men_winner[0]).center(10), str(seniors_men_winner[3]).center(20),
                                                    str(seniors_men_winner[1]).center(20),str(seniors_men_winner[10]).center(10), 
                                                    str(seniors_women_winner[0]).center(10), str(seniors_women_winner[3]).center(20),
                                                    str(seniors_women_winner[1]).center(20),str(seniors_women_winner[10]).center(10)))    
    print ("-------------------------------------------------------------------------------------------------------------------------------------------------")

    #Imprimiendo Ganador Masters por Sexo
    print("|{:15}|{:10}|{:15}|{:15}|{:10}|{:10}|{:15}|{:15}|{:10}|".format('Master'.center(15), str(master_men_winner[0]).center(10), str(master_men_winner[3]).center(20),
                                                    str(master_men_winner[1]).center(20),str(master_men_winner[10]).center(10), 
                                                    str(masters_women_winner[0]).center(10), str(masters_women_winner[3]).center(20),
                                                    str(masters_women_winner[1]).center(20),str(masters_women_winner[10]).center(10)))    
    print ("-------------------------------------------------------------------------------------------------------------------------------------------------")


    wait = input("\nPresione una tecla para continuar")
    clear_screen()
    return dic