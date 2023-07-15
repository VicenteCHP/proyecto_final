from flask import render_template, redirect, session, request, flash, url_for
from app import app
from app.models.user import User
from app.models.cliente import Cliente


@app.route('/nuevo_cliente')
def nuevo_cliente():
    return render_template('ingresar_cliente.html')

@app.route('/guardar_cliente', methods=['POST'])
def guardar_cliente():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    dni = request.form['dni']
    correo = request.form['correo']
    telefono = request.form['telefono']
    direccion = request.form['direccion']
    user_id = session['user_id']['user_id']  # Obtén el ID del usuario logueado desde la sesión

    data = {
        'nombre': nombre,
        'apellido': apellido,
        'dni': dni,
        'correo': correo,
        'telefono': telefono,
        'direccion': direccion,
        'users_id': user_id  # Asigna el user_id del usuario logueado
    }

    print("Valores recibidos:")
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("DNI:", dni)
    print("Correo:", correo)
    print("Teléfono:", telefono)
    print("Dirección:", direccion)
    print("users_id:", user_id)

    cliente_id = Cliente.save(data)
    return redirect(url_for('nuevo_pedido',cliente_id=cliente_id))