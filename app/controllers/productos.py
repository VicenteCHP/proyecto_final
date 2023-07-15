from flask import render_template, redirect, session, request, flash
from app import app
from app.models.user import User
from app.models.cliente import Cliente
from app.models.pedido import Pedido 
from app.models.producto import Producto

@app.route('/nuevo_pedido')
def mostrar_productos():
    productos = Producto.get_all()
    return render_template('ingresar_pedido.html', productos=productos)