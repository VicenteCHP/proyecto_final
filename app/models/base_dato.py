from app.config.mysql_connection import connectToMySQL
from app.models.user import User
from flask import flash

class Datos:
    db = "planta_repostera"
    
    def __init__(self, data):
        self.id = data.get('id')
        self.nombre = data.get('nombre')
        self.apellido = data.get('apellido')
        self.dni = data.get('dni')
        self.correo = data.get('correo')
        self.telefono = data.get('telefono')
        self.direccion = data.get('direccion')
        self.users_id = data.get('users_id')
        self.nombre_producto = data.get('nombre_producto')
        self.nombre_relleno = data.get('nombre_relleno')
        self.nombre_extra = data.get('nombre_extra')
        self.nombre_sabores = data.get('nombre_sabores')
        self.nombre_empaque = data.get('nombre_empaque')
        self.caracteristicas = data.get('caracteristicas')
        self.fecha_entrega = data.get('fecha_entrega')
        self.fecha_ingreso = data.get('fecha_ingreso')
        self.tipo_de_entrega = data.get('tipo_de_entrega')
        
    @classmethod
    def save(cls, data):
        query = """
            SELECT clientes.*, rellenos.nombre AS nombre_relleno, extras.nombre AS nombre_extra, sabores.nombre AS nombre_sabores, empaques.nombre AS nombre_empaque, productos.nombre AS nombre_producto
            FROM clientes
            INNER JOIN pedidos ON clientes.id = pedidos.clientes_id
            INNER JOIN rellenos ON pedidos.relleno_id = rellenos.id
            INNER JOIN extras ON pedidos.extras_id = extras.id
            INNER JOIN sabores ON pedidos.sabores_id = sabores.id
            INNER JOIN empaques ON pedidos.empaques_id = empaques.id
            INNER JOIN productos ON pedidos.productos_id = productos.id
            WHERE fecha_ingreso = %(fecha_ingreso)s
            AND fecha_pago = %(fecha_pago)s
            AND fecha_entrega = %(fecha_entrega)s
            AND caracteristicas = %(caracteristicas)s
            AND tipo_de_entrega = %(tipo_de_entrega)s
            AND precio_total = %(precio_total)s
            AND sabores_id = %(sabores_id)s
            AND relleno_id = %(relleno_id)s
            AND empaques_id = %(empaques_id)s
            AND extras_id = %(extras_id)s
            AND clientes_id = %(clientes_id)s
            AND productos_id = %(productos_id)s
            """
        return connectToMySQL(cls.db).query_db(query, data)
