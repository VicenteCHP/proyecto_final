from app.config.mysql_connection import connectToMySQL
from app.models.user import User
from app.models.cliente import Cliente
from flask import flash


class Pedido:
    db = "planta_repostera"

    def __init__(self, data):
        self.id = data['id']
        self.fecha_ingreso = data['fecha_ingreso']
        self.fecha_pago = data['fecha_pago']
        self.fecha_entrega = data['fecha_entrega']
        self.caracteristicas = data['caracteristicas']
        self.agregar_fotos = data['agregar_fotos']
        self.tipo_de_entrega = data['tipo_de_entrega']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.precio_total = data['precio_total']
        self.sabores_id = data['sabores_id']
        self.relleno_id = data['relleno_id']
        self.empaques_id = data['empaques_id']
        self.extras_id = data['extras_id']
        self.clientes_id = data['clientes_id']
        self.productos_id = data['productos_id']

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO pedido (fecha_ingreso, fecha_pago, fecha_entrega, caracteristicas, tipo_de_entrega, precio_total, sabores_id, relleno_id, empaques_id, extras_id, clientes_id, productos_id) 
        VALUES (%(fecha_ingreso)s, %(fecha_pago)s, %(fecha_entrega)s, %(caracteristicas)s, %(tipo_de_entrega)s, %(precio_total)s, %(sabores_id)s, %(relleno_id)s, %(empaques_id)s, %(extras_id)s, %(clientes_id)s, %(productos_id)s)"""
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM pedido;"
        results = connectToMySQL(cls.db).query_db(query)
        pedidos = []
        for row in results:
            pedidos.append(cls(row))
        return pedidos

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM pedido WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE pedido SET fecha_ingreso = %(fecha_ingreso)s, fecha_pago = %(fecha_pago)s, fecha_entrega = %(fecha_entrega)s, caracteristicas = %(caracteristicas)s, agregar_fotos = %(agregar_fotos)s, tipo_de_entrega = %(tipo_de_entrega)s, precio_total = %(precio_total)s, sabores_id = %(sabores_id)s, relleno_id = %(relleno_id)s, empaques_id = %(empaques_id)s, extras_id = %(extras_id)s, clientes_id = %(clientes_id)s, productos_id = %(productos_id)s WHERE id = %(id)s"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM pedido WHERE id = %(id)s"
        return connectToMySQL(cls.db).query_db(query, data)