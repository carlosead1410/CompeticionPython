from Controller import clear_screen
from Views.average_time import average_time
from Views.general_winner import general_winner
from Views.histogram import histogram
from Views.total_list_participants import total_list_partcipants
from Views.total_participants import total_participants
from Views.total_participants_etarios import total_participants_etarios
from Views.total_participants_sex import total_participants_sex
from Views.winners_etarios_sex import winners_etarios_sex
from Views.winners_group_etarios import winners_group_etarios
from Views.winners_group_sex import winners_group_sex

# ESTE ES EL MENU DE LAS OPCIONES DE ACCIONES
def menu_actions(dic:dict)-> dict:
    option = 0
    if(dic):
        while(True):
            try:
                print("**********   MENU ACCIONES   **********")
                print("1. Lista con Totalidad de Participantes ")
                print("2. Cantidad Total de Participantes ")
                print("3. Cantidad de Participantes por Grupo Etario")
                print("4. Cantidad de Participantes por Sexo")
                print("5. Ganadores por Grupo Etario")
                print("6. Ganadores por Sexo")
                print("7. Ganadores por Grupo Etario y Sexo")
                print("8. Ganador General")
                print("9. Histrograma de participantes por Grupo Etario")
                print("10. Promedio de Tiempo por Grupo Etario y Sexo")            
                print("11. Regresar ")
                option = int(input("\nSeleccione una opcion: "));
                
                
                if(option == 1):
                    clear_screen()
                    dic = total_list_partcipants(dic)
                
                if(option == 2):
                    clear_screen()
                    dic = total_participants(dic)
                
                if(option == 3):
                    clear_screen()
                    dic = total_participants_etarios(dic)
                
                if(option == 4):
                    clear_screen()
                    dic = total_participants_sex(dic)
                
                if(option == 5):
                    clear_screen()
                    dic = winners_group_etarios(dic)
                
                if(option == 6):
                    clear_screen()
                    dic = winners_group_sex(dic)
                
                if(option == 7):
                    clear_screen()
                    dic = winners_etarios_sex(dic)
                    
                if(option == 8):
                    clear_screen()
                    dic = general_winner(dic)
                
                
                if(option == 9):
                    clear_screen()
                    dic = histogram(dic)
                
                if(option == 10):
                    clear_screen()
                    dic = average_time(dic)
                    
                
                if(option == 11):
                    clear_screen()
                    break
                
                if(option < 1 or option > 11):
                    print("\nIngrese una opcion entre el 1 y el 9\n")
                    wait = input("Presione una tecla para continuar")
                    clear_screen()
                
            except ValueError:
                print("\nERROR --> Usted debe ingresar un numero como opcion\n")
                wait = input("Presione una tecla para continuar")
                clear_screen()
    else:
        print("ERROR --> Usted debe cargar un archivo antes de entrar al menu de acciones")
        wait = input("Presione una tecla para continuar")
        clear_screen()
   
    return dic