from flask import render_template, redirect, session, request, flash
from app import app
from app.models.user import User
from app.models.cliente import Cliente
from app.models.pedido import Pedido 
from app.models.sabor import Sabor 

@app.route('/nuevo_pedido')
def ingresar_sabores():
    print(sabores)
    sabores = Sabor.get_all()
    return render_template('ingresar_pedido.html', sabores=sabores)