from database.conexao import conectar
from models.marca import Marca
from models.modelo import Modelo
from models.carro import Carro
from repositories.marca_repository import MarcaRepository
from repositories.modelo_repository import ModeloRepository
from repositories.carro_repository import CarroRepository

banco_carro = CarroRepository()
banco_marca = MarcaRepository()
banco_modelo = ModeloRepository()

conectar()



def menu_principal():

    try:
        opc = int(input("[1] Criar carro\n[2] Alterar valor \n[3] Deletar carro \n[4] Marcar como vendido \n[5] Visualizar carros \n[6] Alterar Quilometragem \n[7] Visualizar disponíveis \n[7] Procurar por placa \nSelecione uma opção: "))

        if opc == 1:
            idmodelo = int(input("Digite o id do modelo: "))
            ano = int(input("Digite o ano: "))
            km = int(input("Digite a quilometragem"))
            valor = int(input("Digite o valor: "))
            cor = input("Digite a cor: ")
            placa = input("Digite a placa: ")
            carro = Carro(idmodelo, ano, km, valor, cor, placa)
            banco_carro.create_car(carro)

    except Exception as e:
        raise e

menu_principal()





        
























