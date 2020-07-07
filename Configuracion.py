import PySimpleGUI as ps
from Letras import Bolsa
from random import randint, random

abc=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Z','Y']
s=[]
for i in range(1,21):
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

def laybag(bag):#en los "default_values" deberian ir los datos de la bolsa por defecto
    global abc
    global s
    print(bag)
    laybag=[[ps.Text("Seleccione la cantidad de letras para cada letra")]]
    try:
        for fila in range(0,len(abc),5):
            laybag += [[ps.Text(abc[i+fila],size=(4,0))for i in range(len(abc)//5)]]
            laybag += [[ps.InputCombo(s,default_value=(randint(1,10)),size=(3,0),key=(abc[i+fila]))for i in range(len(abc)//5)]]
    except IndexError:
        laybag += [[ps.T(i,size=(4,0))for i in abc[-2:]]]
        laybag += [[ps.InputCombo(s,default_value=(randint(1,10)),size=(3,0),key=(i))for i in abc[-2:]]]
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
    print(bag.get_bolsa())
    winbag =laybag(bag)
    while True:
        e,v = winbag.read()
        if e in ('Exit',None):
            break
        elif e =='-save-':
            print('no quiero hacer esto')
            bag = Bolsa()
            k=list(v.items())
            for i in range(len(k)):
                print(k[i][0],k[i][1])
                bag.agregar_bolsa(k[i][0],int(k[i][1]))
            bag.mezclar_bolsa()
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
            if(config['bolsa']==[]):
                config['bolsa']=Bolsa(config['dif'])
            config['bolsa']= modBolsa(config['bolsa'])
        elif eve in (None, "-exit"):
            break
    menuC.close()
    return config

if __name__ == "__main__":
    #baga=Bolsa('medium')
    baga=[]
    config={'dif':'medium','puntosJ':0,'puntosIA':0,'time':10,'pal':[],'bolsa':baga}
    ajustes(config)
    print(config['bolsa'])

