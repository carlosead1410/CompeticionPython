from Controller.functions import clear_screen


def total_participants(dic:dict)->dict:
    print("**********   CANTIDAD TOTAL DE PARTICIPANTES   **********\n")
    
    participants = dic["participants"]
    print(f"Cantidad Total de Participantes: {len(participants)}")
    
    wait = input("\nPresione una tecla para continuar")
    clear_screen()
    return dic

