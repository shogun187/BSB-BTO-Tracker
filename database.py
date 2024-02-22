import json

from pymongo import MongoClient

# Connect to MongoDB (make sure MongoDB server is running)
client = MongoClient('mongodb+srv://shaugntan:T0024416z.@flats.dey3g18.mongodb.net/')

# Specify the database and collection name
db = client['flats']
collection = db['flats']

# Load the JSON file
with open('flats.json') as f:
    data = json.load(f)

# Insert the JSON data into the collection
for flat in data:

    availability = flat.get("available")
    flat.pop("available")
    query = flat
    update_document = {
        "$set": {
            "available" : availability
        }
    }
    collection.update_one(flat, update_document, upsert=True)

# Close the MongoDB connection
client.close()
