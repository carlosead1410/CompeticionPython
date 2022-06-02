import os
import sys
from datetime import date, time, datetime

from Exceptions.exceptions import IncorrectData

def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    # else screen will be cleared for windows
    else:
        os.system('cls')
      
   
        
# METODO PARA SEPARAR PARTICIPANTES (ORDENAR DATA)
def sort_data(dic:dict)->dict:
    data = dic["data"]
    participants = []
    #Primero voy a separar cada registro en una lista
    for i in range(len(data)):
        participant = data[i].replace("'", "").replace("\n","").replace(" ","")

        list_participants = participant.split(",")
        participants.append(list_participants) 
        
    dic["participants"] = participants
    if verify_data(dic) == False:
        raise IncorrectData("Los datos de los participantes estan incompletos")
    
    dic = add_total_time(dic)
    dic = order_list(dic)
    dic = split_participants_etarios(dic)
    dic = split_participants_sex(dic)
    
    dic = split_juniors_sex(dic)
    dic = split_seniors_mens(dic)
    dic = split_masters_mens(dic)
    
    dic = average_juniors_time(dic)
    dic = average_seniors_time(dic)
    dic = average_masters_time(dic)
    
    return dic

#METODO PARA SEPARAR LOS PARTICIPANTES POR GRUPO ETARIOS
def split_participants_etarios(dic:dict)->dict:
    juniors = []
    seniors = []
    masters = []
    
    participants = dic["participants"]
    for i in participants:
        edad = int(i[6])
        if edad <= 25:
            juniors.append(i)
        if edad > 25 and edad <= 40:
            seniors.append(i)
        if edad > 40:
            masters.append(i)
            
    dic["juniors"] = juniors
    dic["seniors"] = seniors
    dic["masters"] = masters
    
    return dic



#METODO PARA SEPARAR LOS PARTICIPANTES POR GRUPO SEXO
def split_participants_sex(dic:dict)->dict:
    mens = []
    womens = []
    participants = dic["participants"]
    for i in participants:
        sex = str(i[5])
        if sex.upper() == 'M' or sex.upper() == "M" :
            mens.append(i)
        if sex.upper() == 'F' or sex.upper() == "F":
            womens.append(i) 
    
    dic["mens"] = mens
    dic["womens"] = womens
    
    return dic

#METODO PARA AGREGAR EL TIEMPO TOTAL DE LOS PARTICIPANTES
def add_total_time(dic:dict)->dict:
    new_participants = []
    participants = dic["participants"]
    for i in participants:
        tiempo = time(int(i[7]),int(i[8]),int(i[9]))
        i.append(tiempo)
        new_participants.append(i)
        
    dic["participants"] = new_participants
    return dic


#ORDENAR LISTA DE MENOR TIEMPO AL MAYOR TIEMPO
def order_list(dic:dict)->dict:
    participants = dic["participants"]
    participants.sort(key=lambda participant: participant[10])
    dic["participants"] = participants
    return dic


#Obtener los hombres y mujeres de los juniors (separarlos por sexo)
def split_juniors_sex(dic:dict)-> dict:
    juniors = dic["juniors"] 
    juniors_mens = []
    juniors_womens = []
    
    for i in juniors:
        sex = str(i[5])
        if sex.upper() == 'M' or sex.upper() == "M" :
            juniors_mens.append(i)
        if sex.upper() == 'F' or sex.upper() == "F":
            juniors_womens.append(i) 
            
    dic["juniors_mens"] = juniors_mens
    dic["juniors_womens"] = juniors_womens
    return dic
    
    
#Obtener los hombres y mujeres de los seniors (separarlos por sexo)
def split_seniors_mens(dic:dict)-> dict:
    seniors = dic["seniors"] 
    seniors_mens = []
    seniors_womens = []
    
    for i in seniors:
        sex = str(i[5])
        if sex.upper() == 'M' or sex.upper() == "M" :
            seniors_mens.append(i)
        if sex.upper() == 'F' or sex.upper() == "F":
            seniors_womens.append(i) 
    
    dic["seniors_mens"] = seniors_mens
    dic["seniors_womens"] = seniors_womens
    return dic


#Obtener los hombres y mujeres de los masters (separarlos por sexo)
def split_masters_mens(dic:dict)-> dict:
    masters = dic["masters"]  
    masters_mens = []
    masters_womens = []
    
    for i in masters:
        sex = str(i[5])
        if sex.upper() == 'M' or sex.upper() == "M" :
            masters_mens.append(i)
        if sex.upper() == 'F' or sex.upper() == "F":
            masters_womens.append(i) 
    
    dic["masters_mens"] = masters_mens
    dic["masters_womens"] = masters_womens
    return dic



