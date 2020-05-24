from pattern.text.es import parse,split,lexicon, spelling, tag

'''
print('hello word')
#//comienza el trabajo
#//hace el trabajo
#//termina el trabajo
print('done')
'''

#aqui empieza lo bueno

def esValida(palabra,*dif):
    palabra=parse(palabra).split('/')
    if palabra[1] in dif:
        if palabra[1] =='NN':
            if (not palabra[0] in spelling) or (not palabra[0] in lexicon):
                print('\n nono square',palabra[1],' \n')
                return False
        print('\n yes', palabra[1] ,'\n')
        return True
    print('\n nono square',palabra[1],' \n')
    return False
 

#main

#p=input()
p='saltare'

# VB:verbo   NN:sustantivo   JJ:adjetivo
dif=['NN','JJ','VB']
if(esValida(p,*dif)):
    print('calculo puntos')
else:
    print('retorno letras y que vuelva a su turno')



