
import PySimpleGUI as sg
sg.theme("Dark Amber")

def Crearmenu():
    layoutM = [
        [sg.T("ScrabbleAR",size=(16,1), justification="center",font=("Times New Roman", 25))],
        [sg.T("       Bienvenido a ScrabbleAR!, el juego donde      ")],
        [sg.T("           hay que armar palabras para ganar         ")],
        [sg.B("Iniciar nuevo juego",size=(17,1), key="inicio"),
        sg.B("Configuracion",size=(17,1), key="config")],
        [sg.B("Puntuaciones",size=(17,1), key="puntos"),
        sg.B("Salir",size=(17,1), key="exit")],
        [sg.B("Continuar partida",size=(36,1), key="continue")]]

    window = sg.Window("ScrabbleAR - Menu", layoutM, finalize=True)
    try:
        arch = open("Guardado.json", "r")
    except Exception as e:
        window["continue"].update(visible=False)


    return window


def Menu():
    menu = Crearmenu()
    while True:
        event, value = menu.read()

        if event == "Iniciar nuevo Juego" or "Continuar partida":
            if(event == "Continuar partida"):
                print("")
                #cargar ajustes por default
            menu.close()
            # IniciarJuego?
        if event == "Puntuaciones":
            print("")
            # AbroListaPuntuaciones
        if event == "Configuracion":
            print("")
            #event,ajustes = crear_ventana_config().read()
        else:
            break
    menu.close()

Menu()