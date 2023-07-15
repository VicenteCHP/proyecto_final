from app.config.mysql_connection import connectToMySQL
from app.models.pedido import Pedido 

class Sabor:
    db = "planta_repostera"

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM sabores;"
        results = connectToMySQL(cls.db).query_db(query)
        sabores = []
        for row in results:
            sabores.append(row)
        return sabores