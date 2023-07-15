from app.config.mysql_connection import connectToMySQL
from app.models.pedido import Pedido 

class Extra:
    db = "planta_repostera"

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM extras;"
        results = connectToMySQL(cls.db).query_db(query)
        extras = []
        for row in results:
            extras.append(row)
        return extras