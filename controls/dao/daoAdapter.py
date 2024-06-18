from typing import TypeVar, Generic, Type
from controls.tda.linked.linkedList import LinkedList
import json
import os

T = TypeVar("T")
class DaoAdapter(Generic[T]):
    atype: T
    def __init__(self, atype: T):
        self.atype = atype
        self.lista = LinkedList()
        self.file = atype.__name__.lower() + ".json"
        self.URL =  (
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            + "/data/"
        )

        
    def _list(self) -> T:
        if os.path.isfile(self.URL + self.file):
            with open(self.URL + self.file, "r") as f:
                datos = json.load(f)
                self.lista.clear()
                for data in datos:
                    a = self.atype.deserializar(data)
                    self.lista.add(a, self.lista._length)
        return self.lista
    
    def _transform_(self):
        return json.dumps(
            [self.lista.get(i).serializable for i in range(self.lista._length)],
            indent=4,
        )
    
    def to_dict(self):
        aux = []
        self._list()
        for i in range(0, self.lista._length):
            aux.append(self.lista.get(i).serializable)
        return aux
    
    def _save(self, data: T) -> None:
        self.lista.add(data, self.lista._length)
        with open(self.URL + self.file, "w") as a:
            a.write(self._transform_())

    def _merge(self, data: T, pos) -> T:
        self._list()
        self.lista.edit(data, pos)
        a = open(self.URL + self.file, "w")
        a.write(self._transform_())
        a.close()

    def _delete(self, pos) -> T:
        self._list()
        self.lista.delete(pos)
        a = open(self.URL + self.file, "w")
        a.write(self._transform_())
        a.close()

    def _generate_id(self) -> int:
        lista = self._list()
        if lista._length == 0:
            return 0
        else:
            return lista.get(lista._length - 1)._id + 1
        
        
    