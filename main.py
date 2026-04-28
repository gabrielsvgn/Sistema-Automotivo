from database.conexao import conectar
from models.marca import Marca
from database.operacao_banco import BancoMarca
from database.operacao_banco import BancoModelo
from database.operacao_banco import BancoCarro
from models.modelo import Modelo
from models.carro import Carro

conectar()
marca_chevrolet = Marca(nome="Chevrolet", idmarca=46)
marca_fiat = Marca(nome="Fiat", idmarca=47)
marca_audi = Marca(nome="Audi", idmarca=48)

modelo_astra = Modelo(nome="Astra", marca=marca_chevrolet, idmodelo=13)
modelo_cobalt = Modelo(nome="Cobalt", marca=marca_chevrolet, idmodelo=14)
modelo_a3 = Modelo(nome="A3", marca=marca_audi, idmodelo=15)

astra = Carro(
    modelo=modelo_astra,
    ano=2007,
    km=216000,
    valor=45000,
    cor="Vermelho Lyra",
    placa="IRB7A08",
    disponivel=True,
    idcarro=5
)

print(modelo_a3.idmodelo)























