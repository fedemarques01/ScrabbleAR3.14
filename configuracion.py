import PySimpleGUI as ps
from Letras import Bolsa

abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
s=[]
for i in range(1,61):
    s.append(str(i))

def crearPantalla(config):
    global s
    layoutM = [
        [ps.T("Configureishon", size=(16, 1), justification="center", font=("Times New Roman", 16))],
        [ps.Text("Dificultad: "),ps.DropDown(("easy","medium","hard"),default_value=("medium"),size=(10,1))],
        [ps.Text("Tiempo de juego (en minutos): ", size=(22, 1)),ps.InputCombo((s),size=(5,1),default_value=(config['time']))],
        [ps.Button("modificar la bolsa (no lo hagas)", key=('-bag-'))],
        [ps.B("Guardar", size=(17, 1), key="-save"),ps.Exit("Volver", size=(10, 1), key="-exit")]
    ]

    window = ps.Window("ScrabbleAR - Menu", layoutM)

    return window

def laybag(bag):
    global abc
    global s
    print(bag)
    laybag=[[ps.Text("Seleccione la cantidad de letras para cada letra")]]
    try:
        for fila in range(0,len(abc),5):
            laybag += [[ps.Text(abc[i+fila],size=(4,0))for i in range(len(abc)//5)]]
            laybag += [[ps.InputCombo(s,default_value=(5),size=(3,0))for i in range(len(abc)//5)]]
    except IndexError:
        laybag += [[ps.T(i,size=(4,0))for i in abc[-2:]]]
        laybag += [[ps.InputCombo(s,default_value=(5),size=(3,0))for i in abc[-2:]]]
    finally:
        laybag += [[ps.B('Guardar',key=('-save-')),ps.B('Volver',key=('Exit'))]]
    winbag = ps.Window("Modificar Bolsa", laybag)
    return winbag

def dific(dific,time):
    time=int(time)
    if dific in('easy','medium','hard'):
        return dific,time
    return None,time

def modBolsa(bag):
    winbag =laybag(bag)
    while True:
        e,v = winbag.read()
        print(e)
        if e in ('Exit',None):
            break
        elif e =='-save-':
            print('no quiero hacer esto')
    winbag.Close()
    return bag

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
                    ps.popup("ingrese valores validos")
                    continue
            except ValueError:
                ps.popup("ingrese valores validos")
            else:
                config['dif']=d
                config['time']=time
        elif eve == '-bag-':
            config['bolsa']= modBolsa(config['bolsa'])
        elif eve in (None, "-exit"):
            break
    menuC.close()
    return config

if __name__ == "__main__":
    ajustes(config={'dif':'medium','puntosJ':0,'puntosIA':0,'time':10,'pal':[],'bolsa':[]})