from app.config.mysql_connection import connectToMySQL
from app.models.user import User
from flask import flash

from app.config.mysql_connection import connectToMySQL

class Cliente:
    db = "planta_repostera"

    def __init__(self, data):
        self.id = data['id']  # Asigna users_id al atributo id
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.dni = data['dni']
        self.correo = data['correo']
        self.telefono = data['telefono']
        self.direccion = data['direccion']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO clientes (nombre, apellido, dni, correo, telefono, direccion, users_id) VALUES (%(nombre)s, %(apellido)s, %(dni)s, %(correo)s, %(telefono)s, %(direccion)s, %(users_id)s)"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM clientes;"
        results = connectToMySQL(cls.db).query_db(query)
        clientes = []
        for row in results:
            clientes.append(cls(row))
        return clientes

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM clientes WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE clientes SET nombre = %(nombre)s, apellido = %(apellido)s, dni = %(dni)s, correo = %(correo)s, telefono = %(telefono)s, direccion = %(direccion)s, users_id = %(users_id)s WHERE id = %(id)s"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM clientes WHERE id = %(id)s"
        return connectToMySQL(cls.db).query_db(query, data)