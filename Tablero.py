import PySimpleGUI as sg
from datetime import datetime as datetime
import json
from validez import validez
import Letras
from guardarPuntos import Guardar as Gp

sg.theme("Topanga")

def Terminar(letras,dif,puntos): #resta los puntos y llama a guardar.py
                                                                       #FALTA actualizar los atriles de la cpu
    resta=0
    for i in letras:
        resta+=Letras.valoresLetras[letras[i]]
    puntos-=resta
    Gp(dif,puntos)
    pass

def crearTablero():
    col = fil = 15
    """
    col,fil y fichas son constantes que se usan a la hora de definir las proporciones del tablero y las fiachas por estante de jugador
    BackT es el tablero pero en back end, usado a la hora de ver el contenido de las casillas 
    y es actualizado cuando se verifica una palabra
    """

    fichas = 7
    backT = [["" for i in range(col)] for i in range(fil)]
    # ColM es la columna donde se encuentra la informacion de la partida junto a otros comentarios y los botones para terminar y guardar la partida
    colM = [
        [sg.B("Guardar", size=(13, 1), key="-save-")],
        [sg.B("Terminar", size=(13, 1), key="Exit")],
        [sg.Frame(layout=[[sg.Text("Ponga una ficha en ST para comenzar la partida", size=(13, 10), key="-comment-")]],
                  title="Comentarios", title_color="Yellow", background_color="Black", key="-block-")],
        [sg.Text(text="Dificultad: ",size=(13,3) ,key="-dif-")],
        [sg.Text(text="Tu puntaje: 0",size=(13,3) ,key="-pJug-")],
        [sg.Text(text="Puntaje CPU: 0",size=(13,3) ,key="-pCPU-")]
    ]

    # col board es la columna donde esta el atril del cpu y el tablero, generados de esta forma para que quede una columna al lado de la otra
    colBoard = [[sg.Text("CPU:")]]

    colBoard += [[sg.B("?",key=('-'+str(i)), size=(2, 1), pad=(0, 0), disabled=True)
                  for i in range(fichas)]]

    colBoard += [[sg.Text("")]]

    colBoard += [[sg.B("", size=(3, 1), key=(m, n), pad=(0, 0))
                  for m in range(col)] for n in range(fil)]

    # ColPlayer es la columna donde estan las fichas del jugador
    colPlayer = [[sg.B("", size=(3, 1), key=str(k), pad=(0, 0))
                  for k in range(fichas)]for l in range(1)]

    # layout del tablero, junta todas las columnas y añade el resto de los botones
    frontT = [
        [sg.Column(colM),
         sg.Column(colBoard)],
        [sg.Text("")],
        [sg.Text("Tus fichas:"), sg.Column(colPlayer),
         sg.B("Comprobar", key="-fin-", size=(10, 1)
              ), sg.B("Pasar", key="-cambiar-", size=(10, 1)),
         sg.B("Deshacer", key="-back-", size=(10, 1))]
    ]

    tablero = sg.Window("ScrabbleAR - Juego", frontT, finalize=True)

    return tablero, backT
# carga todos los botones del tablero, el ya guardado en caso de una partida guardada


