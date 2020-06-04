import PySimpleGUI as sg
import json
from datetime import datetime as datetime
from random import getrandbits, randint
from Validez import validez
import Letras
from GuardarPuntos import Guardar as Gp
import IA as CPU

def GuardarPartida(datos):
    with open("Guardado.json","w") as arch:
        json.dump(arch, datos)
    exit()    

def Terminar(letras,dif,puntos,tablero,atrilCPU): #resta los puntos y llama a guardar.py
    for i in range(0,7):
        tablero['-'+str(i)].update(atrilCPU[i])           #FALTA actualizar los atriles de la cpu
    resta=0
    for i in letras:
        resta+= Letras.valoresLetras[i]
    puntos-=resta
    Gp(dif,puntos)
    sg.popup('Perdiste mostro')
    exit()

def casillas(lentra,board):
    coor=[]
    while(lentra!=len(coor)):
        coor=[]
        n=randint(0,7)
        if(getrandbits(1)):
            for i in range(lentra):
                coor[i].append(n,n+i)
                if(board[coor[i][0]][coor[i][1]]):
                    continue
        else:
            for i in range(lentra):
                coor[i].append(n+1,n)
                if(board[coor[i][0]][coor[i][1]]):
                    continue

    return coor
    
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
        [sg.Frame(layout=[[sg.Text("Ponga una ficha en ST para comenzar la partida", size=(13, 10), key="-comment-",background_color="#190901")]],
                  title="Comentarios", title_color="Yellow", background_color="Black", key="-block-")],
        [sg.Text(text="Dificultad: ",size=(13,3) ,key="-dif-")],
        [sg.Text(text="Tu puntaje: 0",size=(13,3) ,key="-pJug-")],
        [sg.Text(text="Puntaje CPU: 0",size=(13,3) ,key="-pCPU-")]
    ]

    # col board es la columna donde esta el atril del cpu y el tablero, generados de esta forma para que quede una columna al lado de la otra
    colBoard = [[sg.Text("CPU:"),sg.Text(font=("Times New Roman",17),text="                            S C R A B B L E A R ",justification="right")]]

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
         sg.B("Comprobar", key="-check-", size=(10, 1)
              ), sg.B("Cambiar", key="-cambiar-", size=(10, 1)),
         sg.B("Deshacer", key="-back-", size=(10, 1))]
    ]

    tablero = sg.Window("ScrabbleAR - Juego", frontT, finalize=True)

    return tablero, backT

# carga todos los ajustes de la partida(puntaje,dificultad,botones especiales,bolsa,etc)
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
        board[start_button[0]][start_button[1]] = "St"    
    
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
                        "#FCC300", "#E94E00"))  # color y valor de la letra que ya estaba
    

    return tablero, board

def ActualizarAtril(tablero,lista):
    for i in range(0,len(lista)):
        tablero[str(i)].update(lista[i],disabled=False)

    return tablero                    

def modificarTablero(tablero,board,Atril,letras,coord,Jug=True):
    for i in range(0,len(coord)):
        board[coord[0][0]][coord[0][1]] = letras[i]        
        if(Jug):
            tablero[coord[i]].update(button_color=("#FCC300","#E94E00"),disabled_button_color=("#FCC300","#E94E00"),disabled=True)
        else:       
            tablero[coord[i]].update(letras[i], button_color=("#FCC300",'#208020'),disabled_button_color=("#FCC300",'#208020'),disabled=True)

        Atril.usar_ficha(letras[i])
    Atril.rellenar_atril()
    #print(Atril.get_atril_string())
    if(Jug):
        tablero = ActualizarAtril(tablero,Atril.get_atril_array())

    return tablero,board,Atril

def puntos(dif,coor,letras,board,Jug=True):
    if(Jug):
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

def devolverFichas(tablero,coord,board):
    for i in coord:   
        tablero[i].update(board[i[0]][i[1]], disabled=False)
    return tablero         

