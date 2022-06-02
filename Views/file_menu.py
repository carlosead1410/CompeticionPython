
import sys
from Controller.functions import clear_screen
from GetData.load_file import load_file

# ESTE ES EL MENU DE LAS OPCIONES DE ARCHIVO
def menu_file(dic:dict)->dict:
    option = 0
    while(True):
        try:
            print("**********   MENU ARCHIVOS   **********")
            print("1. Cargar Archivos ")
            print("2. Regresar al Menu Principal ")            
            print("3. Salir del Sistema")
            option = int(input("\nSeleccione una opcion: "));
            
            if(option == 1 ):
                clear_screen()
                dic = load_file(dic)
                
            if(option == 2):
                clear_screen()
                break
            
            if(option == 3):
                clear_screen()
                sys.exit()
                break
            
            if(option < 1 or option > 3):
                print("\nIngrese una opcion entre el 1 y el 3\n")
                wait = input("Presione una tecla para continuar")
                clear_screen()
            
        except ValueError:
            print("\nERROR --> Usted debe ingresar un numero como opcion\n")
            wait = input("Presione una tecla para continuar")
            clear_screen()
            
    return dic