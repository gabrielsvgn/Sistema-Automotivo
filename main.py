from database.conexao import conectar
from models.marca import Marca
from database.operacao_banco import BancoMarca
conectar()



ferrari = Marca("488")
ferrari_novo = Marca("458")
banco = BancoMarca()
banco.listar_marcas()



















