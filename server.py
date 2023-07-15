from app import app
from app.controllers import users
from app.controllers import clientes
from app.controllers import pedidos
from app.controllers import empaques
from app.controllers import rellenos
from app.controllers import productos
from app.controllers import sabores
from app.controllers import extras
from app.controllers import base_datos



if __name__ == "__main__":
    app.run(debug=True)
