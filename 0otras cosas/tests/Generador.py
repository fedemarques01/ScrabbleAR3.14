import json
import PySimpleGUI as sg

"""Este .py es utilizado para cargar los datos de los tableros dependiendo
de la dificultad y es utilizado tambien para cargar los datos de una partida anterior."""


"""triple_letter = (1, 5), (1, 9), (5, 1), (5, 5), (5, 9),
                        (5, 13), (9, 1), (9, 5), (9, 9), (9, 13), (13, 5), (13, 9)
        double_letter = (0, 3), (0, 11), (2, 6), (2, 8), (3, 0), (3, 7), (3, 14), (6, 2), (6, 6), (6, 8), (6, 12), (
            7, 3), (7, 11), (8, 2), (8, 6), (8, 8), (8, 12), (11, 0), (11, 7), (11, 14), (12, 6), (12, 8), (14, 3), (14, 11)
        double_word = (1, 1), (2, 2), (3, 3), (4, 4), (1,
                       13), (2, 12), (3, 11), (4, 10),
                (13, 1), (12, 2), (11, 3), (10, 4), (10,
                 10), (11, 11), (12, 12), (13, 13)
        triple_word = (0, 0), (0, 7), (0, 14), (7, 0),
                    (7, 14), (14, 0), (14, 7), (14, 14)
        start_button = (7, 7)
"""
dificil = [
    [(0, 0), (0, 7), (0, 14), (7, 0), (7, 14), (14, 0), (14, 7), (14, 14)],
    [(2, 4), (2, 10), (4, 2), (4, 12), (10, 2), (10, 12), (12, 4), (12, 10)],
    [(2, 7), (4, 5), (4, 9), (5, 4), (5, 10), (7, 2), (7, 12), (9, 4), (9, 10), (10, 5), (10, 9), (12, 7)],
    [(3, 3), (3, 11), (6, 6), (6, 8), (8, 6), (8, 8), (11, 3), (11, 11)],
    [(1, 5), (1, 9), (3, 6), (3, 8), (5, 1), (5, 13), (6, 3), (6, 11), (8, 3), (8, 11), (9, 1), (9, 13), (13, 5), (13, 9)],
    [(0, 3), (0, 11), (1, 2), (1, 12), (2, 1), (2, 13), (3, 0), (3, 14), (5, 7), (7, 5), (7, 9), (9, 7), (11, 14), (12, 13), (13, 12), (14, 11)]
]

facil = [
    [(0, 0), (0, 7), (0, 14), (7, 0), (7, 14), (14, 0), (14, 7), (14, 14)],
    [(2, 1), (2, 13), (3, 2), (3, 12), (4, 3), (4, 11), (10, 3), (10, 11), (11, 2), (11, 12), (12, 1), (12, 13)],
    [(2, 6), (2, 8), (6, 2), (6, 6), (6, 8), (6, 12), (8, 2), (8, 6), (8, 8), (8, 12), (12, 6), (12, 8)],
    [(0, 4), (0, 10), (4, 0), (4, 6), (4, 8), (4, 14), (5, 5), (5, 9), (6, 4), (6, 10), (8, 4), (8, 10), (9, 5), (9, 9), (10, 0), (10, 6), (10, 8), (10, 14), (14, 4)], (14, 10),
    [(2, 3), (2, 11), (5, 1), (5, 13), (9, 1), (9, 13), (12, 3), (12, 11)],
    [(3, 7), (7, 3), (7, 11), (11, 7)]
    ]

normal = [
    [(0, 0), (0, 7), (0, 14), (7, 0), (7, 14), (14, 0), (14, 7), (14, 14)],
    [(1, 1), (1, 13), (2, 2), (2, 12), (4, 4), (4, 10), (10, 4), (10, 10), (12, 2), (12, 12), (13, 1), (13, 13)],
    [(3, 6), (3, 8), (6, 3), (6, 11), (8, 3), (8, 11), (11, 6), (11, 8)],
    [(0, 3), (0, 11), (3, 0), (3, 14), (5, 7), (7, 5), (7, 9), (9, 7), (11, 0), (11, 14), (14, 3), (14, 11)],
    [(2, 7), (3, 3), (3, 11), (6, 6), (6, 8), (8, 6), (8, 8), (11, 3), (11, 11), (12, 7)],
    [(2, 5), (2, 9), (5, 2), (5, 12), (9, 2), (9, 12), (12, 5), (12, 9)]
    ]

with open('TableroAFacil.json', 'w') as arch:
    json.dump(facil, arch)

with open('TableroANormal.json', 'w') as arch:
    json.dump(normal, arch)

