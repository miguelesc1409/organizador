
from pymongo.mongo_client import MongoClient

uri = "mongodb://mych:kontra@cluster0-shard-00-00.3mn1v.mongodb.net:27017,cluster0-shard-00-01.3mn1v.mongodb.net:27017,cluster0-shard-00-02.3mn1v.mongodb.net:27017/?ssl=true&replicaSet=atlas-n9nsx5-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri)
db = client['organizador']  # Cambia por el nombre de tu base de datos
collection = db['peliculas']  # Cambia por el nombre de tu colección

mensaje = collection.find_one() 
print(mensaje)