#Tiempo promedio de juniors
def average_juniors_time(dic:dict)->dict:
    
    juniors_mens = dic["juniors_mens"] 
    juniors_womens = dic["juniors_womens"] 
    hours = 0
    minutes = 0
    seconds = 0
    total_seconds = 0
    
    # Primero se calcula el tiempo promedio de los juniors hombres (transformando todo a segundos)
    for i in juniors_mens:
        total_seconds =  total_seconds + int(i[7])*3600 +  int(i[8])*60 +  int(i[9])
    
    average_seconds = total_seconds / len(juniors_mens)
    minutes, seconds = divmod(average_seconds,60)
    hours, minutes = divmod(minutes,60)
    average_time_junior_mens = time(round(hours),round(minutes),round(seconds))
    dic["average_time_junior_mens"] = average_time_junior_mens
    
    hours = 0
    minutes = 0
    seconds = 0
    total_seconds = 0
    
    # Segundo se calcula el tiempo promedio de los juniors mujeres (transformando todo a segundos)
    for i in juniors_womens:
        total_seconds =  total_seconds + int(i[7])*3600 +  int(i[8])*60 +  int(i[9])
    
    average_seconds = total_seconds / len(juniors_womens)
    minutes, seconds = divmod(average_seconds,60)
    hours, minutes = divmod(minutes,60)
    average_time_junior_womens = time(round(hours),round(minutes),round(seconds))
    dic["average_time_junior_womens"] = average_time_junior_womens
    
    
    return dic

# #Tiempo promedio de seniors
def average_seniors_time(dic:dict)->dict:
    
    seniors_mens = dic["seniors_mens"] 
    seniors_womens = dic["seniors_womens"]
    hours = 0
    minutes = 0
    seconds = 0
    total_seconds = 0
    
    # Primero se calcula el tiempo promedio de los senior hombres (transformando todo a segundos)
    for i in seniors_mens:
        total_seconds =  total_seconds + int(i[7])*3600 +  int(i[8])*60 +  int(i[9])
    
    average_seconds = total_seconds / len(seniors_mens)
    minutes, seconds = divmod(average_seconds,60)
    hours, minutes = divmod(minutes,60)
    average_time_senior_mens = time(round(hours),round(minutes),round(seconds))
    dic["average_time_senior_mens"] = average_time_senior_mens
    
    hours = 0
    minutes = 0
    seconds = 0
    total_seconds = 0
    
    # Segundo se calcula el tiempo promedio de los senior mujeres (transformando todo a segundos)
    for i in seniors_womens:
        total_seconds =  total_seconds + int(i[7])*3600 +  int(i[8])*60 +  int(i[9])
    
    average_seconds = total_seconds / len(seniors_womens)
    minutes, seconds = divmod(average_seconds,60)
    hours, minutes = divmod(minutes,60)
    average_time_senior_womens = time(round(hours),round(minutes),round(seconds))
    dic["average_time_senior_womens"] = average_time_senior_womens
    
    return dic


# #Tiempo promedio de masters
def average_masters_time(dic:dict)->dict:
    
    masters_mens = dic["masters_mens"]
    masters_womens = dic["masters_womens"]
    hours = 0
    minutes = 0
    seconds = 0
    total_seconds = 0
    
    # Primero se calcula el tiempo promedio de los senior hombres (transformando todo a segundos)
    for i in masters_mens:
        total_seconds =  total_seconds + int(i[7])*3600 +  int(i[8])*60 +  int(i[9])
    
    average_seconds = total_seconds / len(masters_mens)
    minutes, seconds = divmod(average_seconds,60)
    hours, minutes = divmod(minutes,60)
    average_time_master_mens = time(round(hours),round(minutes),round(seconds))
    dic["average_time_master_mens"] = average_time_master_mens
    
    hours = 0
    minutes = 0
    seconds = 0
    total_seconds = 0
    
    # Segundo se calcula el tiempo promedio de los senior mujeres (transformando todo a segundos)
    for i in masters_womens:
        total_seconds =  total_seconds + int(i[7])*3600 +  int(i[8])*60 +  int(i[9])
    
    average_seconds = total_seconds / len(masters_womens)
    minutes, seconds = divmod(average_seconds,60)
    hours, minutes = divmod(minutes,60)
    average_time_master_womens = time(round(hours),round(minutes),round(seconds))
    dic["average_time_master_womens"] = average_time_master_womens
    
    return dic


#Verificar si los datos estan completos
def verify_data(dic:dict)->bool:
    participants = dic["participants"]
    count = 0
    for i in participants:
        if len(participants) != 10:
            return False
    
    return True

