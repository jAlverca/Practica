from controls.tda.linked.linkedList import LinkedList
import random
import time
lista = LinkedList()
for i in range(10000):
    lista.add(random.randint(0, 200))

print("Busqueda Lineal Binaria:")
start4 = time.time()
newLista=lista.linealBinariaNumber(100)
end = time.time()
print(f"Tiempo de ejecución: {round(end - start4, 5)} \n")

print("Busqueda lineal:")
start = time.time()
newLista=lista.linealNumber(100)
end = time.time()
print(f"Tiempo de ejecución: {round(end - start, 5)} \n")




