from database.conexao import conectar
from models.marca import Marca
from repositories.marca_repository import MarcaRepository
from repositories.modelo_repository import ModeloRepository
from repositories.carro_repository import CarroRepository
from models.modelo import Modelo
from models.carro import Carro

banco_carro = CarroRepository()
banco_marca = MarcaRepository()

conectar()
marca_chevrolet = Marca(nome="Chevrolet", idmarca=46)
marca_fiat = Marca(nome="Fiat", idmarca=47)
marca_audi = Marca(nome="Audi", idmarca=48)
marca_ford = Marca(nome="Ford", idmarca= 49)


modelo_astra = Modelo(nome="Astra", idmarca=marca_chevrolet.idmarca, idmodelo=13)
modelo_cobalt = Modelo(nome="Cobalt", idmarca=marca_chevrolet.idmarca, idmodelo=14)
modelo_a3 = Modelo(nome="A3", idmarca=marca_audi.idmarca, idmodelo=15)

astra = Carro(
    idmodelo=modelo_astra.idmodelo,
    ano=2007,
    km=216000,
    valor=45000,
    cor="Vermelho Lyra",
    placa="IRB7A08",
    disponivel=True,
)

banco_marca.create_car_brand(marca_ford)























