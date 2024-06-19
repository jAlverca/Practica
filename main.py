from controls.tda.linked.linkedList import LinkedList
import random
import time
lista = LinkedList()
for i in range(25000):
    lista.add(random.randint(0, 200))



print("Busqueda Binaria ")
start = time.time()
newLista= lista.linealBinariaNumber(100)
print(newLista)
end = time.time()   
print(f"Tiempo de ejecución: {round(end - start, 5)} \n")