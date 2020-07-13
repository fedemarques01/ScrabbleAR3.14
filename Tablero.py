import PySimpleGUI as sg
import json
import time
from datetime import datetime as datetime
from random import getrandbits, randint
from Validez import validez
import Letras
from GuardarPuntos import Guardar as Gp
import IA as CPU


def GuardarPartida(datos):
    datos['bolsa'] = datos['bolsa'].get_bolsa()
    datos['atrilJ'] = datos['atrilJ'].get_atril_array()
    datos['atrilCPU'] = datos['atrilCPU'].get_atril_array()
    with open("Guardado.json", "w") as arch:
        json.dump(datos, arch)
    exit()

#se encarga de terminar la partida y decidir el ganador actualizando las puntuaciones
def Terminar(letras, dif, puntos, puntia, tablero, atrilCPU):  
    # resta los puntos y llama a guardar.py
    try:
        for i in range(0, 7):
            tablero['-'+str(i)].update(atrilCPU[i])
        resta = 0
    except IndexError:
        pass    
    for i in letras:
        resta += Letras.valoresLetras[i]
    puntos -= resta
    Gp(dif, puntos)
    if(puntia>=puntos):
        sg.popup('Perdiste mostro')
    else:
        sg.popup('perdiste menos mostro')
    exit()

#maneja la primer jugada de la pc de la partida, basicamente, el que la palabra vaya al ST
def PrimerJugadaPC(tablero,datos,backT,clock,current_time,inicio):
                
    letras = CPU.CPUmain(datos['atrilCPU'].get_atril_array(), datos['pal'])
                
    if(len(letras)<1):
        for i in datos['atrilCPU'].get_atril_array():
            datos['atrilCPU'].usar(i)
        datos['atrilCPU'].cambiar_Fichas(letras)
        turnoPC = False
        pass
    coor = []
    if(getrandbits(1)):
        for i in range(len(letras)):
            coor.append((7, 7+i))
    else:
        for i in range(len(letras)):
            coor.append((7+i, 7))
            #print(coor, letras)
    punt = puntos(datos['pal'], coor, letras, backT, False)
    datos['puntosIA'] += punt
    tablero["-comment-"].update(("La palabra de la CPU vale " +
                                    str(punt) + " puntos").format())
    tablero['-pCPU-'].Update(('Puntos CPU: ' +
                            str(datos['puntosIA'])).format())
    backT, datos['atrilCPU'] = modificarTablero(
        tablero, backT, datos['atrilCPU'], letras, coor, False)
    turnoPC = False
    event = ''
    clock = actualizarTimer(tablero,current_time,inicio)
    PrimeraJugada = False

    return datos,backT,clock,turnoPC,PrimeraJugada


def casillasCPU(lentra, board):
    coor = []
    while(lentra != len(coor)):
        coor = []
        n = randint(0, 15-lentra)
        if(getrandbits(1)):
            for i in range(lentra):
                #print(coor,i)
                coor.append((n, n+i))
                if(not board[coor[i][0]][coor[i][1]] in ("Lx2","Lx3","Px2","Px3","")):
                    break
        else:
            for i in range(lentra):
                #print(coor,i)
                coor.append((n+i, n))
                if(not board[coor[i][0]][coor[i][1]] in ("Lx2","Lx3","Px2","Px3","")):
                    break
    #print('da',coor)
    return coor

