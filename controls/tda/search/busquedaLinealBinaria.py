class BusquedaLienalBinaria:
    def busquedaLinealBinaria(self, lista, x):
        # Busqueda Lineal
        for i in range(len(lista)):
            if lista[i] == x:
                return i
        return -1

    def busquedaBinaria(self, lista, x):
        izq, der = 0, len(lista) - 1
        while izq <= der:
            mitad = (izq + der) // 2
            if lista[mitad] == x:
                return mitad
            elif lista[mitad] < x:
                izq = mitad + 1
            else:
                der = mitad - 1
        return -1
    
    