def Jugar(settings, event):
    claveA = []
    for i in range(7):
        claveA.append(str(i))    
    sg.theme("Topanga")
    tablero, backT = crearTablero()
    # creo un diccionario con los datos de la partida instanciando un tablero vacio por defecto
    PrimeraJugada = True
    if(event == "continue"):
        
        # si existe una partida guardada datos tendra el backT de la partida anterior en tablero, y los settings de la partida anterior
        with open("Guardado.json", "r") as arch:
            datos = json.load(arch)
        PrimeraJugada = False
    else:
        # sino datos tendra los settings que elijio el jugador o los por defecto
        datos = {"tablero": None,'bolsa':Letras.Bolsa(settings['dif'])}
        datos.update(settings)
        #añado los atriles generados a partir de la bolsa que esta al crear el diccionario
        datos.update({'atrilJ': Letras.Atril(datos['bolsa']),'atrilCPU':Letras.Atril(datos['bolsa'])})
          
    tablero, backT = cargarTablero(tablero, backT, datos)
    if(PrimeraJugada):
        if(False or getrandbits(1)):
            sg.popup('Empiezas tu!')
            listLetra = []
            listCoord = []
            aux = ""
            while True:
                event, _ = tablero.read()
                print(event)

                if event in (None,'Exit'):
                    if(event == 'Exit'):
                        Terminar(datos['atrilJ'].get_atril_array(),
                        datos['dif'],datos['puntosJ'],tablero,datos['atrilCPU'].get_atril_array())
                    break  
                #me fijo si el event es una de las posibles llaves de las letras y lo guardo en un auxiliar
                elif(event in claveA):
                    aux = event
                #si ya elegi una letra solo entro al elegir st ya que en la primer jugada la letra va obligatoriamente en esa posicion
                elif event == (7,7) and aux != "":
                    listCoord.append(event) #guardo en la lista de coordenadas
                    listLetra.append(datos['atrilJ'].get_atril_array()[int(aux)]) #guardo en la lista de letras
                    tablero[event].update(listLetra[-1],disabled=True,disabled_button_color=("#FCC300","#E94E00"))#deshabilito el boton y actualizo la casilla con la letra elegida
                    tablero[aux].update(disabled=True)#deshabilito la ficha del atril que el jugador coloco
                    aux = ""#dejo libre para seleccionar otra letra
                #igual que el anterior, solo que evalua el que ya se haya ingresado una ficha en el st
                elif len(event) == 2 and len(listLetra) >= 1 and aux != "":
                    listCoord.append(event)
                    listLetra.append(datos['atrilJ'].get_atril_array()[int(aux)])
                    tablero[event].update(listLetra[-1],disabled=True,disabled_button_color=("#FCC300","#E94E00"))
                    tablero[aux].update(disabled=True)
                    aux = ""

                elif event == "-check-" and listCoord != []:
                    #print("Algo")
                    punt = puntos(datos['pal'],listCoord,listLetra,backT)
                    if(punt <= 1):
                        if(punt == 1):
                            tablero["-comment-"].update("La palabra no es valida, pruebe una palabra distinta".format())
                        else:
                            tablero["-comment-"].update("Las fichas se colocaron erroneamente en el tablero,pruebe colocarlas una al lado de otra o una debajo de otra".format())
                                
                        tablero = devolverFichas(tablero,listCoord,backT)
                        tablero = ActualizarAtril(tablero,datos['atrilJ'].get_atril_array())
                        listLetra = []
                        listCoord = []
                    else:
                        datos['puntosJ'] += punt
                        tablero["-comment-"].update(("Sumaste " + str(punt) + " puntos").format())
                        tablero['-pJug-'].Update(('Tu puntaje: '+ str(datos['puntosJ'])).format())
                        tablero,backT,datos['atrilJ'] = modificarTablero(tablero,backT,datos['atrilJ'],listLetra,listCoord)
                        print(datos['puntosJ'])
                        break 
                #le devuelvo las fichas al jugador si ya ingreso alguna    
                elif event == "-back-" and listCoord != []:       
                    tablero = devolverFichas(tablero,listCoord,backT)
                    tablero = ActualizarAtril(tablero,datos['atrilJ'].get_atril_array())
                    listLetra = []
                    listCoord = [] 
                    
        else:
            sg.popup("Empieza la CPU")
            tablero["-comment-"].update(("La CPU esta pensando").format())
            letras=CPU.CPUmain(datos['atrilCPU'].get_atril_array(),datos['pal'])
            coor=[]
            for i in range(len(letras)):
                coor.append((7,7+i))
            print(coor,letras)
            tablero["-comment-"].update(("La CPU suma " + str(punt) + " puntos").format())
            tablero['-pCPU-'].Update(('Puntos CPU: '+ str(datos['puntosCPU'])).format())
            datos['puntosCPU'] += puntos(datos['pal'],coor,letras,backT,False)
            tablero,backT = modificarTablero(tablero,backT,datos['atrilCPU'],letras,coor,False)
        if(event != None):    
            tablero['-save-'].update(disabled=False)    
    
    listLetra = []
    listCoord = [] 
    while True:
        event, _ = tablero.read()
        print(event)

        if event in (None,'Exit'):
            if(event == 'Exit'):
                Terminar(datos['atrilJ'].get_atril_array(),datos['dif'],datos['puntosJ'],tablero,datos['atrilCPU'].get_atril_array())
            break  
        #me fijo si el event es una de las posibles llaves de las letras y lo guardo en un auxiliar
        elif(event in claveA):
            aux = event
        elif len(event) == 2 and aux != "":
            listCoord.append(event)
            listLetra.append(datos['atrilJ'].get_atril_array()[int(aux)].get_letra())
            tablero[event].update(listLetra[-1],disabled=True,disabled_button_color=("#FCC300","#E94E00"))
            tablero[aux].update(disabled=True)
            aux = ""
        elif event == "-check-" and listCoord != []:
            punt = puntos(datos['pal'],listCoord,listLetra,backT)
            if(punt <= 1):
                if(punt == 1):
                    tablero["-comment-"].update("La palabra no es valida, pruebe una palabra distinta".format())
                else:
                    tablero["-comment-"].update("Las fichas se colocaron erroneamente en el tablero,pruebe colocarlas una al lado de otra o una debajo de otra".format())                        
                tablero = devolverFichas(tablero,listCoord,backT)
                tablero = ActualizarAtril(tablero,datos['atrilJ'].get_atril_array())
            else:
                datos['puntosJ'] += punt
                tablero["-comment-"].update(("Sumaste " + str(punt) + " puntos").format())
                tablero['-pJug-'].Update(('Tu puntaje: '+ str(datos['puntosJ'])).format())
                tablero,backT,datos['atrilJ'] = modificarTablero(tablero,backT,datos['atrilJ'],listLetra,listCoord,"#E94E00")
                print(datos['puntosJ'])
            listLetra = []
            listCoord = []     
        #le devuelvo las fichas al jugador si ya ingreso alguna    
        elif event == "-back-" and listCoord != []:       
            tablero = devolverFichas(tablero,listCoord,backT)
            tablero = ActualizarAtril(tablero,datos['atrilJ'].get_atril_array())
            listLetra = []
            listCoord = []
        elif event == "-save-":
            datos['tablero'] = backT
            sg.popup("La partida se ha guardado")
            #GuardarPartida(datos)

    tablero.close()    



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