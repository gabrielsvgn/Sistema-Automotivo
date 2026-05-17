from database.conexao import conectar

class CarroRepository:
    def __init__(self):
        self.conexao = conectar()
        self.cursor = self.conexao.cursor()

    def create_car(self, carro):
        try:
                self.cursor.execute("""INSERT INTO carro (idmodelo, ano, km, valor, cor, placa, disponivel) 
        VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING idcarro""", 
        (carro.idmodelo, carro.ano, carro.km, carro.valor, carro.cor, carro.placa, "S" if carro.disponivel else "N",))
                id = self.cursor.fetchone()[0]
                self.conexao.commit()
                carro.idcarro = id
        except Exception as e:
                self.conexao.rollback()
                raise e

    def update_car_value (self, id, valor):
        try:
            self.cursor.execute("UPDATE carro SET valor = %s WHERE idcarro = %s", (valor, id,))
            self.conexao.commit()
        except Exception as e:
            raise e
        
    def delete_car (self, id):
        try:
                self.cursor.execute("DELETE FROM carro WHERE idcarro = %s", (id,))
                self.conexao.commit()
        except Exception as e:
            raise e
        
    def sell_car(self, id):
        try:
            self.cursor.execute("UPDATE carro SET disponivel = %s WHERE idcarro = %s", ('N', id,))
            self.conexao.commit()
        except Exception as e:
            raise e
        
    def read_car(self):
        try:
            self.cursor.execute("SELECT * from view_carros")
            cars = self.cursor.fetchall()
            for lista in cars:
                print(lista)
        except Exception as e:
            raise e
        
    def update_car_km(self, novo_valor, id):
        try:
            self.cursor.execute("UPDATE carro SET km = %s WHERE idcarro = %s", (novo_valor, id,))
            self.conexao.commit()
        except Exception as e:
            raise e

    def read_available_cars(self):
        try:
            self.cursor.execute("SELECT * FROM carros_disponiveis")
            return self.cursor.fetchall()
        except Exception as e:
            raise e

    def read_car_plate(self, placa):
        try:
            self.cursor.execute("SELECT * from read_car_plate WHERE placa = %s", (placa.upper(),))
            return self.cursor.fetchall()
        except Exception as e:
            raise e