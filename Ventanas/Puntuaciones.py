import PySimpleGUI as sg
import json
import os.path

'''Este metodo deberia de agarrar los datos guardados y:
    -si es general hace el merge y crea una lista de maximo 10 elementos con str
    -si es facil crea una lista de maximo 10 elementos con los str de la dificultad facil
    -si es normal crea una lista de maximo 10 elementos con los str de la dificultad normal
    -si es dificil lo mismo pero en dificil ya se entendio'''

def exist():
    if(not os.path.isfile("Ventanas\puntaje.json")):
        with open("Ventanas\puntaje.json", "w") as rfile:
            dic = {"easy": [[10, "10/28/2020"]], "medium": [[113, "06/18/2020"]], "hard": [[218, "07+1/28/2020"],[2, "03/28/2020"]]}
            json.dump(dic,rfile)
    pass

def CargarDatos(): #carga los datos de puntaje.json en un diccionario
    #dic = {'easy': [[10], [9], [3], [1]], 'medium': [[5], [4]], 'hard': [[8], [7], [2]]}
    exist()
    with open("Ventanas\puntaje.json", "r") as rfile:
        dic = json.load(rfile)
    return dic

def merge(dic): #en caso de pedir el general, se ejecuta un merge de los puntajes de las 3 dificultades 
    me, mm, mh = 0, 0, 0
    l = []
    m = [dic['easy'][0]+['Easy'], dic['medium'][0]+['Medi'], dic['hard'][0]+['Hard']] #creo la lista para los primeros puntajes de las 3 listas del diccionario
    for i in range(10):  #merge top 10 dificultades
        maximo = max(m)  #saco el maximo de los 3 puntajes
        ''' tests
        #print('m',m)
        #print(maximo)
        '''

        if(maximo[0] == 0): #en caso de que el maximo sea 0, quiere decir que no hay otro puntaje
            l.append(str(str(i+1)+': '+'---------------     --------  --'))
            continue

        '''try/excepts son en caso de que no queden puntajes en alguna de las listas de dificultad
            y lo que harian estas seria, primero preguntar si el numero maximo esta sacado de alguna de estas 
            listas (utilizando un indice para avanzar sobre estas), en caso de ser asi, se incrementaria el indice 
            y se ejecutaria un append de el siguiente puntaje a la lista del merge
        '''
        try: 
            if(maximo[0] == dic['hard'][mh][0]):
                mh += 1
                m.append(dic['hard'][mh]+['Hard'])
        except IndexError:  # excepcion out of range => append 0
            m.append([0])

        try:
            if(maximo[0] == dic['medium'][mm][0]):
                mm += 1
                m.append(dic['medium'][mm]+['Medi'])
        except IndexError:  # excepcion out of range => append 0
            m.append([0])

        try:
            if(maximo[0] == dic['easy'][me][0]):
                me += 1
                m.append(dic['easy'][me]+['Easy'])
        except IndexError:  # excepcion out of range => append 0
            m.append([0])

        #print(i+1,': ',maximo) #<-test
        #se agrega a la lista el numero del puesto, seguido la fecha y la dificultar y seguido el puntaje 
        l.append(str(str(i+1)+': '+maximo[1]+'    '+maximo[2]+' -   '+str(maximo[0])))
        m.remove(maximo) #se elimina el numero maximo de la lista del merge
    return l


def CrearLista(filtro,dic): #se recibe la dificultad y el diccionario que posee los puntajes y devuelve la lista a mostrar
    listaStr = []
    for i in range(1, 11):
        algo=''
        try:                #try/except se ejecuta en caso de no existir mas puntajes por agregar a la lista
            algo = str(str(i)+': '+dic[filtro][i-1][1]+' -  '+str(dic[filtro][i-1][0]))
        except IndexError:  #en caso de no existir mas puntajes, se presentara lo siguiente
            algo = str(str(i)+": ----------------  -----")
        finally:            #tras agregarle todo al string "algo" se añade este a la lista
            listaStr.append(algo)
    return listaStr   #retorna la lista que se debe imprimir en pantalla


def crearVentanaPuntajes(dic): #crea la pantalla a mostrar en pantalla presentando por defecto la pestaña general/merge
    layoutP = [
        [sg.Listbox(values=(merge(dic)),
                    size=(70, 10), key="lista")],
        [sg.B("General", size=(11, 1)), sg.B("Facil", size=(11, 1)),
        sg.B("Normal", size=(11, 1)), sg.B("Dificil", size=(11, 1)),
        sg.Exit("Volver", size=(11, 1), key=('Exit'))]
    ]

    window = sg.Window("Tabla de puntuaciones", layoutP)

    return window


def listaPuntuacionesAltas(): #funcion principal del puntuaciones.py
    dic = CargarDatos()                #cargo el diccionario de puntajes
    sg.theme("DarkBrown")
    window = crearVentanaPuntajes(dic) #cargo la ventana general

    while True: 
        event, _ = window.read()       #muestro la ventana
        if event in (None, "Exit"):    #en caso de cerrar la ventana o presionar "volver" se cierra
            break
        if event == "General":         #se muestra el merge
            window.Element("lista").update(values=merge(dic))
        if event == "Facil":           #se muestra la lista de dificultad "facil"
            window.Element("lista").update(values=CrearLista("easy",dic))
        if event == "Normal":          #se muestra la lista de dificultad "medio"
            window.Element("lista").update(values=CrearLista("medium",dic))
        if event == "Dificil":         #se muestra la lista de dificultad "dificil"
            window.Element("lista").update(values=CrearLista("hard",dic))
    window.close()


if __name__ == "__main__": #main para testeos
    listaPuntuacionesAltas()
