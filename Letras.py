import random

valoresLetras = {"A": 1,
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

class Ficha:
    """
    Clase que crea una ficha. Asigna a una ficha una letra y la referencia a su valor en el diccionario valoresLetras
    """
    def __init__(self, letra, valoresLetras):
        
        self.letra = letra.upper()
        if self.letra in valoresLetras:
            self.valor = valoresLetras[self.letra]
        else:
            self.valor = 0

    def get_letra(self):
        
        return self.letra

    def get_valor(self):
        
        return self.valor

class Bolsa:

     def __init__(self, nivel):
       
         self.bolsa = []
         self.dificultad = ['facil', 'media', 'dificil']
         self.initialize_bolsa(nivel)

     def agregar_bolsa(self, ficha, cantidad):
        
         for i in range(cantidad):
             self.bolsa.append(ficha)

     def initialize_bolsa(self,nivel):
         global valoresLetras
         if nivel == self.dificultad[0]:        
             #bolsa de fichas nivel facil, distribucion de fichas clasica del scrabble en espa;ol
             self.agregar_bolsa(Ficha("A", valoresLetras), 12)
             self.agregar_bolsa(Ficha("B", valoresLetras), 2)
             self.agregar_bolsa(Ficha("C", valoresLetras), 4)
             #self.agregar_bolsa(Ficha("CH", valoresLetras), 1)
             self.agregar_bolsa(Ficha("D", valoresLetras), 5)
             self.agregar_bolsa(Ficha("E", valoresLetras), 12)
             self.agregar_bolsa(Ficha("F", valoresLetras), 1)
             self.agregar_bolsa(Ficha("G", valoresLetras), 2)
             self.agregar_bolsa(Ficha("H", valoresLetras), 2)
             self.agregar_bolsa(Ficha("I", valoresLetras), 6)
             self.agregar_bolsa(Ficha("J", valoresLetras), 1)       
             self.agregar_bolsa(Ficha("L", valoresLetras), 4)
             #self.agregar_bolsa(Ficha("LL", valoresLetras), 1)
             self.agregar_bolsa(Ficha("M", valoresLetras), 2)
             self.agregar_bolsa(Ficha("N", valoresLetras), 5)
             self.agregar_bolsa(Ficha("Ñ", valoresLetras), 1)
             self.agregar_bolsa(Ficha("O", valoresLetras), 9)
             self.agregar_bolsa(Ficha("P", valoresLetras), 2)
             self.agregar_bolsa(Ficha("Q", valoresLetras), 1)
             self.agregar_bolsa(Ficha("R", valoresLetras), 5)
            # self.agregar_bolsa(Ficha("RR", valoresLetras), 1)
             self.agregar_bolsa(Ficha("S", valoresLetras), 6)
             self.agregar_bolsa(Ficha("T", valoresLetras), 4)
             self.agregar_bolsa(Ficha("U", valoresLetras), 5)
             self.agregar_bolsa(Ficha("V", valoresLetras), 1)
             self.agregar_bolsa(Ficha("X", valoresLetras), 1)
             self.agregar_bolsa(Ficha("Y", valoresLetras), 1)
             self.agregar_bolsa(Ficha("Z", valoresLetras), 1)
            # self.agregar_bolsa(Ficha("#", valoresLetras), 2)

         if nivel == self.dificultad[1]:        
             #bolsa de fichas nivel media, se disminuyen algunas vocales y se reducen las consonantes de 1 y 2 puntos
             self.agregar_bolsa(Ficha("A", valoresLetras), 10)
             self.agregar_bolsa(Ficha("B", valoresLetras), 2)
             self.agregar_bolsa(Ficha("C", valoresLetras), 4)
             #self.agregar_bolsa(Ficha("CH", valoresLetras), 1)
             self.agregar_bolsa(Ficha("D", valoresLetras), 3)
             self.agregar_bolsa(Ficha("E", valoresLetras), 10)
             self.agregar_bolsa(Ficha("F", valoresLetras), 1)
             self.agregar_bolsa(Ficha("G", valoresLetras), 2)
             self.agregar_bolsa(Ficha("H", valoresLetras), 2)
             self.agregar_bolsa(Ficha("I", valoresLetras), 6)
             self.agregar_bolsa(Ficha("J", valoresLetras), 1)       
             self.agregar_bolsa(Ficha("L", valoresLetras), 2)
             #self.agregar_bolsa(Ficha("LL", valoresLetras), 1)
             self.agregar_bolsa(Ficha("M", valoresLetras), 2)
             self.agregar_bolsa(Ficha("N", valoresLetras), 4)
             self.agregar_bolsa(Ficha("Ñ", valoresLetras), 1)
             self.agregar_bolsa(Ficha("O", valoresLetras), 8)
             self.agregar_bolsa(Ficha("P", valoresLetras), 2)
             self.agregar_bolsa(Ficha("Q", valoresLetras), 1)
             self.agregar_bolsa(Ficha("R", valoresLetras), 4)
             #self.agregar_bolsa(Ficha("RR", valoresLetras), 1)
             self.agregar_bolsa(Ficha("S", valoresLetras), 4)
             self.agregar_bolsa(Ficha("T", valoresLetras), 2)
             self.agregar_bolsa(Ficha("U", valoresLetras), 4)
             self.agregar_bolsa(Ficha("V", valoresLetras), 1)
             self.agregar_bolsa(Ficha("X", valoresLetras), 1)
             self.agregar_bolsa(Ficha("Y", valoresLetras), 1)
             self.agregar_bolsa(Ficha("Z", valoresLetras), 1)
             #self.agregar_bolsa(Ficha("#", valoresLetras), 2)

         if nivel == self.dificultad[2]:        
             #bolsa de fichas nivel dificil, se disminuyen aun mas las vocales
             self.agregar_bolsa(Ficha("A", valoresLetras), 8)
             self.agregar_bolsa(Ficha("B", valoresLetras), 2)
             self.agregar_bolsa(Ficha("C", valoresLetras), 4)
             #self.agregar_bolsa(Ficha("CH", valoresLetras), 1)
             self.agregar_bolsa(Ficha("D", valoresLetras), 3)
             self.agregar_bolsa(Ficha("E", valoresLetras), 7)
             self.agregar_bolsa(Ficha("F", valoresLetras), 1)
             self.agregar_bolsa(Ficha("G", valoresLetras), 2)
             self.agregar_bolsa(Ficha("H", valoresLetras), 2)
             self.agregar_bolsa(Ficha("I", valoresLetras), 4)
             self.agregar_bolsa(Ficha("J", valoresLetras), 1)       
             self.agregar_bolsa(Ficha("L", valoresLetras), 2)
             #self.agregar_bolsa(Ficha("LL", valoresLetras), 1)
             self.agregar_bolsa(Ficha("M", valoresLetras), 2)
             self.agregar_bolsa(Ficha("N", valoresLetras), 4)
             self.agregar_bolsa(Ficha("Ñ", valoresLetras), 1)
             self.agregar_bolsa(Ficha("O", valoresLetras), 6)
             self.agregar_bolsa(Ficha("P", valoresLetras), 2)
             self.agregar_bolsa(Ficha("Q", valoresLetras), 1)
             self.agregar_bolsa(Ficha("R", valoresLetras), 4)
             #self.agregar_bolsa(Ficha("RR", valoresLetras), 1)
             self.agregar_bolsa(Ficha("S", valoresLetras), 4)
             self.agregar_bolsa(Ficha("T", valoresLetras), 2)
             self.agregar_bolsa(Ficha("U", valoresLetras), 3)
             self.agregar_bolsa(Ficha("V", valoresLetras), 1)
             self.agregar_bolsa(Ficha("X", valoresLetras), 1)
             self.agregar_bolsa(Ficha("Y", valoresLetras), 1)
             self.agregar_bolsa(Ficha("Z", valoresLetras), 1)
             #self.agregar_bolsa(Ficha("#", valoresLetras), 2)
         random.shuffle(self.bolsa)

     def tomar_bolsa(self):
         #Toma la primera ficha de la bolsa y la elimina de la misma. Se usa para cambiar fichas o la recarga del atril (con un ciclo)
         return self.bolsa.pop()

     def cantidad_fichas(self):
         #Retorna la cantidad de fichas restantes
         return len(self.bolsa)

class Atril:
    """
    
    """
    def __init__(self, bolsa):
       
        self.atril = []
        self.bolsa = bolsa
        self.initialize()

    def agregar_al_atril(self):
       
        self.atril.append(self.bolsa.tomar_bolsa())

    def initialize(self):
        
         for i in range(7):
             self.agregar_al_atril()




    def get_atril_string(self):
        #Devuelve el atril en forma de string
        return ", ".join(str(item.get_letra()) for item in self.atril)

    def get_atril_array(self):
        #Devuelve el atril
        return self.atril

    def usar_ficha(self, ficha):
        #Quita la ficha del atril, para ser cambiada o jugada
        self.atril.remove(ficha)

    def get_atril_espaciosVacios(self):
        #Cantidad de fichas que faltan en el atril
        return 7 - len(self.atril)

    def get_atril_tamanio(self):
        #Cantidad de fichas en el atril
        return len(self.atril)

    def rellenar_atril(self):
        #
        while self.get_atril_espaciosVacios() > 0 and self.bolsa.cantidad_fichas() > 0:
            self.agregar_al_atril()

#Codigo de prueba, genera una bolsa segun la dificultad dada en el constructor, imprime las fichas disponibles y cantidad total de fichas 
# de la bolsa. 
if __name__ == "__main__":
    bolsa1 = Bolsa('facil')
    fichasTotales = bolsa1.cantidad_fichas()

    for i in range(fichasTotales):
        print(bolsa1.bolsa[i].letra)
    print('Total de fichas del nivel: facil ')
    print(bolsa1.cantidad_fichas())


    #Crea el atril del jugador y lo muestra en pantalla
    atril1 = Atril(bolsa1)

    atril_jugador =  atril1.get_atril_string()
    print('Atril del jugador')
    print(atril_jugador)

    #fichas en la bolsa luego de crear el primer atril
    print('Fichas restantes')
    print(bolsa1.cantidad_fichas())

    #Se simula una jugada, pidiendo que se escriba una palabra
    # (no hay verificacion alguna, se asume que se usaran letras del atril y que toda palabra es valida)

    print('Escriba una palabra a jugar, finalice con enter')

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

    #Atril del jugador luego de la jugada 
    atril_jugador =  atril1.get_atril_string()
    print('Atril del jugador luego de jugar')
    print(atril_jugador)


    #Se recargan fichas y se muestra el atril nuevo y 
    # la cantidad de fichas en la bolsa luego de todo el proceso
    atril1.rellenar_atril()

    atril_jugador =  atril1.get_atril_string()
    print('Atril del jugador luego de recargar')
    print(atril_jugador)

    print('Fichas restantes luego de recargar')
    print(bolsa1.cantidad_fichas())




