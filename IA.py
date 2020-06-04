from validez import esValida

def CPUformarPalabra(letras):
    s=''
    for i in range(len(letras)):
        s+=letras[i]
    return s

def CPUverificar(letras):
    s=CPUformarPalabra(letras)
    if(esValida(s,'NN','VB','JJ')):
        print(s)
        return True
    else:
        return False


def CPUigual(*num):
    num = list(num)
    for i in range(len(num)-1):
        if num[i] in num[i+1:]:
            return False
    return True

def CPUarmar(l,*ind):
    s=[]
    for i in range(len(ind)):
        s+=[l[ind[i]]]
    return s

def CPUahhh(l,*ind):
    ind=list(ind)
    for i in range(len(l)):
        ind.append(i)
        if CPUigual(*ind):
            if(len(ind)>2):
                aux=CPUarmar(l,*ind)
                CPUverificar(aux)
        if(len(ind)<len(l)):
            CPUahhh(l,*ind)
        ind.pop(-1)
    pass

letras = ['o','o','o','o','k','o','k']
#print(letras[0:])
#print(CPUigual(*letras))
#print(CPUarmar(letras,1,4,5)
CPUahhh(letras)
