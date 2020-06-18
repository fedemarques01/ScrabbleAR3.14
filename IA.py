from Validez import esValida
import Letras

def CPUdesarmar(ind,letras):
    l=[]
    for i in ind:
        l.append(letras[i])
    return l


def CPUformarPalabra(letras):
    s=''
    for i in range(len(letras)):
        s+=letras[i]
    return s

def CPUverificar(letras,dif):
    s=CPUformarPalabra(letras)
    if(esValida(s,*dif)):
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

def CPUahhh(l,dif,word='',*ind):
    ind=list(ind)
    if(word!=''):
        return word
    for i in range(len(l)):
        ind.append(i)
        if CPUigual(*ind):
            if(len(ind)>1):
                aux=CPUarmar(l,*ind)
                if(CPUverificar(aux,dif)):
                    word=ind
                    return word
        if(len(ind)<len(l)):
            word = CPUahhh(l,dif,word,*ind)
        ind.pop(-1)
    return word

def CPUmain(letras,dif):
    ind= CPUahhh(letras,dif)
    print('indices: ', ind)
    ind= CPUdesarmar(ind,letras)
    print('palabra:',letras)
    return ind



if __name__ == "__main__":
        
    letras = ['c','s','a','o']
    #print(letras[0:])
    #print(CPUigual(*letras))
    #print(CPUarmar(letras,1,4,5)
    print('resultado: ',CPUmain(letras,['NN', 'JJ', 'VB']))
