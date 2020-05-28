from pattern.text.es import parse, split, lexicon, spelling

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
    return {}


def esValida(palabra, *dif):
    palabra = parse(palabra).split('/')
    if palabra[1] in dif:
        if palabra[1] == 'NN':
            if (not palabra[0] in spelling) or (not palabra[0] in lexicon):
                print('\n nono square', palabra[1], ' \n')
                return False
        print('\n existe', palabra[1], '\n')
        return True
    print('\n nono existe', palabra[1], ' \n')
    return False

def formarPalabra(dic):
    #buscar si se puede evitar el orden post lambda siguiente ordenando una lista de 
    # valores en base a las claves del diccionario <-----------------------------------
    s=''
    for i in range(len(coor)):
        s+=aux[i][1]
    return s

def validez(dif,coor,letras):
    aux={}
    for i in range(len(coor)):
        aux[coor[i]]=letras[i]

    #verifico si todas las letras estan en una fila/columna y las ordeno
    aux = tieneOrden(aux)
    if aux=={}:
        print('no posee orden')
        return False

    #armo la palabra con las letras ordenadas
    palabra = formarPalabra(aux)
    palabra = palabra.lower()
    
    #verifico si la palabra existe
    #palabra=input()
    if(esValida(palabra, *dif)):
        return True
    else:
        print('no existe')
        return False



# main
if __name__ == "__main__":
   
    dif = ['NN', 'JJ', 'VB']  #<----- VB:verbo   NN:sustantivo   JJ:adjetivo
    coor = [(0, 0), (3, 0), (4, 0), (2, 0),(5, 0)]
    letras = ['P','R','R','E','O']

    print('\n')
    if(validez(dif,coor,letras)):
        print('\n','todo done, master')
    else:
        print('\n','no no square')
