class Usuario():
    def __init__(self):
        self.__nombre = " "
        self.__apellido = " "
        self.__telefono = " "
        self.__id = 0

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _apellido(self):
        return self.__apellido

    @_apellido.setter
    def _apellido(self, value):
        self.__apellido = value

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _telefono(self):
        return self.__telefono

    @_telefono.setter
    def _telefono(self, value):
        self.__telefono = value

    @property
    def serializable(self):
        return {
            'nombre': self._nombre,
            'apellido': self._apellido,
            'id': self._id,
            'telefono': self._telefono
        }
    
    def deserializar(data: dict):
        usuario = Usuario()
        usuario._id = data["id"]
        usuario._nombre = data["nombre"]
        usuario._apellido = data["apellido"]
        usuario._telefono = data["telefono"]
        return usuario

    def __str__(self) -> str:
        return f"{self._nombre} {self._apellido} {self._id} {self._telefono}"
