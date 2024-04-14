# Importa clases y funciones necesarias de Flask
from flask import Flask, render_template, request, jsonify, redirect, url_for  
# Importa la clase ObjectId de la biblioteca bson
from bson import ObjectId  
# Importa el módulo 'database' como 'dbase'
import database as dbase  
# Importa la clase Cliente del módulo cliente
from cliente import Cliente  

# Establece una conexión a la base de datos MongoDB utilizando la función dbConnection() del módulo 'database'
db = dbase.dbConnection()

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Define la ruta principal de la aplicación
@app.route('/')
def home():
    # Obtiene la colección de clientes de la base de datos
    clientes = db['clientes']  
    # Obtiene todos los documentos de la colección 'clientes'
    clientesReceived = list(clientes.find())  
    
    # Convierte los ObjectId a strings para que sean serializables
    for cliente in clientesReceived:
        cliente['_id'] = str(cliente['_id'])

    # Verifica si la solicitud proviene de Postman
    if 'PostmanRuntime' in request.headers.get('User-Agent'):
        # Si la solicitud proviene de Postman, devuelve la lista de clientes en formato JSON
        return jsonify(clientesReceived)
    else:
        # Si no, renderiza el template HTML 'index.html' y pasa la lista de clientes como contexto
        return render_template('index.html', clientes=clientesReceived)

# Define la ruta para agregar un nuevo cliente mediante un método POST
@app.route('/clientes', methods=['POST'])
def addCliente():
    # Obtiene la colección de clientes de la base de datos
    clientes = db['clientes']  
    # Obtiene el nombre del cliente desde el formulario
    nombre = request.form['nombre']  
    # Obtiene el apellido del cliente desde el formulario
    apellido = request.form['apellido']  
    # Obtiene la edad del cliente desde el formulario
    edad = request.form['edad']  

    # Verifica si se proporcionaron valores para nombre, apellido y edad
    if nombre and apellido and edad:
        # Crea una instancia de la clase Cliente con los datos proporcionados
        cliente = Cliente(nombre, apellido, edad)
        # Inserta el cliente en la colección de clientes
        clientes.insert_one(cliente.toDBCollection())
        # Redirige a la página principal
        return redirect(url_for('home'))
    else:
        # Si no se proporcionaron todos los datos requeridos, retorna un error 404
        return notFound()

# Define la ruta para eliminar un cliente mediante un método DELETE
@app.route('/delete/<string:cliente_nombre>', methods=['DELETE'])
def delete(cliente_nombre):
    # Obtiene la colección de clientes de la base de datos
    clientes = db['clientes']  
    # Elimina el cliente con el nombre proporcionado de la colección de clientes
    clientes.delete_one({'nombre': cliente_nombre})
    # Redirige a la página principal
    return redirect(url_for('home'))

# Define la ruta para editar un cliente mediante un método POST
@app.route('/edit/<string:cliente_nombre>', methods=['POST'])
def edit(cliente_nombre):
    # Obtiene la colección de clientes de la base de datos
    clientes = db['clientes']  
    # Obtiene el nuevo nombre del cliente desde el formulario
    nombre = request.form['nombre']  
    # Obtiene el nuevo apellido del cliente desde el formulario
    apellido = request.form['apellido']  
    # Obtiene la nueva edad del cliente desde el formulario
    edad = request.form['edad']  

    # Verifica si se proporcionaron valores para nombre, apellido y edad
    if nombre and apellido and edad:
        # Actualiza los datos del cliente con el nombre proporcionado en la colección de clientes
        clientes.update_one({'nombre': cliente_nombre}, {'$set': {'nombre': nombre, 'apellido': apellido, 'edad': edad}})
        # Redirige a la página principal
        return redirect(url_for('home'))
    else:
        # Si no se proporcionaron todos los datos requeridos, retorna un error 404
        return notFound()

# Maneja el error 404
@app.errorhandler(404)
def notFound(error=None):
    # Crea un mensaje de error personalizado
    message = {
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    # Retorna el mensaje de error como una respuesta JSON con código de estado 404
    response = jsonify(message)
    response.status_code = 404
    return response

# Si se ejecuta este script directamente, inicia la aplicación Flask
if __name__ == '__main__':
    # Inicia la aplicación en modo de depuración y en el puerto 4000
    app.run(debug=True, port=4000)
