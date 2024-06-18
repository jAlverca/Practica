from models.usuario import Usuario
from controls.dao.daoAdapter import DaoAdapter
class UsuarioController(DaoAdapter):
    def __init__(self):
        super().__init__(Usuario)
        self.__usuario = None
    @property
    def _usuario(self):
        if self.__usuario is None:
            self.__usuario = Usuario()
        return self.__usuario

    @_usuario.setter
    def _usuario(self, value):
        self.__usuario = value

    def _lista(self):
        return self._list()

    @property
    def save(self):
        self._usuario._id = self._generate_id()
        print("gg")
        self._save(self._usuario)
        self.__usuario = None

        