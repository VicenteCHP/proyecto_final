from flask import render_template, redirect, session, request, flash
from app import app
from app.models.user import User
from app.models.cliente import Cliente
from app.models.pedido import Pedido 
from app.models.empaque import Empaque

@app.route('/nuevo_pedido')
def mostrar_empaques():
    empaques = Empaque.get_all()
    return render_template('ingresar_pedido.html', empaques=empaques)