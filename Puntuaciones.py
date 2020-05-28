import PySimpleGUI as sg
import json

"""Este metodo deberia de agarrar los datos guardados y:
    -si es general hace el merge y crea una lista de maximo 10 elementos con str
    -si es facil crea una lista de maximo 10 elementos con los str de la dificultad facil
    -si es normal crea una lista de maximo 10 elementos con los str de la dificultad normal
    -si es dificil lo mismo pero en dificil ya se entendio"""
def CargarDatos():
    #dic = {'eas': [[10], [9], [3], [1]], 'mid': [[5], [4]], 'har': [[8], [7], [2]]}
    dic={}
    with open("puntaje.json", "r") as rfile:
        dic = json.load(rfile)
    return dic

def merge(dic):
    me, mm, mh = 0, 0, 0
    l = []
    m = [dic['eas'][0]+['Easy'], dic['mid'][0]+['Medi'], dic['har'][0]+['Hard']]
    for i in range(10):
        maximo = max(m)
        #print('m',m)
        #print(maximo)
        try:
            if(maximo[0] == 0):
                #print(i+1,': ---')
                l.append(str(str(i+1)+': '+'-'))
                continue
            
            elif(maximo[0] == dic['har'][mh][0]):
                mh += 1
                m.append(dic['har'][mh]+['Hard'])

            elif(maximo[0] == dic['mid'][mm][0]):
                mm += 1
                m.append(dic['mid'][mm]+['Medi'])

            elif(maximo[0] == dic['eas'][me][0]):
                me += 1
                m.append(dic['eas'][me]+['Easy'])

        except IndexError:  # excepcion out of range => append 0
            m.append([0])
            #print(i,': ',maximo)
        l.append(str(str(i+1)+': '+str(maximo[0])+' '+maximo[1]+' '+maximo[2]))
        m.remove(maximo)
    return l


def CrearLista(filtro,dic):
    listaStr = []
    for i in range(1, 11):
        try:
            algo = str(str(i)+': '+str(dic[filtro][i-1][0])+' '+dic[filtro][i-1][1])
        except IndexError:
            algo = str(str(i)+": -----")
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
            window.Element("lista").update(values=CrearLista("eas",dic))
        if event == "Normal":
            window.Element("lista").update(values=CrearLista("mid",dic))
        if event == "Dificil":
            window.Element("lista").update(values=CrearLista("har",dic))
    window.close()


if __name__ == "__main__":
    listaPuntuacionesAltas()
