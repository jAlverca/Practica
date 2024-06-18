class BusquedaBinaria:

    def busquedaBinaria(self, lista, item):
        primero = 0
        ultimo = len(lista) - 1
        while primero <= ultimo:
            puntoMedio = (primero + ultimo) // 2
            if lista[puntoMedio] == item:
                return puntoMedio
            else:
                if item < lista[puntoMedio]:
                    ultimo = puntoMedio - 1
                else:
                    primero = puntoMedio + 1
        return None