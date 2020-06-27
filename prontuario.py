from medicamento import Medicamento
from medico import Medico
from paciente import Paciente
from datetime import date

data = date.today()
data_atual = ‘{}/{}/{}’.format(data.day, data.month, data.year)
hora = date.strftime('%H:%M')


class Prontuário:

    def __init__(self):
        self.__lista = []

    def insere_procedimento(self, medicamento, posologia, medico, data, hora):
        x = {medicamento: Medicamento.nome_medicamento, posologia: posologia,
             medico: Medico.nome_medico, data: data_atual, hora: hora}

        append.lista[x]

    def exibe_prontuario(self):
        print(lista)
