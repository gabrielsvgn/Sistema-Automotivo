from database.conexao import conectar
from models.marca import Marca
from database.operacao_banco import BancoMarca
from database.operacao_banco import BancoModelo
from models.modelo import Modelo
conectar()



opala = Modelo(1, "Opala SS")
banco_marca = BancoMarca()
banco_modelo = BancoModelo()
banco_modelo.listar_modelo()




















