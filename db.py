from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv('MONGO_USER')
passw = os.getenv('MONGO_PASS')

uri = f"mongodb+srv://{user}:{passw}@cluster0.g4gozmk.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)