from flask import Flask, render_template, request, jsonify, redirect, url_for
from bson import ObjectId
import database as dbase  
from cliente import Cliente

db = dbase.dbConnection()

app = Flask(__name__)

# Rutas de la aplicación
@app.route('/')
def home():
    clientes = db['clientes']
    clientesReceived = list(clientes.find())
    # Convertimos ObjectId a strings
    for cliente in clientesReceived:
        cliente['_id'] = str(cliente['_id'])

    if 'PostmanRuntime' in request.headers.get('User-Agent'):
        # Si la solicitud proviene de Postman, devuelve JSON
        return jsonify(clientesReceived)
    else:
        # Si no, renderiza el template HTML
        return render_template('index.html', clientes=clientesReceived)

# Method Post
@app.route('/clientes', methods=['POST'])
def addCliente():
    clientes = db['clientes']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad = request.form['edad']

    if nombre and apellido and edad:
        cliente = Cliente(nombre, apellido, edad)
        clientes.insert_one(cliente.toDBCollection())
        response = jsonify({
            'nombre' : nombre,
            'apellido' : apellido,
            'edad' : edad
        })
        return redirect(url_for('home'))
    else:
        return notFound()

# Method delete
@app.route('/delete/<string:cliente_nombre>', methods=['DELETE'])
def delete(cliente_nombre):
    clientes = db['clientes']
    clientes.delete_one({'nombre' : cliente_nombre})
    return redirect(url_for('home'))

# Method Put
@app.route('/edit/<string:cliente_nombre>', methods=['POST'])
def edit(cliente_nombre):
    clientes = db['clientes']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad = request.form['edad']

    if nombre and apellido and edad:
        clientes.update_one({'nombre' : cliente_nombre}, {'$set' : {'nombre' : nombre, 'apellido' : apellido, 'edad' : edad}})
        response = jsonify({'message' : 'Cliente ' + cliente_nombre + ' actualizado correctamente'})
        return redirect(url_for('home'))
    else:
        return notFound()

@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(debug=True, port=4000)
