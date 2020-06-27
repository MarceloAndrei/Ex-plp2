from pessoa import Pessoa
class Paciente(Pessoa):
    i = 0
    def __init__(self):
        i = i+1
    def __del__(self):
        i = i-1
    def definir_id(self, identificacao):
        if len(identificacao) > 5:
            print("Erro")
        else:
            self._identificacao = identificacao
    def definir_prontuário(self,Prontuario):
    def pacientes_ativos(self):
        return i