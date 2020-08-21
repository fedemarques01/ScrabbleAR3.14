from datetime import date as dt
import json
from Ventanas.Puntuaciones import exist

def CargarDatos(): #guarda el diccionario que posee puntaje.json
    #{"easy": [[10, "10/28/2020"], [9, "09/28/2020"], [3, "03/28/2020"], [1, "01/28/2020"]], "medium": [[5, "05/28/2020"], [4, "04/28/2020"]], "hard": [[100, "05/28/2020"], [8, "07+1/28/2020"], [7, "07/28/2020"], [2, "02/28/2020"]]}
    dic={}
    exist()
    with open("Ventanas\puntaje.json", "r") as rfile:
        dic = json.load(rfile)
    return dic

def Guardar(dific,puntos): #guarda el nuevo dato en el diccionario de puntajes
    date = dt.today().strftime("%m/%d/%Y") #guarda la fecha
    dic=CargarDatos()                      #carga el diccionario
    l=dic[dific]                           #guarda la lista de puntajes de la dificultad recibida por parametro
    for i in range(len(l)):              #inserta ordenadamente el nuevo puntaje a la lista
        if(l[i][0]>puntos):
            continue
        l.insert(i, [puntos]+[date])
        break
    
    dic[dific]=l                           #cambia el valor de la lista de esa dificultad a la nueva lista
    with open("Ventanas\puntaje.json", "w") as rfile: #guarda el diccionario
        json.dump(dic,rfile)
    

if __name__ == "__main__": #main para testeos
    Guardar('medium',250)
    print('sacabo')
