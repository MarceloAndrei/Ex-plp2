from pessoa import Pessoa;
class Medico(Pessoa):
    def __init__(self,nome):
        self.__nome = nome
    def definir_id(self, identificacao):
        if len(identificacao) > 3:
            print("Erro")
        else:
            self._identificacao = identificacao
    def nome_medico(self):
        return self.__nome