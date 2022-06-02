from Controller.functions import clear_screen


def total_participants_sex(dic:dict)->dict:
    print("**********  CANTIDAD DE PARTICIPANTES POR SEXO   **********\n")
    mens = dic["mens"] 
    womens = dic["womens"] 
    print(f"Cantidad De Participantes por Sexo: Masculino: {len(mens)} | Femenino: {len(womens)}")
        
    wait = input("\nPresione una tecla para continuar")
    clear_screen()
    return dic