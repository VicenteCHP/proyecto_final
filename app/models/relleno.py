from app.config.mysql_connection import connectToMySQL
from app.models.pedido import Pedido 

class Relleno:
    db = "planta_repostera"

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM relleno;"
        results = connectToMySQL(cls.db).query_db(query)
        rellenos = []
        for row in results:
            rellenos.append(row)
        return rellenos