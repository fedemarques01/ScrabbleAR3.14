import PySimpleGUI as sg

def crearPantalla(config):
    s=[]
    for i in range(1,61):
        s.append(str(i))
    layoutM = [
        [sg.T("Configureishon", size=(16, 1), justification="center", font=("Times New Roman", 16))],
        [sg.Text("Dificultad: "),sg.DropDown(("easy","medium","hard"),default_value=("medium"),size=(10,1))],
        [sg.Text("Tiempo de juego (en minutos): ", size=(22, 1)),sg.InputCombo((s),size=(5,1),default_value=(config['time']))],
         [sg.B("Guardar", size=(17, 1), key="-save"),sg.Exit("Volver", size=(10, 1), key="-exit")]
    ]

    window = sg.Window("ScrabbleAR - Menu", layoutM)

    return window

def dific(dific,time):
    time=int(time)
    if dific in('easy','medium','hard'):
        return dific,time
    return None,time

def ajustes(config):
    menuC = crearPantalla(config)
    while True:
        #print(config,'\n')
        eve, val = menuC.read()
        #print(val)
        if eve in ("-save-"):
            try:
                d,time=dific(val[0],val[1])
                if(d==None):
                    sg.popup("ingrese valores validos")
                    continue
            except ValueError:
                sg.popup("ingrese valores validos")
            else:
                config['dif']=d
                config['time']=time
        elif eve in (None, "-exit"):
            break
    menuC.close()
    return config

if __name__ == "__main__":
    ajustes(config={'dif':'medium','puntosJ':0,'puntosIA':0,'time':10,'pal':[]})