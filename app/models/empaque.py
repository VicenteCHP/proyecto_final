from app.config.mysql_connection import connectToMySQL
from app.models.pedido import Pedido 

class Empaque:
    db = "planta_repostera"

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM empaques;"
        results = connectToMySQL(cls.db).query_db(query)
        empaques = []
        for row in results:
            empaques.append(row)
        return empaques