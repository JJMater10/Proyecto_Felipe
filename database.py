from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://jaider:1234@cluster0.773wf9g.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["dbb_clientes_app"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db
