from Validez import esValida
import Letras

def CPUdesarmar(ind,letras):
    l=[]
    for i in ind:
        l.append(letras[i])
    return l

def meJodeQueSeaUnObjeto(atr):
    lis=[]
    for i in range(len(atr)):
        lis.append(atr[i].get_letra())

    return lis

def CPUformarPalabra(letras):
    s=''
    for i in range(len(letras)):
        s+=letras[i]
    return s

def CPUverificar(letras):
    s=CPUformarPalabra(letras)
    if(esValida(s,'NN','VB','JJ')):
        print('a',s)
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

def CPUahhh(l,word='',*ind):
    ind=list(ind)
    if(word!=''):
        return word
    for i in range(len(l)):
        ind.append(i)
        if CPUigual(*ind):
            if(len(ind)>2):
                aux=CPUarmar(l,*ind)
                if(CPUverificar(aux)):
                    word=ind
                    return word
        if(len(ind)<len(l)):
            word = CPUahhh(l,word,*ind)
        ind.pop(-1)
    return word

def CPUmain(cosa):
    letras=meJodeQueSeaUnObjeto(cosa)
    word= CPUahhh(letras)
    #print('indices: ', word)
    word= CPUdesarmar(word,letras)
    return word



if __name__ == "__main__":
        
    letras = ['c','s','a','o']
    #print(letras[0:])
    #print(CPUigual(*letras))
    #print(CPUarmar(letras,1,4,5)
    print('resultado: ',CPUmain(letras))
