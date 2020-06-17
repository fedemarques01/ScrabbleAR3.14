from pattern.text.es import parse, split, lexicon, spelling
from random import randint
import PySimpleGUI as sg
import os.path
import json
from Puntuaciones import listaPuntuacionesAltas as pt
from Configuracion import ajustes
import Tablero

sg.theme("Dark Amber")




def Crearmenu():
    layoutM = [
        [sg.T("ScrabbleAR", size=(16, 1), justification="center",
              font=("Times New Roman", 25))],
        [sg.T("       Bienvenido a ScrabbleAR!, el juego donde      ")],
        [sg.T("           hay que armar palabras para ganar         ")],
        [sg.B("Iniciar nuevo juego", size=(17, 1), key="inicio"),
         sg.B("Configuracion", size=(17, 1), key="config")],
        [sg.B("Puntuaciones", size=(17, 1), key="puntos"),
         sg.B("Salir", size=(17, 1), key="exit")]
    ]

    if(os.path.isfile("Guardado.json")):
        layoutM += [[sg.B("Continuar partida", size=(36, 1), key="continue")]]

    window = sg.Window("ScrabbleAR - Menu", layoutM)

    return window

def setDif(dificultad):
    if(dificultad=='easy'):
        return ['NN', 'JJ', 'VB']
    elif(dificultad=='medium'):
        return ['NN', 'VB']
    elif(dificultad=='hard'):
        i=randint(0,2)
        dif=['NN', 'JJ', 'VB']
        return dif[i]


def Menu():
    config={'dif':'medium','puntosJ':0,'puntosIA':0,'time':10,'pal':[],'bolsa':[]}
    menu = Crearmenu()
    while True:
        menu.un_hide()
        event, _ = menu.read()
        print(event)
        if event in ("inicio", "continue"):
            if(event == "continue"):
                print("")
            menu.close()
            config['pal']=setDif(config['dif'])
            Tablero.Jugar(config,event)
        elif event == "puntos":
            menu.hide()
            pt()
        elif event == "config":
            menu.hide()
            config = ajustes(config)
        elif event in (None, "exit"):
            break


Menu() 
