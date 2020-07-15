import PySimpleGUI as sg
import json

"""Este metodo deberia de agarrar los datos guardados y:
    -si es general hace el merge y crea una lista de maximo 10 elementos con str
    -si es facil crea una lista de maximo 10 elementos con los str de la dificultad facil
    -si es normal crea una lista de maximo 10 elementos con los str de la dificultad normal
    -si es dificil lo mismo pero en dificil ya se entendio"""
def CargarDatos():
    #dic = {'easy': [[10], [9], [3], [1]], 'medium': [[5], [4]], 'hard': [[8], [7], [2]]}
    dic={}
    with open("Ventanas\puntaje.json", "r") as rfile:
        dic = json.load(rfile)
    return dic

def merge(dic):
    me, mm, mh = 0, 0, 0
    l = []
    m = [dic['Easy'][0]+['Easy'], dic['Medium'][0]+['Medi'], dic['Hard'][0]+['Hard']]
    for i in range(10):
        maximo = max(m)
        #print('m',m)
        #print(maximo)
        
        if(maximo[0] == 0):
            #print(i+1,': ---')
            l.append(str(str(i+1)+': '+'---------------     --------  --'))
            continue

        try:
            if(maximo[0] == dic['Hard'][mh][0]):
                mh += 1
                m.append(dic['Hard'][mh]+['Hard'])
        except IndexError:  # excepcion out of range => append 0
            m.append([0])

        try:
            if(maximo[0] == dic['Medium'][mm][0]):
                mm += 1
                m.append(dic['Medium'][mm]+['Medi'])
        except IndexError:  # excepcion out of range => append 0
            m.append([0])

        try:
            if(maximo[0] == dic['Easy'][me][0]):
                me += 1
                m.append(dic['Easy'][me]+['Easy'])
        except IndexError:  # excepcion out of range => append 0
            m.append([0])

        #print(i+1,': ',maximo)
        l.append(str(str(i+1)+': '+maximo[1]+'    '+maximo[2]+' -   '+str(maximo[0])))
        m.remove(maximo)
    return l


def CrearLista(filtro,dic):
    listaStr = []
    for i in range(1, 11):
        try:
            algo = str(str(i)+': '+dic[filtro][i-1][1]+' -  '+str(dic[filtro][i-1][0]))
        except IndexError:
            algo = str(str(i)+": ----------------  -----")
        finally:
            listaStr.append(algo)
    return listaStr


def crearVentanaPuntajes(dic):

    layoutP = [
        [sg.Listbox(values=(merge(dic)),
                    size=(70, 10), key="lista")],
        [sg.B("General", size=(11, 1)), sg.B("Facil", size=(11, 1)),
         sg.B("Normal", size=(11, 1)), sg.B("Dificil", size=(11, 1)),
         sg.Exit("Volver", size=(11, 1), key=('Exit'))]
    ]

    window = sg.Window("Tabla de puntuaciones", layoutP)

    return window


def listaPuntuacionesAltas():
    dic = CargarDatos()
    sg.theme("DarkBrown")
    window = crearVentanaPuntajes(dic)

    while True:
        event, _ = window.read()
        if event in (None, "Exit"):
            break
        if event == "General":
            window.Element("lista").update(values=merge(dic))
        if event == "Facil":
            window.Element("lista").update(values=CrearLista("Easy",dic))
        if event == "Normal":
            window.Element("lista").update(values=CrearLista("Medium",dic))
        if event == "Dificil":
            window.Element("lista").update(values=CrearLista("Hard",dic))
    window.close()


if __name__ == "__main__":
    listaPuntuacionesAltas()
