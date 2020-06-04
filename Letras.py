import random

valoresLetras= {"A": 1,
                 "B": 3,
                 "C": 3,
                 "CH":5,
                 "D": 2,
                 "E": 1,
                 "F": 4,
                 "G": 2,
                 "H": 4,
                 "I": 1,
                 "J": 8,
                 "L": 1,
                 "LL":8,
                 "M": 3,
                 "N": 1,
                 "Ñ": 8,
                 "O": 1,
                 "P": 3,
                 "Q": 5,
                 "R": 1,
                 "RR":8,
                 "S": 1,
                 "T": 1,
                 "U": 1,
                 "V": 4,
                 "X": 8,
                 "Y": 4,
                 "Z": 10,
                 "#": 0}  



def get_valor(letra,valoresLetras):
        
    return valoresLetras[letra]

class Bolsa:

     def __init__(self, nivel):
       
         self.bolsa = []
         self.dificultad = ['easy', 'medium', 'hard']
         self.initialize_bolsa(nivel)

<<<<<<< HEAD
     def agregar_bolsa(self, letra, cantidad):
         mayus = letra.upper()
         for i in range(cantidad):
             self.bolsa.append(mayus)
=======
     def agregar_bolsa(self, ficha, cantidad):
        
         for _ in range(cantidad):
             self.bolsa.append(ficha)
>>>>>>> facfc2e366250c8de4a53cc19ce5459ab7785c6e

     def initialize_bolsa(self,nivel):
               
         if nivel == self.dificultad[0]:        
             #bolsa nivel facil, distribucion  clasica del scrabble en espa;ol
             self.agregar_bolsa("A", 12)
             self.agregar_bolsa("B", 2)
             self.agregar_bolsa("C", 4)
             #self.agregar_bolsa("CH", 1)
             self.agregar_bolsa("D", 5)
             self.agregar_bolsa("E", 12)
             self.agregar_bolsa("F", 1)
             self.agregar_bolsa("G", 2)
             self.agregar_bolsa("H", 2)
             self.agregar_bolsa("I", 6)
             self.agregar_bolsa("J", 1)       
             self.agregar_bolsa("L", 4)
             #self.agregar_bolsa("LL", 1)
             self.agregar_bolsa("M", 2)
             self.agregar_bolsa("N", 5)
             self.agregar_bolsa("Ñ", 1)
             self.agregar_bolsa("O", 9)
             self.agregar_bolsa("P", 2)
             self.agregar_bolsa("Q", 1)
             self.agregar_bolsa("R", 5)
            # self.agregar_bolsa("RR", 1)
             self.agregar_bolsa("S", 6)
             self.agregar_bolsa("T", 4)
             self.agregar_bolsa("U", 5)
             self.agregar_bolsa("V", 1)
             self.agregar_bolsa("X", 1)
             self.agregar_bolsa("Y", 1)
             self.agregar_bolsa("Z", 1)
            # self.agregar_bolsa("#", 2)

         if nivel == self.dificultad[1]:        
             #bolsa nivel media, se disminuyen algunas vocales y se reducen las consonantes de 1 y 2 puntos
             self.agregar_bolsa("A", 10)
             self.agregar_bolsa("B", 2)
             self.agregar_bolsa("C", 4)
             #self.agregar_bolsa("CH", 1)
             self.agregar_bolsa("D", 3)
             self.agregar_bolsa("E", 10)
             self.agregar_bolsa("F", 1)
             self.agregar_bolsa("G", 2)
             self.agregar_bolsa("H", 2)
             self.agregar_bolsa("I", 6)
             self.agregar_bolsa("J", 1)       
             self.agregar_bolsa("L", 2)
             #self.agregar_bolsa("LL", 1)
             self.agregar_bolsa("M", 2)
             self.agregar_bolsa("N", 4)
             self.agregar_bolsa("Ñ", 1)
             self.agregar_bolsa("O", 8)
             self.agregar_bolsa("P", 2)
             self.agregar_bolsa("Q", 1)
             self.agregar_bolsa("R", 4)
             #self.agregar_bolsa("RR", 1)
             self.agregar_bolsa("S", 4)
             self.agregar_bolsa("T", 2)
             self.agregar_bolsa("U", 4)
             self.agregar_bolsa("V", 1)
             self.agregar_bolsa("X", 1)
             self.agregar_bolsa("Y", 1)
             self.agregar_bolsa("Z", 1)
             #self.agregar_bolsa("#", 2)

         if nivel == self.dificultad[2]:        
             #bolsa nivel dificil, se disminuyen aun mas las vocales
             self.agregar_bolsa("A", 8)
             self.agregar_bolsa("B", 2)
             self.agregar_bolsa("C", 4)
             #self.agregar_bolsa("CH", 1)
             self.agregar_bolsa("D", 3)
             self.agregar_bolsa("E", 7)
             self.agregar_bolsa("F", 1)
             self.agregar_bolsa("G", 2)
             self.agregar_bolsa("H", 2)
             self.agregar_bolsa("I", 4)
             self.agregar_bolsa("J", 1)       
             self.agregar_bolsa("L", 2)
             #self.agregar_bolsa("LL", 1)
             self.agregar_bolsa("M", 2)
             self.agregar_bolsa("N", 4)
             self.agregar_bolsa("Ñ", 1)
             self.agregar_bolsa("O", 6)
             self.agregar_bolsa("P", 2)
             self.agregar_bolsa("Q", 1)
             self.agregar_bolsa("R", 4)
             #self.agregar_bolsa("RR", 1)
             self.agregar_bolsa("S", 4)
             self.agregar_bolsa("T", 2)
             self.agregar_bolsa("U", 3)
             self.agregar_bolsa("V", 1)
             self.agregar_bolsa("X", 1)
             self.agregar_bolsa("Y", 1)
             self.agregar_bolsa("Z", 1)
             #self.agregar_bolsa("#", 2)
         random.shuffle(self.bolsa)

     def tomar_bolsa(self):
         #Toma la primera de la bolsa y la elimina de la misma. Se usa para cambiars o la recarga del atril (con un ciclo)
         return self.bolsa.pop()

     def cantidad_Fichas(self):
         #Retorna la cantidad des restantes
         return len(self.bolsa)