with open('TableroADificil.json', 'w') as arch:
    json.dump(dificil, arch)

    """inicio = int(time.time())#tiempo comienzo 
    current_time = datos['time']*60 + 1
        while True:
            if(datos['bolsa'].cantidad_Fichas() == 0):
                tablero["-comment-"].update(
                            "La bolsa no tiene mas fichas".format())
                Terminar(datos['atrilJ'].get_atril_array(),
                            datos['dif'], datos['puntosJ'],datos['puntosIA'], tablero, datos['atrilCPU'].get_atril_array())                
            if(turnoPC) and clock:
                tablero["-comment-"].update(("La CPU esta pensando").format())
                
                letras = CPU.CPUmain(datos['atrilCPU'].get_atril_array(), datos['pal'])
                
                if(len(letras)<1):
                    for i in datos['atrilCPU'].get_atril_array():
                        datos['atrilCPU'].usar(i)
                    datos['atrilCPU'].cambiar_Fichas(letras)
                    turnoPC = False
                    continue
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
                tablero["-comment-"].update(("La CPU suma " +
                                            str(punt) + " puntos").format())
                tablero['-pCPU-'].Update(('Puntos CPU: ' +
                                        str(datos['puntosIA'])).format())
                backT, datos['atrilCPU'] = modificarTablero(
                    tablero, backT, datos['atrilCPU'], letras, coor, False)
                turnoPC = False
                event = ''
                break
            clock = actualizarTimer(tablero,current_time,inicio)    
            event, _ = tablero.read(timeout=250)

            if event in (None, 'Exit') or not clock:
                if(event == 'Exit') or not clock:
                    Terminar(datos['atrilJ'].get_atril_array(),
                             datos['dif'], datos['puntosJ'],datos['puntosIA'], tablero, datos['atrilCPU'].get_atril_array())
                break
            # me fijo si el event es una de las posibles llaves de las letras y lo guardo en un auxiliar
            elif(event in claveA):
                aux = event
            # si ya elegi una letra solo entro al elegir st ya que en la primer jugada la letra va obligatoriamente en esa posicion
            elif event == (7, 7) and aux != "":
            # guardo en la lista de coordenadas
                listCoord.append(event)
                listLetra.append(datos['atrilJ'].get_atril_array()[
                           int(aux)])  # guardo en la lista de letras
                # deshabilito el boton y actualizo la casilla con la letra elegida
                tablero[event].update(
                        listLetra[-1], disabled=True, disabled_button_color=("#FCC300", "#E94E00"))
                # deshabilito la ficha del atril que el jugador coloco
                tablero[aux].update(disabled=True)
                aux = ""  # dejo libre para seleccionar otra letra
            # igual que el anterior, solo que evalua el que ya se haya ingresado una ficha en el st
            elif type(event) is tuple and len(listLetra) >= 1 and aux != "":
                listCoord.append(event)
                listLetra.append(
                    datos['atrilJ'].get_atril_array()[int(aux)])
                tablero[event].update(
                    listLetra[-1], disabled=True, disabled_button_color=("#FCC300", "#E94E00"))
                tablero[aux].update(disabled=True)
                aux = ""

            elif event == "-check-" and listCoord != []:
                # print("Algo")
                punt = puntos(datos['pal'], listCoord, listLetra, backT)
                if(punt <= 1):
                    if(punt == 1):
                        tablero["-comment-"].update(
                            "La palabra no es valida, pruebe una palabra distinta".format())
                    else:
                        tablero["-comment-"].update(
                            "Las fichas se colocaron erroneamente en el tablero,pruebe colocarlas una al lado de otra o una debajo de otra".format())

                    DevolverFichas(tablero, listCoord, backT)
                    ActualizarAtril(
                        tablero, datos['atrilJ'].get_atril_array())
                    listLetra = []
                    listCoord = []
                else:
                    datos['puntosJ'] += punt
                    tablero["-comment-"].update(
                        ("Sumaste " + str(punt) + " puntos").format())
                    tablero['-pJug-'].Update(('Tu puntaje: ' +
                                              str(datos['puntosJ'])).format())
                    backT, datos['atrilJ'] = modificarTablero(
                        tablero, backT, datos['atrilJ'], listLetra, listCoord)
                    print(datos['puntosJ'])
                    turnoPC = True
                    break
                # el jugador elije las fichas a cambiar
            elif event == '-cambiar-':
                DevolverFichas(tablero, listCoord, backT)
                if(datos['cambios'] > 0):
                    datos['atrilJ'], changed, clock = cambiar(
                        tablero, datos['atrilJ'] ,current_time ,inicio)
                    datos['cambios'] -= 1
                    if(datos['cambios'] == 0):
                        tablero['-cambiar-'].update("Pasar")    
                tablero['-comment-'].update(
                    'Ponga una ficha en ST para comenzar la partida'.format())
                tablero['-save-'].update(disabled=True)
                listLetra = []
                listCoord = []    
                if(changed) or datos['cambios'] == 0:
                    turnoPC = True               

                # le devuelvo las fichas al jugador si ya ingreso alguna
            elif event == "-back-" and listCoord != []:
                DevolverFichas(tablero, listCoord, backT)
                ActualizarAtril(
                    tablero, datos['atrilJ'].get_atril_array())
                listLetra = []
                listCoord = []            
        if(event != None):
            tablero['-save-'].update(disabled=False)
    """