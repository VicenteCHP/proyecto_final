from flask import render_template, redirect, session, request, flash
from app import app
import os
from app.models.user import User
from app.models.cliente import Cliente
from app.models.pedido import Pedido 
from app.models.relleno import Relleno 

@app.route('/nuevo_pedido', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        file = request.files['foto']
        filename = file.filename
        file.save(os.path.join('img_uploads', filename))
        return 'Imagen subida exitosamente'

    return render_template('ingresar_pedido.html')