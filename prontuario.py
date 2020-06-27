class Prontuário:
    def __init__(self):
        lista = []
    def insere_procedimento(self, Medicamenteo, pesologia, Medico, data, hora):
        x = {Medicamenteo, pesologia, Medico, data, hora}
        lista.append(x)
    def exibe_prontuario(self, lista):
        print(lista)