class Atril:
    """
    
    """
    def __init__(self, bolsa):
       
        self.atril = []
        self.bolsa = bolsa
        self.initialize()



    def initialize(self):
        
<<<<<<< HEAD
        for i in range(7):
            self.agregar_al_atril()
=======
         for _ in range(7):
             self.agregar_al_atril()
>>>>>>> facfc2e366250c8de4a53cc19ce5459ab7785c6e


    def agregar_al_atril(self):
       
        self.atril.append(self.bolsa.tomar_bolsa())


    def get_atril_string(self):
        #Devuelve el atril en forma de string
        return ", ".join(str(item) for item in self.atril)

    def get_atril_array(self):
        #Devuelve el atril
        return self.atril

<<<<<<< HEAD
    def usar(self,letra):
        #Quita la del atril, para ser cambiada o jugada
        self.atril.remove(letra)
=======
    def usar_ficha(self, ficha):
        #Quita la ficha del atril, para ser cambiada o jugada
        for i in self.atril:
            if(i.get_letra() == ficha):
                print(i.get_letra())
                print (i)
                self.atril.remove(i)
                break
>>>>>>> facfc2e366250c8de4a53cc19ce5459ab7785c6e

    def get_atril_espaciosVacios(self):
        #Cantidad des que faltan en el atril
        return 7 - len(self.atril)

    def get_atril_tamanio(self):
        #Cantidad des en el atril
        return len(self.atril)

    def rellenar_atril(self):
        #
        while self.get_atril_espaciosVacios() > 0 and self.bolsa.cantidad_Fichas() > 0:
            self.agregar_al_atril()

