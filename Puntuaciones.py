import PySimpleGUI as sg


"""Este metodo deberia de agarrar los datos guardados y:
    -si es general hace el merge y crea una lista de maximo 10 elementos con str
    -si es facil crea una lista de maximo 10 elementos con los str de la dificultad facil
    -si es normal crea una lista de maximo 10 elementos con los str de la dificultad normal
    -si es dificil lo mismo pero en dificil ya se entendio"""


def CrearLista(filtro):
    listaStr = []

    for i in range(0, 10):
        algo = i
        listaStr.append(algo)

    return listaStr


def crearVentanaPuntajes():

    layoutP = [
        [sg.Listbox(values=(CrearLista("General")),
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
            window.Element("lista").update(values=CrearLista("General"))
        if event == "Facil":
            window.Element("lista").update(values=CrearLista("Facil"))
        if event == "Normal":
            window.Element("lista").update(values=CrearLista("Normal"))
        if event == "Dificil":
            window.Element("lista").update(values=CrearLista("Dificil"))
    window.close()


listaPuntuacionesAltas()
