from datetime import date as dt
import json

def CargarDatos():
    #{"easy": [[10, "10/28/2020"], [9, "09/28/2020"], [3, "03/28/2020"], [1, "01/28/2020"]], "medium": [[5, "05/28/2020"], [4, "04/28/2020"]], "hard": [[100, "05/28/2020"], [8, "07+1/28/2020"], [7, "07/28/2020"], [2, "02/28/2020"]]}
    dic={}
    with open("puntaje.json", "r") as rfile:
        dic = json.load(rfile)
    return dic

def Guardar(dific,puntos):
    date = dt.today().strftime("%m/%d/%Y")
    dic=CargarDatos()
    l=dic[dific]
    for i in range(len(l)):
        if(l[i][0]>puntos):
            continue
        l.insert(i, [puntos]+[date])
        break
    
    dic[dific]=l
    with open("puntaje.json", "w") as rfile:
        json.dump(dic,rfile)
    

if __name__ == "__main__":
    Guardar('medium',250)
    print('sacabo')
