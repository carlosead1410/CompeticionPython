from Controller import clear_screen
from Views.action_menu import menu_actions
from Views.file_menu import menu_file

# ESTE ES EL MENU PRINCIPAL
def Menu():
    option = 0
    dic = None
    while(True):
        try:
            print("**********   BIENVENIDO AL SISTEMA DE COMPETENCIA   **********")
            print("1. Archivos ")
            print("2. Acciones ")
            # print("3. Salir ")
            option = int(input("\nSeleccione una opcion: "));
            
            if(option == 1 ):
                clear_screen()                
                dic = menu_file(dic)
                
            if(option == 2 ):
                clear_screen()                
                dic = menu_actions(dic)
            
            if(option < 1 or option > 2):
                print("\nIngrese una opcion entre el 1 y el 2\n")
                wait = input("Presione una tecla para continuar")
                clear_screen()

        except ValueError:
            print("\nERROR --> Usted debe ingresar un numero como opcion\n")
            wait = input("Presione una tecla para continuar")
            clear_screen()