#Codigo de prueba, genera una bolsa segun la dificultad dada en el constructor, imprime lass disponibles y cantidad total des 
# de la bolsa. 
if __name__ == "__main__":
    bolsa1 = Bolsa('facil')
    fichasTotales = bolsa1.cantidad_fichas()

    for i in range(fichasTotales):
        print(bolsa1.bolsa[i].letra)
    print('Total de fichas del nivel: facil ')
    print(bolsa1.cantidad_fichas())

<<<<<<< HEAD
bolsa1 = Bolsa('facil')
fichasTotales = bolsa1.cantidad_Fichas()

for i in range (fichasTotales):
    print(bolsa1.bolsa[i])
print('Total fichas del nivel: facil ')
print(bolsa1.cantidad_Fichas())
=======

    #Crea el atril del jugador y lo muestra en pantalla
    atril1 = Atril(bolsa1)
>>>>>>> facfc2e366250c8de4a53cc19ce5459ab7785c6e

    atril_jugador =  atril1.get_atril_string()
    print('Atril del jugador')
    print(atril_jugador)

<<<<<<< HEAD
#Crea el atril del jugador y lo muestra en pantalla
atril1 = Atril(bolsa1)
atril2 = Atril(bolsa1)
=======
    #fichas en la bolsa luego de crear el primer atril
    print('Fichas restantes')
    print(bolsa1.cantidad_fichas())
>>>>>>> facfc2e366250c8de4a53cc19ce5459ab7785c6e

    #Se simula una jugada, pidiendo que se escriba una palabra
    # (no hay verificacion alguna, se asume que se usaran letras del atril y que toda palabra es valida)

<<<<<<< HEAD
atril_cpu =  atril2.get_atril_string()
print('Atril del cpu')
print(atril_cpu)

#fichas en la bolsa luego de crear los 2 atriles
print('cantidad Fichas restantes')
print(bolsa1.cantidad_Fichas())
=======
    print('Escriba una palabra a jugar, finalice con enter')
>>>>>>> facfc2e366250c8de4a53cc19ce5459ab7785c6e

    palabra = input()

    #Se verifcan las letras y se eliminan del atril del jugador
    jugada = []
    for letra in palabra:
        letra= letra.upper()
        encontre = False
        i = 0
        arreglo = atril1.get_atril_array()
        while (encontre == False):
            if letra == arreglo[i].letra:
                encontre = True
                atril1.usar_ficha(arreglo[i])
            else:
                i=i+1

<<<<<<< HEAD
palabra = input()

#Se verifcan las letras y se eliminan del atril del jugador
jugada = []
for letra in palabra:
    encontre = False
    i = 0
    arreglo = atril1.get_atril_array()
    while (encontre == False):
        if letra == arreglo[i]:
            encontre = True
            atril1.usar(arreglo[i])
        else:
            i=i+1

#Atril del jugador luego de la jugada 
atril_jugador =  atril1.get_atril_string()
print('Atril del jugador luego de jugar')
print(atril_jugador)


#Se recargans y se muestra el atril nuevo y 
# la cantidad des en la bolsa luego de todo el proceso
atril1.rellenar_atril()
=======
    #Atril del jugador luego de la jugada 
    atril_jugador =  atril1.get_atril_string()
    print('Atril del jugador luego de jugar')
    print(atril_jugador)


    #Se recargan fichas y se muestra el atril nuevo y 
    # la cantidad de fichas en la bolsa luego de todo el proceso
    atril1.rellenar_atril()
>>>>>>> facfc2e366250c8de4a53cc19ce5459ab7785c6e

    atril_jugador =  atril1.get_atril_string()
    print('Atril del jugador luego de recargar')
    print(atril_jugador)

<<<<<<< HEAD
print('fichas restantes luego de recargar')
print(bolsa1.cantidad_Fichas())
=======
    print('Fichas restantes luego de recargar')
    print(bolsa1.cantidad_fichas())
>>>>>>> facfc2e366250c8de4a53cc19ce5459ab7785c6e




