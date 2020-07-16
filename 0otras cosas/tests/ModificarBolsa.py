import PySimpleGUI as ps

abc=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Z','Y']
s=[]
for i in range(1,21):
    s.append(str(i))

def dific(dific,time):
    time=int(time)
    if dific in('Easy','Medium','Hard'):
        return dific,time
    return None,time

def crearPantalla(config):
    global s
    layoutM = [
        [ps.T("Configureishon", size=(16, 1), justification="center", font=("Times New Roman", 16))],
        [ps.Text("Dificultad: "),ps.DropDown(("Easy","Medium","Hard"),default_value=("Medium"),size=(10,1))],
        [ps.Text("Tiempo de juego (en minutos): ", size=(22, 1)),ps.InputCombo((s),size=(5,1),default_value=(config['time']))],
        [ps.Button("Modificar la bolsa", key=('-bag-'))],
        [ps.B("Guardar", size=(17, 1), key="-save"),ps.Exit("Volver", size=(10, 1), key="-exit")]
    ]
    window = ps.Window("ScrabbleAR - Menu", layoutM)

    return window

def modBolsa():
    layout = [
        [ps.Text("Letra a añadir: ",size=(20,1)),ps.InputText()],
        [ps.Text("Cantidad de fichas de esa letra: ",size=(20,1)),ps.InputText()],
        [ps.Text("Puntaje de esa ficha: ",size=(20,1)),ps.InputText()],
        [ps.Button("Añadir",size=(8,1)),
        ps.Button("Guardar y salir",size=(8,1),key='-save-'),
        ps.B("Salir sin guardar",size=(8,1),key='-Exit-')]
        ]
    window = ps.Window("Ingresamelo todo Lince",layout)
    lista = []
    while True:
        event, values = window.read()
        print(values)
        window[0].update('')
        window[1].update('')
        window[2].update('')

        if event == 'Añadir':
            aux = list(values.values())
            if '' in aux:
                ps.popup('Complete todos los campos')
                continue
            aux[0] = aux[0].upper()
            try:
                aux[1] = int(aux[1])
                aux[2] = int(aux[2])
            except Exception:
                ps.popup('Los campos del puntaje y la cantidad deben tener solo numeros')
                continue
            if aux[0] not in abc:
                ps.popup('La letra no es valida, ingrese otra')
                continue
            elif aux[1] not in range(1,11):
                ps.popup('Por favor ingrese una cantidad entre 1 y 10')
                continue
            elif aux[2] not in range(1,11):
                ps.popup('Por favor ingrese un puntaje entre 1 y 10')
                continue
            lista.append(aux)
        elif event == '-save-':
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
        bolsa.quitar_letra(aux[0])#retiro la letra de la bolsa
        bolsa.agregar_bolsa(aux[0],aux[1])#añado la cantidad indicada por el jugador
        dic[aux[0]] = aux[2]#le asigno el valor que eligio el jugador
    bolsa.mezclar_bolsa()
    return bolsa,dic

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
                    ps.popup("Ingrese valores validos")
                    continue
            except ValueError:
                ps.popup("Ingrese valores validos")
            else:
                config['dif']=d
                config['time']=time
        elif eve == '-bag-':
            lista = modBolsa()
        elif eve in (None, "-exit"):
            break
    config['bolsa']= Bolsa(config['dif'])
    config['bolsa'],config['letrasP'] = aplicarCambios(config['bolsa'],lista)    
    menuC.close()
    return config

if __name__ == "__main__":
    #baga=Bolsa('medium')
    baga=[]
    config={'dif':'Medium','puntosJ':0,'puntosIA':0,'time':10,'pal':[],'bolsa':baga}
    ajustes(config)
    print(config['bolsa'])