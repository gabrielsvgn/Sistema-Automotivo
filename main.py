from database.conexao import conectar
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
        opc = int(input("[1] Criar carro\n[2] Editar valor \n[3] Deletar carro \n[4] Marcar como vendido \n[5] Visualizar carros \n[6] Editar Quilometragem \n[7] Visualizar disponíveis \n[8] Procurar por placa \nSelecione uma opção: "))

        if opc == 1:
            idmodelo = int(input("Digite o id do modelo: "))
            ano = int(input("Digite o ano: "))
            km = int(input("Digite a quilometragem: "))
            valor = int(input("Digite o valor: "))
            cor = input("Digite a cor: ")
            placa = input("Digite a placa: ")
            disponivel = "S"
            carro = Carro(idmodelo, ano, km, valor, cor, placa, disponivel)
            banco_carro.create_car(carro)
            print("Carro adicionado com sucesso! ")

        if opc == 2:
            novo_valor = int(input("Digite o novo valor: "))
            idcarro = int(input("Digite o id do carro: "))
            banco_carro.update_car_km(novo_valor, idcarro)
            print("Valor alterado com sucesso! ")

        if opc == 3:
            deletar = int(input("Digite o id do carro: "))
            banco_carro.delete_car(deletar)
            print("Carro deletado com sucesso! ")

        if opc == 4:
            vender = int(input("Digite o id do carro que você quer vender: "))
            banco_carro.sell_car(vender)
            print("Carro marcado como vendido! ")

        if opc == 5:
            banco_carro.read_car()
            print("Mostrando todos veículos... ")

        if opc == 6:
            quilometragem = int(input("Digite a nova Quilometragem: "))
            idkm = int(input("Digite o id do carro: "))
            banco_carro.update_car_km(quilometragem, idkm)
            print("Quilometragem editada com sucesso! ")

        if opc == 7:
            banco_carro.read_available_cars()
            print("Mostrando veículos disponíveis... ")

        if opc == 8:
            placa_carro = input("Digite a placa do carro: ")
            banco_carro.read_car_plate(placa_carro)
            print("Mostrando carro...")

    except ValueError:
        print("Adicione um valor válido")

menu_principal()





        
























