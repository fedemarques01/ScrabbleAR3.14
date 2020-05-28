import PySimpleGUI as sg
from datetime import datetime as datetime
sg.theme("Topanga")
def crearTablero():
    col = fil = 15 
    """
    tamaño del tablero, son constantes basically
    BackT es el tablero pero en back end, usado a la hora de ver el contenido de las casillas 
    y es actualizado cuando se verifica una palabra
    """

    fichas = 7 
    backT = [["" for i in range(col)] for i in range(fil)]

    colM = [
        [sg.B("Guardar",size=(13,1),key="-save-")],
        [sg.B("Terminar",size=(13,1),key="Exit")],
        [sg.Frame(layout=[[sg.Text("",size=(13,10),key="-comment-")]],
        title="Comentarios",title_color="Yellow",background_color="Black",key="-block-")],
        [sg.Text("Dificultad: ",key="-dif-")],
        [sg.Text("Tu puntaje: 0",key="-pJug-")],
        [sg.Text("Puntaje CPU: 0",key="-pCPU-")]
    ]

    colBoard = [[sg.Text("CPU:")]]

    colBoard += [[sg.B("?",size=(2,1),pad=(0,0),disabled=True) for i in range(fichas)]for j in range(1)]

    colBoard += [[sg.Text("")]]

    colBoard += [[sg.B("",size=(3,1), key =(m,n),pad=(0,0)) for m in range(col)] for n in range(fil)]

    colPlayer = [[sg.B("",size=(3,1),key = str(k) , pad=(0,0)) for k in range(fichas)]for l in range(1)] 

    frontT = [
        [sg.Column(colM),
        sg.Column(colBoard)],
    [sg.Text("")],
    [sg.Text("Tus fichas:"), sg.Column(colPlayer),
    sg.B("Comprobar",key="-fin-",size=(10,1)),sg.B("Pasar",key="-cambiar-",size=(10,1)),
    sg.B("Deshacer",key="-back-",size=(10,1))]
    ]

    tablero = sg.Window("ScrabbleAR - Juego",frontT)

    return tablero,backT

#def cargarTablero(tableroGuardado):

def Jugar():
    tablero,backT = crearTablero() 
    print("me mori")
    event, _ = tablero.read()

if __name__ == "__main__":
    Jugar()
