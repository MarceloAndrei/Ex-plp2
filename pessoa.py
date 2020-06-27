class Pessoa:
    def __init__(self, nome):
        self.__nome = nome
    def get_nome(self):
        return self.__nome
    def definir_id(self, identificacao):
        self._identificacao = identificacao