letras = ['o','o','o','o','k','o','k']
#print(letras[0:])
#print(CPUigual(*letras))
#print(CPUarmar(letras,1,4,5)

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
