import PySimpleGUI as sg


"""Este metodo deberia de agarrar los datos guardados y:
    -si es general hace el merge y crea una lista de maximo 10 elementos con str
    -si es facil crea una lista de maximo 10 elementos con los str de la dificultad facil
    -si es normal crea una lista de maximo 10 elementos con los str de la dificultad normal
    -si es dificil lo mismo pero en dificil ya se entendio"""

def merge():
    me, mm, mh = 0, 0, 0
    l = []
    dic={'eas':[[10], [9], [3], [0]], 'mid':[[5], [4]], 'har':[[8], [7], [2]]}
    #dic=cargarDatos()<------------load dic   
    m = [dic['eas'][0], dic['mid'][0], dic['har'][0]]
    for i in range(10):
        maximo = max(m)
        try:
            if(maximo[0] == 0):
                #print(i+1,': ---')
                l.append(str(str(i+1)+': '+'-'))
                continue
            elif(maximo == dic['eas'][me]):
                me += 1
                m.append(dic['eas'][me])

            elif(maximo == dic['mid'][mm]):
                mm += 1
                m.append(dic['mid'][mm])

            elif(maximo == dic['har'][mh]):
                mh += 1
                m.append(dic['har'][mh])

        except IndexError:  # excepcion out of range => append 0
            m.append([0])
        #print(i,': ',maximo)
        l.append(str(str(i+1)+': '+str(maximo[0])))
        m.remove(maximo)
    return l

def CrearLista(filtro):
    listaStr = []

    for i in range(1, 11):
        algo = i
        listaStr.append(algo)

    return listaStr


def crearVentanaPuntajes():

    layoutP = [
        [sg.Listbox(values=(merge()),
                    size=(70, 10), key="lista")],
        [sg.B("General", size=(11, 1)), sg.B("Facil", size=(11, 1)),
         sg.B("Normal", size=(11, 1)), sg.B("Dificil", size=(11, 1)),
         sg.B("Salir", size=(11, 1))]
    ]

    window = sg.Window("Tabla de puntuaciones", layoutP, keep_on_top=True)

    return window


def listaPuntuacionesAltas():
    # CargarDatos()
    sg.theme("DarkBrown")
    window = crearVentanaPuntajes()

    while True:
        event, values = window.read()
        if event in (None, "Exit") or event == "Salir":
            break
        if event == "General":
            window.Element("lista").update(values=merge())
        if event == "Facil":
            window.Element("lista").update(values=CrearLista("Facil"))
        if event == "Normal":
            window.Element("lista").update(values=CrearLista("Normal"))
        if event == "Dificil":
            window.Element("lista").update(values=CrearLista("Dificil"))
    window.close()


listaPuntuacionesAltas()
