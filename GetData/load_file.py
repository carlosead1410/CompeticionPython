from Controller.functions import clear_screen, sort_data
from Exceptions.exceptions import IncorrectData, InvalidTextFile, is_text_plain_file

def load_file(dic:dict)->dict:
    data = None
    try:
            
        file_name = input("Ingrese el nombre del archivo: ")
        f = open(file_name,"rt")
        if not is_text_plain_file(file_name):
            raise InvalidTextFile("El archivo debe ser de Texto!")
        
        data = f.readlines()
        f.close()

        dic = {"data": data}

        dic = sort_data(dic)
        
        
        
    except FileNotFoundError:
        print("\nError --> Archivo no encontrado\n")
        wait = input("Presione una tecla para continuar")
        clear_screen()
        dic = None
        
        
    except PermissionError:
        print("\nError --> No cuenta con permisos para leer el archivo\n")
        wait = input("Presione una tecla para continuar")
        clear_screen()
        dic = None
        
    
    except InvalidTextFile as e:
        print("\nError: ", e)
        wait = input("Presione una tecla para continuar")
        clear_screen()
        dic = None
        
        
    except IncorrectData as e:
        print("\nError: ", e)
        wait = input("Presione una tecla para continuar")
        clear_screen()
        dic = None
        
    except:
        print("\nError no esperado mientras se lee el archivo\n")
        wait = input("Presione una tecla para continuar")
        clear_screen()
        dic = None
        
        
    else:
        print("\nArchivo Leido Exitosamente!!!\n")
        wait = input("Presione una tecla para continuar")
        clear_screen()
        
    return dic