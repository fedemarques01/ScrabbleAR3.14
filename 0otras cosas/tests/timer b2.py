from threading import Timer as timer

def temporizador(time):
    def timeout():
        print("Game over")
    t = timer(time, timeout)
    return t
    
t= temporizador(1)
print(t)
t.start()#Empieza el temporizador
print(t.join())