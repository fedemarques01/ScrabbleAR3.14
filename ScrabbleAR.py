from pattern.text.es import parse, split, lexicon, spelling
from random import randint
from os import remove
import PySimpleGUI as sg
import os.path
import json
from Ventanas.Puntuaciones import listaPuntuacionesAltas as pt
from Ventanas.Configuracion import ajustes
import Tablero
from Funciones import Letras

sg.theme("Dark Amber")



"""Esta funcion se encarga de la creacion 
de la interfaz del menu en PySimpleGui y devuelve la ventana ya lista para utilizar"""
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
    #Si hay una partida guardada, el boton para continuarla aparecera en la ventana
    if(os.path.isfile("Guardado.json")):
        layoutM += [[sg.B("Continuar partida", size=(36, 1), key="continue")]]

    window = sg.Window("ScrabbleAR - Menu", layoutM)

    return window

def setDif(dificultad):
    if(dificultad=='Easy'):
        return ['NN', 'JJ', 'VB']
    elif(dificultad=='Medium'):
        return ['NN', 'VB']
    elif(dificultad=='Hard'):
        i=randint(0,2)
        dif=['NN', 'JJ', 'VB']
        return dif[i]

"""La funcion del menu, abre la ventana del menu principal desde donde el usuario puede elegir que desea hacer:
configurar cosas, ver las puntuaciones, jugar una nueva partida o continuar una( si existe el archivo)"""
def Menu():
    config={'dif':'Medium','puntosJ':0,'puntosIA':0,'time':10,'pal':[],'bolsa':Letras.Bolsa('Medium'),'letrasP': Letras.valoresLetras}
    menu = Crearmenu()
    while True:
        menu.un_hide()
        event, _ = menu.read()
        print(event)
        if event in ("inicio", "continue"):
            if(event == 'inicio' and os.path.isfile('Guardado.json')):
                #crea una ventana en un par de lineas de codigo para determinar si se quiere o no descartar la partida guardada
                event2, _ = sg.Window('ADVERTENCIA',
                [[sg.T('Si inicias una nueva partida se borrara la guardada, seguro que quieres continuar?')],
                [sg.B('OK'), sg.B('Cancel') ]]).read(close=True)
                if event2 == 'OK':
                    remove('Guardado.json')# borra la partida guardada
                else:
                    continue    
            menu.close()
            config['pal']=setDif(config['dif'])
            Tablero.Jugar(config,event)
        elif event == "puntos":
            menu.hide()
            pt()#muestra la lista de puntuaciones(ver Puntuaciones.py)
        elif event == "config":
            menu.hide()
            config = ajustes(config)#muestra los ajustes(ver Configuraciones.py)
        elif event in (None, "exit"):
            break


Menu() 
