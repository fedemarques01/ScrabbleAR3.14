from pattern.text.es import parse, split, lexicon, spelling
import PySimpleGUI as p

# aqui empieza lo bueno
def lineal(coor, n):
    x = coor[0][n]
    for i in range(1, len(coor)):
        if(coor[i][n] != x):
            return False
    return True

def tieneOrden(dic):
    coor=[]
    for c in dic.keys():
        coor.append(c)
    #print(coor,'\n')
    if(lineal(coor, 0)):
        return sorted(dic.items(), key=lambda cor: cor[0][1])
    if(lineal(coor, 1)):
        return sorted(dic.items(), key=lambda cor: cor[0][0])
    return []


def esValida(palabra, *dif):
    palabra = parse(palabra).split('/')
    if palabra[1] in dif:
        if palabra[1] == 'NN':
            if (not palabra[0] in spelling) and (not palabra[0] in lexicon):
                #print('nono square'+ palabra[1])
                return False
        #print('existe'+ palabra[1])
        return True
    return False

def formarPalabra(dic):
    #buscar si se puede evitar el orden post lambda siguiente ordenando una lista de 
    # valores en base a las claves del diccionario <-----------------------------------
    s=''
    for i in range(len(dic)):
        s+=dic[i][1]
    return s

def validez(dif,coor,letras):
    aux={}
    for i in range(len(coor)):
        aux[coor[i]]=letras[i]

    #verifico si todas las letras estan en una fila/columna y las ordeno
    aux = tieneOrden(aux)
    if aux==[]:
        p.popup('No posee orden')
        return -100

    #armo la palabra con las letras ordenadas
    palabra = formarPalabra(aux)
    palabra = palabra.lower()
    
    #verifico si la palabra existe
    #palabra=input()
    if(esValida(palabra, *dif)):
        return 2
    else:
        p.popup('No existe')
        return -200



# main
if __name__ == "__main__":
   
    dif = ['NN', 'JJ', 'VB']  #<----- VB:verbo   NN:sustantivo   JJ:adjetivo
    coor = [(3, 0), (4, 0), (0, 0), (1, 0)]
    letras = ['M','A','G','O']

    print('\n')
    v=validez(dif,coor,letras)
    print(v)
    if(v>1):
        print('todo done, master')
    else:
        print('no no square')
