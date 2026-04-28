from database.conexao import conectar
from psycopg2 import sql

# Banco Marca
class BancoMarca:
    def __init__(self):
        self.conexao = conectar()
        self.cursor = self.conexao.cursor()

    # Adicionar Marca
    def adicionar_marca(self, marca):
        try:
            self.cursor.execute("INSERT INTO marca (nome) VALUES (%s) RETURNING idmarca", (marca.nome,))
            id = self.cursor.fetchone()[0]
            self.conexao.commit()
            marca.idmarca = id
        except Exception as e:
            self.conexao.rollback()
            raise e

    # Remover Marca
    def remover_marca(self, idmarca):
        try:
            self.cursor.execute("DELETE FROM marca WHERE idmarca = %s", (idmarca,))
            self.conexao.commit()
        except Exception as e:
             self.conexao.rollback()
             raise e

    # Atualizar Marca
    def atualizar_marca(self, novo_nome, idmarca):
        try:
            self.cursor.execute("UPDATE marca SET nome = %s WHERE idmarca = %s", (novo_nome.nome, idmarca,))
            self.conexao.commit()
        except Exception as e:
            self.conexao.rollback()
            raise e
        
    # Listar Marcas
    def listar_marcas(self):
        try:
            self.cursor.execute("SELECT * FROM marca")
            return self.cursor.fetchall()
        except Exception as e:
            self.conexao.rollback()
            raise e

# Banco Modelo
class BancoModelo:
    def __init__ (self):
        self.conexao = conectar()
        self.cursor = self.conexao.cursor()

    # Adicionar Modelo
    def adicionar_modelo(self, modelo):
        try:
            self.cursor.execute("""INSERT INTO modelo (idmarca, nome) VALUES (%s, %s) RETURNING idmodelo""", (modelo.idmarca, modelo.nome,))
            id = self.cursor.fetchone()[0]
            self.conexao.commit()
            modelo.idmodelo = id
        except Exception as e:
            self.conexao.rollback()
            raise e
            
    # Listar Todos
    def listar_modelo(self):
        try:
            self.cursor.execute("""SELECT
                                mdl.nome,
                                mrc.nome
                                FROM
                                modelo mdl
                                LEFT OUTER JOIN
                                marca mrc on mrc.idmarca = mdl.idmarca
                                """)
            return self.cursor.fetchall()
            
       
        except Exception as e:
            raise e


    # Atualizar Modelos
    def atualizar_modelo(self, idmodelo, novo_nome):
        try:
            self.cursor.execute("""UPDATE modelo SET nome = %s WHERE idmodelo = %s""", (novo_nome, idmodelo,))
            self.conexao.commit()
        except Exception as e:
            self.conexao.rollback()
            raise e

    # Remover
    def remover_modelo(self, idmodelo):
        try:
            self.cursor.execute("DELETE FROM modelo WHERE idmodelo = %s", (idmodelo,))
            if self.cursor.rowcount == 0:
                print("Modelo não encontrado")
            self.conexao.commit()
        except Exception as e:
            self.conexao.rollback()
            raise e
        
# Banco Carro
class BancoCarro:
    def __init__(self):
        self.conexao = conectar()
        self.cursor = self.conexao.cursor()

    def adicionar_carro(self, carro):
        try:
            if carro.idmodelo is None:
                ValueError("Modelo precisa estar salvo no banco antes")
                self.cursor.execute("""INSERT INTO carro (idmodelo, ano, km, valor, cor, placa, disponivel) 
        VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING idcarro""", 
        (carro.idmodelo, carro.ano, carro.km, carro.valor, carro.cor, carro.placa, "S" if carro.disponivel else "N",))
                id = self.cursor.fetchone()[0]
                self.conexao.commit()
                carro.idcarro = id
        except Exception as e:
                self.conexao.rollback()
                raise e

        







