class Heapsort:

    def heapsort(self, array):
        n = len(array)
        self.build_max_heap(array, n)
        for i in range(n - 1, 0, -1):
            array[0], array[i] = array[i], array[0]
            n -= 1
            self.max_heapify(array, 0, n)
        return array