from controls.tda.linked.node import Node

class LinkedList(object):
    def __init__(self):
        self.__head = None
        self.__last = None
        self.__length = 0
        self.__current = None

    @property
    def _head(self):
        return self.__head

    @_head.setter
    def _head(self, value):
        self.__head = value

    @property
    def _last(self):
        return self.__last

    @_last.setter
    def _last(self, value):
        self.__last = value

    @property
    def _length(self):
        return self.__length

    @_length.setter
    def _length(self, value):
        self.__length = value

    @property
    def isEmpty(self):
        return self.__head is None or self.__length == 0
    
    def addFirst(self, data):
        if self.isEmpty:
            node = Node(data)
            self.__head = node
            self.__last = node
            self.__length += 1
        else:
            headOld = self.__head
            node = Node(data, headOld)
            self.__head = node
    
    def addLast(self, data):
        if self.isEmpty:
            self.addFirst(data)
        else:
            node = Node(data)
            self.__last._next = node
            self.__last = node
            self.__length += 1

    def getFirst(self):
        if self.isEmpty:
            raise ValueError("Lista vacía")
        else:
            return self.__head._data
    
    def getLast(self):
        if self.isEmpty:
            raise ValueError("Lista vacía")
        else:
            return self.__last._data
        
    def get(self, index):
        if self.isEmpty:
            raise ValueError("Lista vacía")
        elif index < 0 or index >= self._length:
            raise IndexError("Fuera de rango")
        elif index == 0:
            return self.getFirst()
        elif index == (self._length - 1):
            return self.getLast()
        else:
            node = self.getNode(index)
            return node._data
        
    @property
    def toArray(self):
        array = [] 
        if self._length > 0:
            aux = self.__head
            for _ in range(self._length):
                array.append(aux._data)
                aux = aux._next
        return array
        
    def delete(self, pos=0):
        pass
        
    def getNode(self, pos):
        if self.isEmpty:
            raise Exception("Error, Lista vacía")
        elif pos < 0 or pos >= self._length:
            raise IndexError("Error, Fuera del límite de la lista")
        elif pos == 0:
            return self.__head
        elif pos == (self._length - 1):
            return self.__last
        else:
            search = self.__head
            cont = 0
            while cont < pos:
                cont += 1
                search = search._next
            return search
    
    def add(self, data, pos=0):
        if pos == 0:
            self.addFirst(data)
        elif pos == self.__length:
            self.addLast(data)
        else:
            node_preview = self.getNode(pos-1)
            node_last = node_preview._next 
            node = Node(data, node_last)
            node_preview._next = node
            self.__length += 1

    def edit(self, data, pos=0):
        if pos == 0:
            self.__head._data = data
        elif pos == self.__length:
            self.__last._data = data
        else:
            node = self.getNode(pos)
            node._data = data

    def update(self, pos, data):
        if self.isEmpty:
            raise Exception("Lista vacía")
        elif pos < 0 or pos >= self._length:
            raise IndexError("Error, fuera de los límites")
        elif pos == 0:
            self.__head._data = data
        elif pos == (self._length - 1):
            self.__last._data = data
        else:
            search = self.__head
            cont = 0
            while cont < pos:
                cont += 1
                search = search._next
            search._data = data

    def str(self) -> str:
        out = ""
        if self.isEmpty:
            out = "Lista vacía"
        else:
            node = self.__head
            while node is not None:
                out += str(node._data)
                node = node._next
        return out
    
    def listar(self):
        lista = []
        aux = self.__head
        for _ in range(self._length):
            lista.append(aux._data)
            aux = aux._next
        return lista
    
    @property
    def print(self):
        node = self.__head
        data = ""
        while node is not None:
            data += str(node._data) + "  "
            node = node._next
        print("Lista de datos")
        print(data)

    def clear(self):
        self.__head = None
        self.__last = None
        self.__length = 0

    def __iter__(self):
        self.__current = self.__head
        return self

    def __next__(self):
        if self.__current is None:
            raise StopIteration
        else:
            item = self.__current._data
            self.__current = self.__current._next
            return item

    def __getitem__(self, index):
        if index < 0 or index >= self._length:
            raise IndexError("Error, fuera de los límites de la lista")
        else:
            return self.getNode(index)._data

    def to_dict(self) -> dict:
        dict_list = []
        aux = self.__head
        for _ in range(self._length):
            dict_list.append(aux._data.serializable)
            aux = aux._next
        return dict_list

    #METODO QUICKSORT
    def quick(self, attribute, asc=True, ):
        array = self.toArray
        sorted_array = self.quicksort_(array, attribute, asc)
        self.clear()
        for item in sorted_array:
            self.addLast(item)
    
    def quicksort_(self, array, attribute, asc):
        if len(array) <= 1:
            return array
        pivot = array[len(array) // 2]
        if asc:
            left = [x for x in array if getattr(x, attribute) < getattr(pivot, attribute)]
            middle = [x for x in array if getattr(x, attribute) == getattr(pivot, attribute)]
            right = [x for x in array if getattr(x, attribute) > getattr(pivot, attribute)]
        else:
            left = [x for x in array if getattr(x, attribute) > getattr(pivot, attribute)]
            middle = [x for x in array if getattr(x, attribute) == getattr(pivot, attribute)]
            right = [x for x in array if getattr(x, attribute) < getattr(pivot, attribute)]
        return self.quicksort_(left, attribute, asc) + middle + self.quicksort_(right, attribute, asc)
    #FIN DEL METODO QUICKSORT

    #METODO QUICKSORT PARA NUMEROS
    def quickNumber(self, asc=True):
        array = self.toArray
        sorted_array = self.quicksortNumber(array, asc)
        self.clear()
        for item in sorted_array:
            self.addLast(item)

    def quicksortNumber(self, array, asc):
        if len(array) <= 1:
            return array
        pivot = array[len(array) // 2]
        if asc:
            left = [x for x in array if x < pivot]
            middle = [x for x in array if x == pivot]
            right = [x for x in array if x > pivot]
        else:
            left = [x for x in array if x > pivot]
            middle = [x for x in array if x == pivot]
            right = [x for x in array if x < pivot]
        return self.quicksortNumber(left, asc) + middle + self.quicksortNumber(right, asc)
    #FIN DEL METODO QUICKSORT PARA NUMEROS

    #METODO MERGESORT
    def merge(self, attribute, asc=True):
        array = self.toArray
        sorted_array = self.mergesort(array, attribute, asc)
        self.clear()
        for item in sorted_array:
            self.addLast(item)
    
    def mergesort(self, array, attribute, asc):
        if len(array) <= 1:
            return array
        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]
        left = self.mergesort(left, attribute, asc)
        right = self.mergesort(right, attribute, asc)
        return self.merge_(left, right, attribute, asc)
    
    def merge_(self, left, right, attribute, asc):
        result = []
        left_index = 0
        right_index = 0
        while left_index < len(left) and right_index < len(right):
            if asc:
                if getattr(left[left_index], attribute) < getattr(right[right_index], attribute):
                    result.append(left[left_index])
                    left_index += 1
                else:
                    result.append(right[right_index])
                    right_index += 1
            else:
                if getattr(left[left_index], attribute) > getattr(right[right_index], attribute):
                    result.append(left[left_index])
                    left_index += 1
                else:
                    result.append(right[right_index])
                    right_index += 1
        result += left[left_index:]
        result += right[right_index:]
        return result
    #FIN DEL METODO MERGESORT

    #METODO MERGESORT PARA NUMEROS
    def mergeNumber(self, asc=True):
        array = self.toArray
        sorted_array = self.mergesortNumber(array, asc)
        self.clear()
        for item in sorted_array:
            self.addLast(item)

    def mergesortNumber(self, array, asc):
        if len(array) <= 1:
            return array
        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]
        left = self.mergesortNumber(left, asc)
        right = self.mergesortNumber(right, asc)
        return self.numberMerge(left, right, asc)

    def numberMerge(self, left, right, asc):
        result = []
        left_index = 0
        right_index = 0
        while left_index < len(left) and right_index < len(right):
            if asc:
                if left[left_index] < right[right_index]:
                    result.append(left[left_index])
                    left_index += 1
                else:
                    result.append(right[right_index])
                    right_index += 1
            else:
                if left[left_index] > right[right_index]:
                    result.append(left[left_index])
                    left_index += 1
                else:
                    result.append(right[right_index])
                    right_index += 1
        result += left[left_index:]
        result += right[right_index:]
        return result
    #FIN DEL METODO MERGESORT PARA NUMEROS

    #METODO SHELLSORT
    def shell(self, attribute, asc=True):
        array = self.toArray
        sorted_array = self.shellsort(array, attribute, asc)
        self.clear()
        for item in sorted_array:
            self.addLast(item)
    
    def shellsort(self, array, attribute, asc):
        n = len(array)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = array[i]
                j = i
                if asc:
                    while j >= gap and getattr(array[j - gap], attribute) > getattr(temp, attribute):
                        array[j] = array[j - gap]
                        j -= gap
                else:
                    while j >= gap and getattr(array[j - gap], attribute) < getattr(temp, attribute):
                        array[j] = array[j - gap]
                        j -= gap
                array[j] = temp
            gap //= 2
        return array
    #FIN DEL METODO SHELLSORT

    #METODO SHELLSORT PARA NUMEROS
    def shellNumber(self, asc=True):
        array = self.toArray
        sorted_array = self.shellsortNumber(array, asc)
        self.clear()
        for item in sorted_array:
            self.addLast(item)

    def shellsortNumber(self, array, asc):
        n = len(array)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = array[i]
                j = i
                if asc:
                    while j >= gap and array[j - gap] > temp:
                        array[j] = array[j - gap]
                        j -= gap
                else:
                    while j >= gap and array[j - gap] < temp:
                        array[j] = array[j - gap]
                        j -= gap
                array[j] = temp
            gap //= 2
        return array
    #FIN DEL METODO SHELLSORT PARA NUMEROS


    #METODO BUSQUEDA BINARIA 
    def busquedaBinaria(self, attribute, value):
        if self.isEmpty:
            raise Exception("Error, lista vacía")
        else:
            self.quick(attribute)
            array = self.toArray
            low = 0
            high = len(array) - 1
            while low <= high:
                mid = (low + high) // 2
                if getattr(array[mid], attribute) == value:
                    return array[mid]
                elif getattr(array[mid], attribute) < value:
                    low = mid + 1
                else:
                    high = mid - 1
            return None
    #FIN DEL METODO BUSQUEDA BINARIA

    #METODO BUSQUEDA LINEAL
    def lineal(self, attribute, value):
        if self.isEmpty:
            raise Exception("Error, lista vacía")
        else:
            for i in range(self._length):
                if getattr(self.get(i), attribute) == value:
                    return self.get(i)
            return None
    #FIN DEL METODO BUSQUEDA LINEAL

    #METODO BUSQUEDA LINEAL PARA NUMEROS
    def linealNumber(self, value):
        if self.isEmpty:
            raise Exception("Error, lista vacía")
        else:
            for i in range(self._length):
                if self.get(i) == value:
                    return self.get(i)
            return None
    #FIN DEL METODO BUSQUEDA LINEAL PARA NUMEROS
            
    #BUSQUEDA LINEAL BINARIA
    def linealBinaria(self, attribute, value):
        if self.isEmpty:
            raise Exception("Error, lista vacía")
        
        found_items = []
        current = self._head
        index = 0

        while current is not None:
            if getattr(current._data, attribute) == value:
                found_items.append(current._data)
            current = current._next
            index += 1

        if found_items:
            return found_items  

        array = self.toArray
        low, high = 0, len(array) - 1

        while low <= high:
            mid = (low + high) // 2
            if getattr(array[mid], attribute) == value:
                left, right = mid, mid + 1
                while left >= low and getattr(array[left], attribute) == value:
                    found_items.append(array[left])
                    left -= 1
                while right <= high and getattr(array[right], attribute) == value:
                    found_items.append(array[right])
                    right += 1
                break  
            elif getattr(array[mid], attribute) < value:
                low = mid + 1
            else:
                high = mid - 1

        return found_items
    #FIN DE LA BUSQUEDA LINEAL BINARIA

    #METODO DE BUSQUEDA LINEAL BINARIA PARA NUMEROS
    def linealBinariaNumber(self, value):
        if self.isEmpty:
            raise Exception("Error, lista vacía")
        
        found_items = []
        current = self._head
        index = 0

        while current is not None:
            if current._data == value:
                found_items.append(current._data)
            current = current._next
            index += 1

        if found_items:
            return found_items  
        array = self.toArray
        low, high = 0, len(array) - 1

        while low <= high:
            mid = (low + high) // 2
            if array[mid] == value:
                left, right = mid, mid + 1
                while left >= low and array[left] == value:
                    found_items.append(array[left])
                    left -= 1
                while right <= high and array[right] == value:
                    found_items.append(array[right])
                    right += 1
                break  
            elif array[mid] < value:
                low = mid + 1
            else:
                high = mid - 1

        return found_items
    #FIN DE LA BUSQUEDA LINEAL BINARIA PARA NUMEROS



