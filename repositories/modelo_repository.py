from database.conexao import conectar

class ModeloRepository:
    def __init__ (self):
        self.conexao = conectar()
        self.cursor = self.conexao.cursor()

    
    def create_car_model(self, modelo):
        try:
            self.cursor.execute("""INSERT INTO modelo (idmarca, nome) VALUES (%s, %s) RETURNING idmodelo""", (modelo.idmarca, modelo.nome,))
            id = self.cursor.fetchone()[0]
            self.conexao.commit()
            modelo.idmodelo = id
        except Exception as e:
            self.conexao.rollback()
            raise e
            
    def update_car_model(self, idmodelo, novo_nome):
        try:
            self.cursor.execute("""UPDATE modelo SET nome = %s WHERE idmodelo = %s""", (novo_nome, idmodelo,))
            self.conexao.commit()
        except Exception as e:
            self.conexao.rollback()
            raise e

    def delete_car_model(self, idmodelo):
        try:
            self.cursor.execute("DELETE FROM modelo WHERE idmodelo = %s", (idmodelo,))
            if self.cursor.rowcount == 0:
                print("Modelo não encontrado")
            self.conexao.commit()
        except Exception as e:
            self.conexao.rollback()
            raise e
                 
    def read_car_model(self):
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