
def igual(*num):
    num = list(num)
    for i in range(len(num)-1):
        if num[i] in num[i+1:]:
            return False
    return True

def armar(l,*ind):
    s=[]
    for i in range(len(ind)):
        s+=[l[ind[i]]]
    return s

def ahhh(l,*ind):
    ind=list(ind)
    for i in range(len(l)):
        ind.append(i)
        if igual(*ind):
            aux=armar(l,*ind)
            print(aux)
        if(len(ind)<len(l)):
            ahhh(l,*ind)
        ind.pop(-1)
    pass

letras = ['a','b','c','d']
# print(letras[0:])
#print(igual(*letras))
#print(armar(letras,1,4,5))
ahhh(letras)




'''
for i in range(len(letras)):
    for j in range(len(letras)):
        if i != j:
            print(i, j)

        for k in range(len(letras)):
            if igual(i,j,k):
                print(i, j, k)

            for l in range(len(letras)):
                if igual(i,j,k,l):
                    print(i, j, k, l)

                for m in range(len(letras)):
                    if igual(i,j,k,l, m):
                        print(i, j, k, l, m)

                    for n in range(len(letras)):
                        if igual(i, j, k, l, m, n):
                            print(i, j, k, l, m, n)

                        for o in range(len(letras)):
                            if igual(i, j, k, l, m, n, o):
                                print(i, j, k, l, m, n, o)
'''
