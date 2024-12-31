from flask import Flask, render_template
from pymongo import MongoClient
from bson.objectid import ObjectId
import logging

app = Flask(__name__)

# Configuración del logger
logging.basicConfig(filename='app.log', 
                    level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

uri = "mongodb://mych:kontra@cluster0-shard-00-00.3mn1v.mongodb.net:27017,cluster0-shard-00-01.3mn1v.mongodb.net:27017,cluster0-shard-00-02.3mn1v.mongodb.net:27017/?ssl=true&replicaSet=atlas-n9nsx5-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri)
db = client['organizador']  # Cambia por el nombre de tu base de datos
collection = db['peliculas']  # Cambia por el nombre de tu colección

@app.route('/')
def home():
    colecciones = sorted(db.list_collection_names())
    contenido = collection.find()  # Obtiene un documento de la colección
    logging.info(contenido)
    return render_template('index.html', colecciones=colecciones, contenido=contenido)


@app.route('/categorias/<coleccion>',methods=['GET'])
def categorias(coleccion):
    try:
        collection = db[coleccion] 
        nombre_coleccion = coleccion
        colecciones = sorted(db.list_collection_names())
        contenido = collection.find()  # Obtiene un documento de la colección
        return render_template('categorias.html', colecciones=colecciones, contenido=contenido, nombre_categoria=nombre_coleccion)
    except Exception as e:
        print(f"No se pudo conectar a MongoDB: {e}")

    
@app.route('/edit/<document_id>&<coleccion>')
def edit(coleccion,document_id):
    collection = db[coleccion] 
    document = collection.find_one({"_id": ObjectId(document_id)})
    return render_template('edit.html')

if __name__ == '__main__':
    app.run(debug=True)