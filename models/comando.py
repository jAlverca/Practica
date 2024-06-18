from datetime import datetime
class Comando():
    def __init__(self):
        self.__id = 0
        self.__id_usuario = 0
        self.__contenido = " "
        self.__fecha = datetime.now()

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _id_usuario(self):
        return self.__id_usuario

    @_id_usuario.setter
    def _id_usuario(self, value):
        self.__id_usuario = value

    @property
    def _contenido(self):
        return self.__contenido

    @_contenido.setter
    def _contenido(self, value):
        self.__contenido = value

    @property
    def _fecha(self):
        return self.__fecha

    @_fecha.setter
    def _fecha(self, value):
        self.__fecha = value

    @property
    def serializable(self):
        return {
            'id': self._id,
            'id_usuario': self._id_usuario,
            'contenido': self._contenido,
            'fecha': self._fecha
        }
    
    def deserializar(data):
        comando = Comando()
        comando._id = data["id"]
        comando._id_usuario = data["id_usuario"]
        comando._contenido = data["contenido"]
        comando._fecha = data["fecha"]
        return comando