from Funciones.Validez import esValida
from Funciones import Letras

def CPUdesarmar(ind,letras): #recibe las letras del atril y las pocisiones ordenadas para formar la palabra
    l=[]
    for i in ind:
        l.append(letras[i])
    return l

def CPUformarPalabra(letras): #junta la lista de caracteres en 1 solo string para luego comprobarla
    s=''
    for i in range(len(letras)):
        s+=letras[i]
    return s

def CPUverificar(letras,dif): #comprueba si la palabra es valida
    s=CPUformarPalabra(letras)
    if(esValida(s,*dif)):
        print('a',s)
        return True

    else:
        return False

def CPUigual(*num): #verifica si no hay numeros repetidos en la lista de indices
    num = list(num)
    for i in range(len(num)-1):
        if num[i] in num[i+1:]:
            return False
    return True

def CPUarmar(l,*ind): #arma la lista de caracteres utilizando los indices ordenados y la lista de letras a la cual los indices se refieren
    s=[]
    for i in range(len(ind)):
        s+=[l[ind[i]]]
    return s


''' funcion principal de la IA '''
'''esta funcion recibe la lista de letras del atril, los tipos de palabras que admite el programa (VB,NN o AJ), una verificacion
    de recursividad que por defecto es '' y una lista de indices que en un comienzo estan vacios
    lo que hace la funcion es tomar una lista de indices de a 1 y comprueba si existe una palabra de esa forma, por ej
    la funcion empezaria con 1 para en su 1er recursividad añadir el 2,(ya que el el "CPUigual" de la linea 53 le diria que 
    el 1 ya se encuentra en la lista) y en su siguiente recursividad añadiria el 3, etc para que al volver de la recursividad, la
    funcion empiece por el 2, añadiendo en su recursividad el 1 y luego el 3, etc mostrando todas las posibilidades de permutacion
    y para cada permutacion posible de indices/numeros, se comprobaria si existe una palabra posible con dicho orden'''
def CPUahhh(l,dif,word='',*ind): 
    ind=list(ind)
    if(word!=''): #verifico si ya se encontró una palabra
        return word
    for i in range(len(l)):
        ind.append(i)
        if CPUigual(*ind): #compruebo si el indice agregado no existia previamente en la lista
            if(len(ind)>=3): #palabras de tamaño minimo 3
                aux=CPUarmar(l,*ind) #armo la palabra en forma de string
                if(CPUverificar(aux,dif)): #comprueba si la palabra es valida
                    word=ind
                    return word
        if(len(ind)<len(l)): #si le quedan letras por analizar se llama a la recursividad
            word = CPUahhh(l,dif,word,*ind)
        ind.pop(-1) #elimino el ultimo indice agregado a la lista
    return word

def CPUmain(letras,dif): #main de la funcion que recibe el atril y el tipo de palabra valida (VB o NN por ej)
    pal= CPUahhh(letras,dif) #envia las letras del atril y el tipo de palabra valida y devuelve los indices de las letras en el atril y en que orden se deben tomar
    ''' print('palabra:',letras)
        print('indices: ', pal)
    '''#prints para testeos
    ind= CPUdesarmar(pal,letras) #crea la palabra reciviendo los indices y las letras
    return pal,ind #retorna la lista de caracteres (ordenados) que forman la palabra a colocar en el tablero



if __name__ == "__main__": #main para testeos
        
    letras = ['c','s','a','o']
    #print(letras[0:])
    #print(CPUigual(*letras))
    #print(CPUarmar(letras,1,4,5)
    print('resultado: ',CPUmain(letras,['NN', 'JJ', 'VB']))
