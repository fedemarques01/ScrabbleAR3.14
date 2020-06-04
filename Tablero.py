import PySimpleGUI as sg
import json
from datetime import datetime as datetime
from random import getrandbits
from validez import validez
import Letras
from guardarPuntos import Guardar as Gp



def Terminar(letras,dif,puntos,tablero,atrilCPU): #resta los puntos y llama a guardar.py
    for i in range(0,7):
        tablero['-'+str(i)].update(atrilCPU[i].get_letra())           #FALTA actualizar los atriles de la cpu
    resta=0
    for i in letras:
        resta+=i.get_valor()
    puntos-=resta
    Gp(dif,puntos)
    sg.popup('perdiste mostro')
    exit()

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
        [sg.B("Guardar", size=(13, 1), key="-save-",disabled=True)],
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
              ), sg.B("Cambiar", key="-cambiar-", size=(10, 1)),
         sg.B("Deshacer", key="-back-", size=(10, 1))]
    ]

    tablero = sg.Window("ScrabbleAR - Juego", frontT, finalize=True)

    return tablero, backT
# carga todos los botones del tablero, el ya guardado en caso de una partida guardada
def ActualizarAtril(tablero,lista):
    for i in range(0,len(lista)):
        tablero[str(i)].update(lista[i].get_letra(),disabled=False)

    return tablero    

def cargarTablero(tablero, board, datos):
    # si es None, no hay partida guardada entonces carga la lista de tuplas por cada casilla especial
    tabla = datos['tablero']
    tablero['-pJug-'].Update(('Tu puntaje: '+ str(datos['puntosJ'])).format())
    tablero['-pCPU-'].Update(('Puntaje CPU: '+ str(datos['puntosIA'])).format())
    tablero['-dif-'].Update(('Dificultad: '+ datos['dif']).format())
    tablero = ActualizarAtril(tablero, datos['atrilJ'].get_atril_array())
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
    v=validez(dif,coor,letras)
    if v in (0,1):
        return v

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

def modificarTablero(tablero,board,Atril,letras,coord):
    for i in range(0,len(coord)):
        tablero[coord[i]].update(button_color=("#FCC300","#E94E00"),disabled_button_color=("#FCC300","#E94E00"),disabled=True)
        board[coord[0][0]][coord[0][1]] = letras[i]
        Atril.usar_ficha(letras[i])
    Atril.rellenar_atril()
    #print(Atril.get_atril_string())
    tablero = ActualizarAtril(tablero,Atril.get_atril_array())

    return tablero,board,Atril     

def Jugar(settings, event):
    claveA = []
    for i in range(7):
        claveA.append(str(i))    
    sg.theme("Topanga")
    tablero, backT = crearTablero()
    # creo un diccionario con los datos de la partida instanciando un tablero vacio por defecto
    PrimeraJugada = True
    #print("me mori")
    if(event == "continue"):
        arch = open("Guardado.json", "r")
        # si existe una partida guardada datos tendra el backT de la partida anterior en tablero, y los settings de la partida anterior
        datos = (json.load(arch))
        PrimeraJugada = False
    else:
        # sino datos tendra los settings que elijio el jugador o los por defecto
        datos = {"tablero": None,'bolsa':Letras.Bolsa(settings['dif'])}
        datos.update(settings)
        #añado los atriles generados a partir de la bolsa que esta al crear el diccionario
        datos.update({'atrilJ': Letras.Atril(datos['bolsa']),'atrilCPU':Letras.Atril(datos['bolsa'])})
          
    tablero, backT = cargarTablero(tablero, backT, datos)
    if(PrimeraJugada):
        if(True or getrandbits(1)):
            sg.popup('Empiezas tu!')
            listLetra = []
            listCoord = []
            aux = ""
            while True:
                event, _ = tablero.read()
                print(event)

                if event == None:
                    break  

                elif(event in claveA):
                    aux = event

                elif event == (7,7) and aux != "":
                    listCoord.append(event)
                    listLetra.append(datos['atrilJ'].get_atril_array()[int(aux)].get_letra())
                    tablero[event].update(listLetra[-1])
                    #print("por favor no te rompas")
                    tablero[aux].update(disabled=True)
                    aux = ""

                elif len(event) == 2 and len(listLetra) >= 1 and aux != "":
                    listCoord.append(event)
                    listLetra.append(datos['atrilJ'].get_atril_array()[int(aux)].get_letra())
                    tablero[event].update(listLetra[-1])
                    #print("por favor no te rompas")
                    tablero[aux].update(disabled=True)
                    aux = ""

                elif event == "-fin-":
                    #print("Algo")
                    punt = puntos(datos['pal'],listCoord,listLetra,backT)
                    if(punt == 0):
                        tablero["-comment-"].update("La palabra no es valida, ingrese las letras en orden una al lado de la otra e intente de nuevo".format())
                        #devolverfichas
                        listLetra = listCoord = []
                    else:
                        datos['puntosJ'] += punt
                        tablero["-comment-"].update(("Sumaste " + str(punt) + " puntos").format())
                        tablero['-pJug-'].Update(('Tu puntaje: '+ str(datos['puntosJ'])).format())
                        tablero,backT,datos['atrilJ'] = modificarTablero(tablero,backT,datos['atrilJ'],listLetra,listCoord)
                        print(datos['puntosJ'])
                        listLetra = listCoord = []
                        break    

                elif event == 'Exit':
                    Terminar(datos['atrilJ'].get_atril_array(),settings['dif'],settings['puntosJ'],tablero,datos['atrilCPU'].get_atril_array())

        else:
            sg.popup("Empieza la CPU")
            #Esto esta para ver el tablero nada mas, la idea es sacarlo despues
            while True:
                event, _ = tablero.read()
                print(event)
                if event == (7,7):
                    print("por favor no te rompas")
                elif event in (None,'Exit'):
                    break
            #Primera jugada pc
        tablero['-save-'].update(disabled=False)    

    while True:
        event, _ = tablero.read()
        if event in (None,"Exit"):
            break



if __name__ == "__main__":
    dic={'dif':'medium','puntosJ':0,'puntosIA':0,'time':10,'pal':['NN','JJ','VB']}
    Jugar(dic,None)
    '''
    datos={"tablero": None};datos.update(dic)
    tablero, backT = crearTablero()
    tablero, backT = cargarTablero(tablero, backT, datos)
    
    dif = ['NN', 'JJ', 'VB']  #<----- VB:verbo   NN:sustantivo   JJ:adjetivo
    coor = [(0, 0), (3, 0), (4, 0), (2, 0), (5, 0)]
    print(puntos(dif,coor,letras,backT))

    
    for dato in backT:
        print(dato)'''