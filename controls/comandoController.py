from models.comando import Comando
from controls.dao.daoAdapter import DaoAdapter
class ComandoController(DaoAdapter):
    def __init__(self):
        super().__init__(Comando)
        self.__comando = None

    @property
    def _comando(self):
        if self.__comando is None:
            self.__comando = Comando()
        return self.__comando

    @_comando.setter
    def _comando(self, value):
        self.__comando = value
       
    def _lista(self):
        return self._list()

    @property
    def save(self):
        self._comando._id = self._generate_id()
        self._save(self._comando)
        self.__comando = None
