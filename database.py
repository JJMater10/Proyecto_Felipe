from pymongo import MongoClient  # Importa la clase MongoClient del módulo pymongo
import certifi  # Importa el módulo certifi

MONGO_URI = 'mongodb+srv://jaider:1234@cluster0.773wf9g.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'  # URI de conexión a MongoDB
ca = certifi.where()  # Obtiene la ubicación del archivo de certificados CA

def dbConnection():  # Define la función para establecer la conexión a la base de datos
    try:  # Inicia el bloque try para manejar excepciones
        client = MongoClient(MONGO_URI, tlsCAFile=ca)  # Crea un cliente MongoClient con la URI y el archivo de certificados CA
        db = client["dbb_clientes_app"]  # Accede a la base de datos "dbb_clientes_app"
    except ConnectionError:  # Captura la excepción ConnectionError en caso de error de conexión
        print('Error de conexión con la bdd')  # Imprime un mensaje de error
    return db  # Retorna el objeto de la base de datos

