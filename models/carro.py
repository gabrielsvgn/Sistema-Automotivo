class Carro:
    def __init__(self, idmodelo, ano, km, valor, cor, placa, disponivel = True, idcarro = None):
        self.idcarro = idcarro
        self.idmodelo = idmodelo
        self.ano = ano
        self.km = km
        self.valor = valor
        self.cor = cor
        self.placa = placa
        self.disponivel = disponivel