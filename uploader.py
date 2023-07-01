
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json

uri = "mongodb+srv://arkavo:linebs14@2dm.glvekuw.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

with open("JSON_OUT_CrI3.json", "r") as f:
    data = json.load(f)

print(data["Blocks"])

# Get the database and collection
db = client["2DM"]
collection = db["CrCl3"]

# Insert the data
collection.insert_one(data)

# Print the inserted document's ID
print(f"Inserted document with ID: {data['_id']}")

# Close the connection
client.close()