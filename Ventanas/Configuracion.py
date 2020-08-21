import PySimpleGUI as ps
from Funciones import Letras
from Funciones.Letras import Bolsa
from random import randint, random

abc=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Z','Y']
s=[]
for i in range(1,61):
    s.append(str(i))

def crearPantalla(config): #crea la pantalla principal de configuración
    global s
    layoutM = [
        [ps.T("Configureishon", size=(20, 1), justification="center", font=("Times New Roman", 16))],
        [ps.Text("Dificultad: "),ps.DropDown(("Easy","Medium","Hard"),default_value=("Medium"),size=(10,1))],
        [ps.Text("Tiempo de juego (en minutos): ", size=(22, 1)),ps.InputCombo((s),size=(5,1),default_value=(config['time']))],
        [ps.Button("Modificar la bolsa", key=('-bag-'),size=(29,1))],
        [ps.B("Guardar", size=(17, 1), key="-save"),ps.Exit("Volver", size=(10, 1), key="-exit")]
    ]
    window = ps.Window("ScrabbleAR - Menu", layoutM)

    return window

def verif(dific,time): #verifica si la dificultad y el tiempo son validos
    time=int(time)
    if dific in('Easy','Medium','Hard'):
        return dific,time
    return None,time

#La creacion de la intefaz y los procesos necesarios para modificar la bolsa
def modBolsa():
    layout = [
        [ps.Text("Letra a añadir: ",size=(27,1)),ps.InputText(size=(3,1))],
        [ps.Text("Cantidad de fichas de esa letra(1-15): ",size=(27,1)),ps.InputText(size=(3,1))],
        [ps.Text("Puntaje de esa ficha(1-12): ",size=(27,1)),ps.InputText(size=(3,1))],
        [ps.Button("Añadir",size=(14,1)),
        ps.Button("Guardar y salir",size=(14,1),key='-save-'),
        ps.B("Salir sin guardar",size=(14,1),key='-Exit-')]
        ]
    window = ps.Window("Ingresamelo todo Lince",layout,finalize=True)
    lista = []
    while True:
        event, values = window.read()
        print('a',values)
        
        if event == 'Añadir':
            aux = list(values.values())
            if '' in aux:#que pasa si deja un campo vacio
                ps.popup('Complete todos los campos')
                continue
            aux[0] = aux[0].upper()
            try:#Esto cubre que se ingresen numeros en los puntajes y cantidad de las fichas
                aux[1] = int(aux[1])
                aux[2] = int(aux[2])
            except Exception:
                ps.popup('Los campos del puntaje y la cantidad deben tener solo numeros')
                continue
            if aux[0] not in abc:#se revisa que la letra sea acorde al Scrabble
                ps.popup('La letra no es valida, ingrese otra')
                continue
            elif aux[1] not in range(1,16):#se revisa que la cantidad este dentro de los terminos
                ps.popup('Por favor ingrese una cantidad entre 1 y 15')
                continue
            elif aux[2] not in range(1,13):#se revisa que el puntaje este dentro de los terminos
                ps.popup('Por favor ingrese un puntaje entre 1 y 12')
                continue
            print('paso')
            lista.append(aux)
            window[0].update('')
            window[1].update('')
            window[2].update('')
        elif event == '-save-':
            ps.popup('se guardaron los cambios')
            break                    
        elif event in(None,'-Exit-'):
            if(event == '-Exit-'):
                event2, _ = ps.Window('ADVERTENCIA',
                [[ps.T('No se guardaran los cambios realizados a la bolsa, ¿continuar de todas formas?')],
                [ps.B('OK'), ps.B('Cancel') ]]).read(close=True)
                if event2 == 'Cancel':
                    continue
            lista = []    
            break
        
    window.close()
    return lista

def aplicarCambios(bolsa,lista):
    dic = Letras.valoresLetras
    for aux in lista:
        bolsa.quitar_bolsa(aux[0])        #retiro la letra de la bolsa
        bolsa.agregar_bolsa(aux[0],aux[1])#añado la cantidad indicada por el jugador
        dic[aux[0]] = aux[2]              #le asigno el valor que eligio el jugador
    bolsa.mezclar_bolsa()
    return bolsa,dic

def ajustes(config): #main de configuraciones
    menuC = crearPantalla(config)
    lista = []
    while True:
        #print(config,'\n')
        eve, val = menuC.read()
        #print(val)
        if eve == "-save": #en caso de seleccionar "guardar" se verifica que los valores sean validos
            try:
                d,time=verif(val[0],val[1]) #verificador de dificultad y timer
                print(d,config['dif'],time,config['time'])
                if(d==None): #en caso de no ser validos
                    ps.popup("ingrese valores validos") 
                    continue
            except ValueError: #en caso de no ser validos
                ps.popup("ingrese valores validos")
            else:
                config['dif']=d
                config['time']=time
                ps.popup('se guardaron los cambios')
        elif eve == '-bag-': #en caso de seleccionar el modificar bolsa se abre la ventana para modificar la bolsa
            lista = modBolsa()
        elif eve in (None, "-exit"):
            break
    menuC.close()
    config['bolsa']= Bolsa(config['dif']) 
    if lista != []: 
        config['bolsa'],config['letrasP'] = aplicarCambios(config['bolsa'],lista) 
    return config

if __name__ == "__main__":
    #baga=Bolsa('medium')
    baga=[]
    config={'dif':'Medium','puntosJ':0,'puntosIA':0,'time':10,'pal':[],'bolsa':baga}
    ajustes(config)
    print(config['bolsa'])

