from flask import render_template, redirect, session, request, flash,url_for
from app import app
from app.models.user import User
from app.models.cliente import Cliente
from app.models.pedido import Pedido 
from app.models.relleno import Relleno
from app.models.empaque import Empaque
from app.models.producto import Producto
from app.models.sabor import Sabor
from app.models.extra import Extra      


@app.route('/nuevo_pedido/<int:cliente_id>/')
def nuevo_pedido(cliente_id):
    data={'id':cliente_id}
    rellenos = Relleno.get_all() 
    empaques = Empaque.get_all()
    productos = Producto.get_all()
    sabores = Sabor.get_all()
    extras = Extra.get_all()
    cliente = Cliente.get_by_id(data)
    return render_template('ingresar_pedido.html', rellenos=rellenos, empaques=empaques,cliente=cliente,productos=productos,sabores=sabores,extras=extras)

@app.route('/guardar_pedido/<int:cliente_id>/', methods=['POST'])
def guardar_pedido(cliente_id):
    fecha_ingreso = request.form.get('fecha_ingreso')
    fecha_pago = request.form.get('fecha_pago')
    fecha_entrega = request.form.get('fecha_entrega')
    caracteristicas = request.form.get('caracteristicas')
    tipo_de_entrega = request.form.get('tipo_entrega')
    precio_total = request.form.get('precio_total')
    sabores_id = request.form.get('sabores_id')
    relleno_id = request.form.get('relleno_id')
    empaques_id = request.form.get('empaques_id')
    extras_id = request.form.get('extras_id')
    clientes_id = cliente_id
    productos_id = request.form.get('productos_id')

    data = {
        'fecha_ingreso': fecha_ingreso,
        'fecha_pago': fecha_pago,
        'fecha_entrega': fecha_entrega,
        'caracteristicas': caracteristicas,
        'tipo_de_entrega': tipo_de_entrega,
        'precio_total': precio_total,
        'sabores_id': sabores_id,
        'relleno_id': relleno_id,
        'empaques_id': empaques_id,
        'extras_id': extras_id,
        'clientes_id': clientes_id,
        'productos_id': productos_id
    }

    Pedido.save(data)  

    return redirect(url_for('dashboard')) 