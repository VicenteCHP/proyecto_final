from app.config.mysql_connection import connectToMySQL
from app.models.pedido import Pedido 

class Producto:
    db = "planta_repostera"

    def __init__(self, data):
        self.id = data['id']
        self.nombre_producto = data['nombre_producto']
        self.precio_producto = data['precio_producto']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM productos;"
        results = connectToMySQL(cls.db).query_db(query)
        productos = []
        for row in results:
            producto = cls(row)
            productos.append(producto)
        return productos

    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM productos WHERE id = %(id)s;"
        data = {
            'id': id
        }
        result = connectToMySQL(cls.db).query_db(query, data)
        if result:
            return cls(result[0])
        return None