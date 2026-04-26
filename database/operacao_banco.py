from database.conexao import conectar
from psycopg2 import sql

# Banco Marca
class BancoMarca:
    def __init__(self):
        self.conexao = conectar()
        self.cursor = self.conexao.cursor()

    def adicionar_marca(self, marca):
        try:
            self.cursor.execute("INSERT INTO marca (nome) VALUES (%s)", (marca.nome,))
            self.conexao.commit()
        except Exception as e:
            print(f"Nome duplicado! ", e)
            self.conexao.rollback()

    def remover_marca(self, idmarca):
        try:
            self.cursor.execute("DELETE FROM marca WHERE idmarca = %s", (idmarca,))
            self.conexao.commit()
        except Exception as e:
             print(f"Erro ao remover marca com o ID {idmarca}:", e)
             self.conexao.rollback()

    def atualizar_marca(self, novo_nome, idmarca):
        try:
            self.cursor.execute("UPDATE marca SET nome = %s WHERE idmarca = %s", (novo_nome.nome, idmarca,))
            self.conexao.commit()
        except Exception as e:
            print("Erro ao atualizar marca", e)
            self.conexao.rollback()
        

    def listar_marcas(self):
        try:
            self.cursor.execute("SELECT * FROM marca")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Erro ao listar marcas: ", e)

      


        