def cargarTablero(tablero, board, datos):
    # si es None, no hay partida guardada entonces carga la lista de tuplas por cada casilla especial
    tabla = datos['tablero']
    tablero['-pJug-'].Update(('Tu puntaje: '+ str(datos['puntosJ'])).format())
    tablero['-pCPU-'].Update(('Puntaje CPU: '+ str(datos['puntosIA'])).format())
    tablero['-dif-'].Update(('Dificultad: '+ datos['dif']).format())
    if(tabla == None):

        triple_letter = [(1, 5), (1, 9), (5, 1), (5, 5), (5, 9),
                         (5, 13), (9, 1), (9, 5), (9, 9), (9, 13), (13, 5), (13, 9)]
        double_letter = [(0, 3), (0, 11), (2, 6), (2, 8), (3, 0), (3, 7), (3, 14), (6, 2), (6, 6), (6, 8), (6, 12), (
            7, 3), (7, 11), (8, 2), (8, 6), (8, 8), (8, 12), (11, 0), (11, 7), (11, 14), (12, 6), (12, 9), (14, 3), (14, 11)]
        double_word = [(1, 1), (2, 2), (3, 3), (4, 4), (1, 13), (2, 12), (3, 11), (4, 10),
                       (13, 1), (12, 2), (11, 3), (10, 4), (10, 10), (11, 11), (12, 12), (13, 13)]
        triple_word = [(0, 0), (0, 7), (0, 14), (7, 0),
                       (7, 14), (14, 0), (14, 7), (14, 14)]
        start_button = (7, 7)

        for x in triple_letter:
            tablero[x].Update(
                "Lx3", button_color=("#D4D4D4", "#8A1111"))
            board[x[0]][x[1]] = "Lx3"
        for x in double_letter:
            tablero[x].Update(
                "Lx2", button_color=("#D4D4D4", "#79118A"))
            board[x[0]][x[1]] = "Lx2"
        for x in double_word:
            tablero[x].Update(
                "Px2", button_color=("#D4D4D4", "#8A1155"))
            board[x[0]][x[1]] = "Px2"
        for x in triple_word:
            tablero[x].Update(
                "Px3", button_color=("#D4D4D4", "#0F6F6C"))
            board[x[0]][x[1]] = "Px3"
        tablero[start_button].Update(
            "St", button_color=("#D4D4D4", "#928900"))
    
    # caso contrario, recorre el tablero guardado y actualiza en base a eso
    else:
        
        board = tabla
        for i in range(len(tabla)):
            for j in range(len(tabla[i])):
                if(tabla[i][j] == ""):
                    continue
                elif(tabla[i][j] == "Lx3"):
                    tablero[(i, j)].Update(
                        "Lx3", button_color=("#D4D4D4", "#8A1111"))
                elif(tabla[i][j] == "Lx2"):
                    tablero[(i, j)].Update(
                        "Lx2", button_color=("#D4D4D4", "#79118A"))
                elif(tabla[i][j] == "Px2"):
                    tablero[(i, j)].Update(
                        "Px2", button_color=("#D4D4D4", "#8A1155"))
                elif(tabla[i][j] == "Px3"):
                    tablero[(i, j)].Update(
                        "Lx2", button_color=("#D4D4D4", "#0F6F6C"))
                else:
                    tablero[(i, j)].Update(tabla[i][j], button_color=(
                        "#FCC300", "#CD3500"))  # color y valor de la letra que ya estaba
    

    return tablero, board                

#FCC300
def puntos(dif,coor,letras,board):
    if not validez(dif,coor,letras):
        return 0

    pt,pp=0,1
    for i in range(len(coor)):
        pl=Letras.valoresLetras[letras[i]]
        bonus=board[coor[i][0]][coor[i][1]]
        if bonus!= "":
            if bonus== "Lx2":
                pl*=2
            elif bonus == "Lx3":
                pl*=3
            elif bonus == "Px2":
                pp*=2
            elif bonus == "Px3":
                pp*=3
        pt+=pl
    return pt*pp

# carga todos los ajustes de la partida(puntaje,dificultad,botones especiales,bolsa)

def Jugar(settings, event):
    sg.theme("Topanga")
    tablero, backT = crearTablero()
    # creo un diccionario con los datos de la partida instanciando un tablero vacio por defecto
    datos = {"tablero": None}
    print("me mori")
    if(event == "continue"):
        arch = open("Guardado.json", "r")
        # si existe una partida guardada datos tendra el backT de la partida anterior en tablero, y los settings de la partida anterior
        datos.update(json.load(arch))
    else:
        # sino datos tendra los settings que elijio el jugador o los por defecto
        datos.update(settings)

    tablero, backT = cargarTablero(tablero, backT, datos)
    while True:
        event, _ = tablero.read()
        print(event)
        if event in (None,'Exit'):
            break
    tablero.close()


if __name__ == "__main__":
    dic={'dif':'mid','puntosJ':0,'puntosIA':0,'time':10,'pal':[]}
    Jugar(dic,None)
    '''
    datos={"tablero": None};datos.update(dic)
    tablero, backT = crearTablero()
    tablero, backT = cargarTablero(tablero, backT, datos)
    
    dif = ['NN', 'JJ', 'VB']  #<----- VB:verbo   NN:sustantivo   JJ:adjetivo
    coor = [(0, 0), (3, 0), (4, 0), (2, 0), (5, 0)]
    letras = ['P','R','R','E','O']
    print(puntos(dif,coor,letras,backT))

    
    for dato in backT:
        print(dato)'''