#Todo el setup de la intefaz del juego, la creacion de la ventana tablero en su maximo esplendor
def crearTablero():
    col = fil = 15
    """
    col,fil y fichas son constantes que se usan a la hora de definir las proporciones del tablero y las fichas por estante de jugador
    BackT es el tablero pero en back end, usado a la hora de ver el contenido de las casillas
    y es actualizado cuando se verifica una palabra
    """

    fichas = 7
    backT = [["" for i in range(col)] for i in range(fil)]
    # ColM es la columna donde se encuentra la informacion de la partida junto a otros comentarios y los botones para terminar y guardar la partida
    colM = [
        [sg.B("Guardar", size=(13, 1), key="-save-", disabled=True)],
        [sg.B("Terminar", size=(13, 1), key="Exit")],
        [sg.Frame(layout=[[sg.Text("Ponga una ficha en ST para comenzar la partida", size=(13, 10), key="-comment-", background_color="#190901")]],
                  title="Comentarios", title_color="Yellow", background_color="Black", key="-block-")],
        [sg.Frame(layout=[[sg.Text('00:00:00', size=(13, 1), font=('Helvetica', 10), justification='center', key='-timer-', background_color="#190901")]],
                  title="Tiempo", title_color="Orange", background_color="Black")],
        [sg.Text(text="Dificultad: ", size=(13, 1), key="-dif-")],
        [sg.Text(text="Tu puntaje: 0", size=(13, 1), key="-pJug-")],
        [sg.Text(text="Puntaje CPU: 0", size=(13, 1), key="-pCPU-")]
    ]

    # col board es la columna donde esta el atril del cpu y el tablero, generados de esta forma para que quede una columna al lado de la otra
    colBoard = [[sg.Text("CPU:"), sg.Text(font=("Times New Roman", 17),
                                          text="                            S C R A B B L E A R ", justification="right")]]

    colBoard += [[sg.B("?", key=('-'+str(i)), size=(2, 1), pad=(0, 0), disabled=True)
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

    return tablero,backT

#Muestra las nuevas fichas del jugador o las habilita en caso de que puedan ser usadas de nuevo
def ActualizarAtril(tablero, lista):
    for i in range(0, len(lista)):
        tablero[str(i)].update(lista[i], disabled=False)

#Carga todos los datos de una partida ya sea una anterior o una nueva
def CargarTablero(tablero, board, datos):
    # si es None, no hay partida guardada entonces carga la lista de tuplas por cada casilla especial
    tabla = datos['tablero']
    tablero['-pJug-'].Update(('Tu puntaje: ' + str(datos['puntosJ'])).format())
    tablero['-pCPU-'].Update(('Puntaje CPU: ' +
                        str(datos['puntosIA'])).format())                          
    tablero['-dif-'].Update(('Dificultad: ' + datos['dif']).format())
    if(datos['cambios'] == 0):
        tablero['-cambiar-'].update("Pasar")
    ActualizarAtril(tablero, datos['atrilJ'].get_atril_array())
    if(tabla == None):
        #se lee un .json con las coordenadas de las casillas de especiales segun la dificultad
        if(datos['dif'] == 'easy'):
            with open('TableroFacil.json','r') as arch:
                dic = json.load(arch)
        elif datos['dif'] == 'medium':
            with open('TableroNormal.json','r') as arch:
                dic = json.load(arch)
        elif datos['dif'] == 'hard':
            with open('TableroDificil.json','r') as arch:
                dic = json.load(arch)        
        print(dic['tripleL'])
        for x in dic['tripleL']:
            tablero[(x[0],x[1])].Update(
                "Lx3", button_color=("#e8c204", "#13866c"))
            board[x[0]][x[1]] = "Lx3"
        for x in dic['doubleL']:
            tablero[(x[0],x[1])].Update(
                "Lx2", button_color=("#e8c204", "#63025d"))
            board[x[0]][x[1]] = "Lx2"
        for x in dic['doubleW']:
            tablero[(x[0],x[1])].Update(
                "Px2", button_color=("#e8c204", "#9E1180"))
            board[x[0]][x[1]] = "Px2"
        for x in dic['tripleW']:
            tablero[(x[0],x[1])].Update(
                "Px3", button_color=("#e8c204", "#63021e"))
            board[x[0]][x[1]] = "Px3"
        for x in dic['castigo3']:
            tablero[(x[0],x[1])].Update(
                "-3", button_color=("#e8c204", "#632802"))
            board[x[0]][x[1]] = "-3"
        for x in dic['castigo5']:
            tablero[(x[0],x[1])].Update(
                "-5", button_color=("#e8c204", "#1c0263"))
            board[x[0]][x[1]] = "-5"    
        tablero[(7,7)].Update(
            "St", button_color=("#e8c204", "#000000"))
        board[7][7] = "St"

    # caso contrario, recorre el tablero guardado y actualiza en base a eso
    else:

        board = tabla
        for i in range(len(tabla)):
            for j in range(len(tabla[i])):
                if(tabla[i][j] == ""):
                    continue
                elif(tabla[i][j] == "Lx3"):
                    tablero[(i, j)].Update(
                        "Lx3", button_color=("#e8c204", "#13866c"))
                elif(tabla[i][j] == "Lx2"):
                    tablero[(i, j)].Update(
                        "Lx2", button_color=("#e8c204", "#63025d"))
                elif(tabla[i][j] == "Px2"):
                    tablero[(i, j)].Update(
                        "Px2", button_color=("#e8c204", "#9E1180"))
                elif(tabla[i][j] == "Px3"):
                    tablero[(i, j)].Update(
                        "Px3", button_color=("#e8c204", "#63021e"))
                elif(tabla[i][j] == "-3"):
                    tablero[(i, j)].Update(
                        "-3", button_color=("#e8c204", "#632802"))
                elif(tabla[i][j] == "-5"):
                    tablero[(i, j)].Update(
                        "-5", button_color=("#e8c204", "#1c0263"))        
                else:
                    tablero[(i, j)].Update(tabla[i][j],button_color=(
                        "#FCFF41", "#870303"),disabled_button_color=(
                        "#FCFF41", "#870303"),disabled=True)  # color y valor de la letra que ya estaba

    return board

#modifica el contenido del tablero de juego al verificar una palabra o devolver las fichas
def modificarTablero(tablero, board, Atril, letras, coord, Jug=True):
    for i in range(0, len(coord)):
        board[coord[i][0]][coord[i][1]] = letras[i]
        if(Jug):
            tablero[coord[i]].update(button_color=(
                "#FCC300", "#E94E00"), disabled_button_color=("#FCC300", "#E94E00"), disabled=True)
        else:
            tablero[coord[i]].update(letras[i], button_color=(
                "#FCC300", '#208020'), disabled_button_color=("#FCC300", '#208020'), disabled=True)

        Atril.usar(letras[i])
    Atril.rellenar_atril()
    # print(Atril.get_atril_string())
    if(Jug):
        ActualizarAtril(tablero, Atril.get_atril_array())

    return board, Atril


def puntos(dif, coor, letras, board, Jug=True):
    if(Jug):
        v = validez(dif, coor, letras)
        if v in (0, 1):
            return v

    pt, pp = 0, 1
    for i in range(len(coor)):
        pl = Letras.valoresLetras[letras[i]]
        bonus = board[coor[i][0]][coor[i][1]]
        if bonus != "":
            if bonus == "Lx2":
                pl *= 2
            elif bonus == "Lx3":
                pl *= 3
            elif bonus == "Px2":
                pp *= 2
            elif bonus == "Px3":
                pp *= 3
        pt += pl
    return pt*pp

#habilita las casillas que tenian fichas y las libera para ser reutilizadas
def DevolverFichas(tablero, coord, board):
    for i in coord:
        tablero[i].update(board[i[0]][i[1]], disabled=False)

#Todas las operaciones que se efectuan para que el jugador cambie una o mas fichas
def cambiar(tablero, atril,current_time,inicio):
    tablero['-comment-'].update(
        'Seleccione las fichas que desea cambiar y pulse comprobar para cambiarlas o deshacer para volver una ficha atras o cancelar'.format())
    tablero['-save-'].update(disabled=True)
    tablero['Exit'].update(disabled=True)
    tablero['-cambiar-'].update(disabled=True)
    letras = []
    pos = []
    while True:
        clock = actualizarTimer(tablero,current_time,inicio)
        event, _ = tablero.read(timeout=250)
        if event == None:
            exit()
        elif len(event) == 1:
            letras.append(atril.get_atril_array()[int(event)])
            tablero[event].update(disabled=True)
            pos.append(event)
        elif event == '-back-':
            if letras == []:
                break
            tablero[pos[-1]].update(disabled=False)
            letras.pop()
            pos.pop()
        elif event == '-check-':
            break
    # si seleccioné letras entonces saco las fichas del atril y agarro nuevas, actualizando el atril visual
    booleano = False
    if letras != []:
        for i in letras:
            atril.usar(i)
        atril.cambiar_Fichas(letras)
        print(atril.get_atril_array())
        booleano = True
    ActualizarAtril(tablero, atril.get_atril_array())    
    tablero['-save-'].update(disabled=False)
    tablero['Exit'].update(disabled=False)
    tablero['-cambiar-'].update(disabled=False)
    return atril,booleano,clock

#Actualiza el tiempo restante
def actualizarTimer(tablero,current_time,inicio):
    boolean = True
    current_time = current_time + inicio - int(time.time())
    if(current_time < 0):
        boolean = False
        mins = 0
        secs = 0
    else:    
        mins, secs = divmod(current_time, 60)
    tablero['-timer-'].update('{:02d}:{:02d}'.format(mins, secs))
    return boolean

#Se encarga de hacer posible el jugar una partida de scrabble, utiliza todas las funciones previas
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
        datos['bolsa'] = Letras.Bolsa(datos['bolsa'])
        datos['atrilJ'] = Letras.Atril(datos['bolsa'])
        datos['atrilCPU'] = Letras.Atril(datos['bolsa'])
        tablero['-save-'].update(disabled=True)
        tablero['-comment-'].update('Bienvenido de nuevo!'.format())
        PrimeraJugada = False
    else:
        # sino datos tendra los settings que elijio el jugador o los por defecto
        datos = {"tablero": None, 'cambios': 3}
        if settings['bolsa'] == []:
            settings['bolsa'] = Letras.Bolsa(settings['dif']) 
        datos.update(settings)
        # añado los atriles generados a partir de la bolsa que esta al crear el diccionario
        datos.update({'atrilJ': Letras.Atril(
            datos['bolsa']), 'atrilCPU': Letras.Atril(datos['bolsa'])})

    backT = CargarTablero(tablero, backT, datos)
    turnoPC = False
    #variables del timer
    clock = True
    if not PrimeraJugada:
        inicio = int(time.time())
        current_time = datos['time']
    else:
        # determina quien comienza si el jugador o la pc
        turnoPC = not getrandbits(1)
        inicio = int(time.time())#tiempo comienzo 
        current_time = datos['time']*60 + 1
        if(turnoPC):
            sg.popup("Empieza la CPU",auto_close=True,auto_close_duration=2)
            datos,backT,clock,turnoPC,PrimeraJugada = PrimerJugadaPC(tablero,datos,backT,clock,current_time,inicio)   
        else:    
            sg.popup('Empiezas tu!')
    listLetra = []
    listCoord = []
    aux = ""
    #en caso de errores coloque aqui el primer while de abajo    
    
    listLetra = []
    listCoord = []

    while True:
        if(backT[7][7] != 'St'):
            PrimeraJugada = False
        clock = actualizarTimer(tablero,current_time,inicio)
        #solucion trucha para que el usuario vea el 00:00
        if(datos['bolsa'].cantidad_Fichas() == 0):
            tablero["-comment-"].update(
                            "La bolsa no tiene mas fichas".format())
            Terminar(datos['atrilJ'].get_atril_array(),
                        datos['dif'], datos['puntosJ'],datos['puntosIA'], tablero, datos['atrilCPU'].get_atril_array())
        if(turnoPC) and clock:
            if(PrimeraJugada):
                datos,backT,clock,turnoPC,PrimeraJugada = PrimerJugadaPC(tablero,datos,backT,clock,current_time,inicio) 
            letras = CPU.CPUmain(datos['atrilCPU'].get_atril_array(), datos['pal'])
            coor = []
            
            if(len(letras)<1):
                for i in datos['atrilCPU'].get_atril_array():
                        datos['atrilCPU'].usar(i)
                datos['atrilCPU'].cambiar_Fichas(letras)
                tablero["-comment-"].update(("La CPU ha decidido pasar su turno").format())
                turnoPC = False
                continue
            print('\n',letras)

            #alpha para darle las coor a la palabra
            coor= casillasCPU(len(letras), backT)
            print(coor,'\n')

            #calcular puntos en base a las coordenadas y las letras
            punt = puntos(datos['pal'], coor, letras, backT, False)
            datos['puntosIA'] += punt
            #CPU-puntos++
            tablero["-comment-"].update(("La palabra de la CPU vale " + str(punt) + " puntos").format())
            tablero['-pCPU-'].Update(('Puntos CPU: ' + str(datos['puntosIA'])).format())
            #modificarTablero.. hace eso.. modifica.. el tablero..
            backT, datos['atrilCPU'] = modificarTablero(tablero, backT, datos['atrilCPU'], 
            letras, coor, False)
            turnoPC = False #pasa el turno al usuario

        event, _ = tablero.read(timeout=250)
        #revisa si se termino el tiempo, se eligio terminar o se cerro la ventana, en los dos primeros casos termina la partida y muestra el ganador
        if event in (None, 'Exit') or not clock:
            if(event == 'Exit') or not clock:
                Terminar(datos['atrilJ'].get_atril_array(
                ), datos['dif'], datos['puntosJ'],datos['puntosIA'], tablero, datos['atrilCPU'].get_atril_array())
            break
        # me fijo si el event es una de las posibles llaves de las letras y lo guardo en un auxiliar
        elif(event in claveA):
            aux = event
        #pongo la letra eligida en la casilla y se guarda en la lista de letras que se usan para formar la palabra    
        elif type(event) is tuple and aux != "":
            listCoord.append(event)
            listLetra.append(datos['atrilJ'].get_atril_array()[int(aux)])
            tablero[event].update(
                listLetra[-1], disabled=True, disabled_button_color=("#FCC300", "#E94E00"))
            tablero[aux].update(disabled=True)
            aux = ""
        elif event == "-check-" and listCoord != []:
            if(PrimeraJugada and not((7,7) in listCoord)):
                sg.popup('La palabra debe tener una letra sobre el st')
                DevolverFichas(tablero, listCoord, backT)
                ActualizarAtril(
                    tablero, datos['atrilJ'].get_atril_array())
            else:
                punt = puntos(datos['pal'], listCoord, listLetra, backT)
                if(punt <= -100):
                    if(punt == -200):
                        tablero["-comment-"].update(
                            "La palabra no es valida, pruebe una palabra distinta".format())
                    else:
                        tablero["-comment-"].update(
                            "Las fichas se colocaron erroneamente en el tablero,pruebe colocarlas una al lado de otra o una debajo de otra".format())
                    DevolverFichas(tablero, listCoord, backT)
                    ActualizarAtril(
                        tablero, datos['atrilJ'].get_atril_array())    
                else:
                    datos['puntosJ'] += punt
                    if datos['puntosJ'] < 0:
                        datos['puntosJ'] = 0
                    tablero["-comment-"].update(("Tu palabra tiene un valor de " +
                                            str(punt) + " puntos. \nLa CPU esta pensando.").format())
                    tablero['-pJug-'].Update(('Tu puntaje: ' +
                                        str(datos['puntosJ'])).format())
                    backT, datos['atrilJ'] = modificarTablero(
                        tablero, backT, datos['atrilJ'], listLetra, listCoord, "#E94E00")
                    print(datos['puntosJ'])
                    turnoPC = True
                    sg.popup_auto_close(auto_close_duration=0.00000001)
                    time.sleep(2)
                
            listLetra = []
            listCoord = []
        # le devuelvo las fichas al jugador si ya ingreso alguna
        elif event == "-back-" and listCoord != []:
            DevolverFichas(tablero, listCoord, backT)
            ActualizarAtril(
                tablero, datos['atrilJ'].get_atril_array())
            listLetra = []
            listCoord = []
        #guarda todos los datos de la partida y cierra el programa
        elif event == "-save-":
            datos['time'] = current_time + inicio - int(time.time())
            datos['tablero'] = backT
            sg.popup("La partida se ha guardado")
            GuardarPartida(datos)
        #Devuelve las fichas ingresadas pero no comprobadas y le permite al usuario cambiar sus fichas    
        elif event == '-cambiar-':
            DevolverFichas(tablero, listCoord, backT)
            if(datos['cambios'] > 0):
                datos['atrilJ'], changed, clock = cambiar(tablero, datos['atrilJ'],current_time,inicio)
                datos['cambios'] -= 1
                if(datos['cambios'] == 0):
                    tablero['-cambiar-'].update('Pasar')
            tablero['-comment-'].update(''.format())
            listLetra = []
            listCoord = []    
            if(changed) or datos['cambios'] == 0:
                turnoPC = True



    tablero.close()


if __name__ == "__main__":
    dic = {'dif': 'hard', 'puntosJ': 0, 'puntosIA': 0, 'time': 10,'pal':['NN','JJ','VB'],'bolsa':[]}
    Jugar(dic, None)
    '''
    datos={"tablero": None};datos.update(dic)
    tablero, backT = crearTablero()
    tablero, backT = cargarTablero(tablero, backT, datos)
    
    dif = ['NN', 'JJ', 'VB']  #<----- VB:verbo   NN:sustantivo   JJ:adjetivo
    coor = [(0, 0), (3, 0), (4, 0), (2, 0), (5, 0)]
    print(puntos(dif,coor,letras,backT))

    
    for dato in backT:
        print(dato)'''
