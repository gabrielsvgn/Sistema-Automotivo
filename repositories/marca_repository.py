from database.conexao import conectar

class MarcaRepository:
    def __init__(self):
        self.conexao = conectar()
        self.cursor = self.conexao.cursor()

    
    def create_car_brand(self, marca):
        try:
            self.cursor.execute("INSERT INTO marca (nome) VALUES (%s) RETURNING idmarca", (marca.nome,))
            id = self.cursor.fetchone()[0]
            self.conexao.commit()
            marca.idmarca = id
        except Exception as e:
            self.conexao.rollback()
            raise e


    def delete_car_brand(self, idmarca):
        try:
            self.cursor.execute("DELETE FROM marca WHERE idmarca = %s", (idmarca,))
            self.conexao.commit()
        except Exception as e:
             self.conexao.rollback()
             raise e

    
    def update_car_brand(self, novo_nome, idmarca):
        try:
            self.cursor.execute("UPDATE marca SET nome = %s WHERE idmarca = %s", (novo_nome.nome, idmarca,))
            self.conexao.commit()
        except Exception as e:
            self.conexao.rollback()
            raise e
        
    
    def read_all_car_brand(self):
        try:
            self.cursor.execute("SELECT * FROM marca")
            return self.cursor.fetchall()
        except Exception as e:
            self.conexao.rollback()
            raise e


    def read_car_brand (self, marca):
        try:
            self.cursor.execute("SELECT lower(nome) FROM marca WHERE nome = %s", (marca,))
            carro = self.cursor.fetchall()
            for lista in carro:
                print(lista)
        except Exception as e:
            raise e
