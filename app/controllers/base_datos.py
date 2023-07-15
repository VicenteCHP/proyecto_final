from flask import render_template, redirect, session, request, flash, url_for
from app import app
from app.models.user import User
from app.models.cliente import Cliente
from app.models.base_dato import Datos


@app.route('/base_de_datos')
def base_datos():
    
    return render_template('base_datos.html')


@app.route('/base_de_datos', methods=['POST'])
def mostrar_datos():
    data = {
        'id': request.form.get('id'),
        'nombre': request.form.get('nombre'),
        'apellido': request.form.get('apellido'),
        'dni': request.form.get('dni'),
        'correo': request.form.get('correo'),
        'telefono': request.form.get('telefono'),
        'direccion': request.form.get('direccion'),
        'users_id': request.form.get('users_id'),
        'nombre_producto': request.form.get('nombre_producto'),
        'nombre_relleno': request.form.get('nombre_relleno'),
        'nombre_extra': request.form.get('nombre_extra'),
        'nombre_sabores': request.form.get('nombre_sabores'),
        'nombre_empaque': request.form.get('nombre_empaque'),
        'caracteristicas': request.form.get('caracteristicas'),
        'fecha_entrega': request.form.get('fecha_entrega'),
        'fecha_ingreso': request.form.get('fecha_ingreso'),
        'tipo_de_entrega': request.form.get('tipo_de_entrega')
    }
    
    return render_template('base_datos.html', datos=data)

