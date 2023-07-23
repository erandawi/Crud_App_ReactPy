from pymongo import MongoClient

# Replace <URL> with your MongoDB Atlas connection string
uri = "mongodb+srv://eranda:Poson*27@cluster0.qljkuq6.mongodb.net/"
client = MongoClient(uri)

# Replace <database-name> with the name of your database
db = client["DB"]

# Replace <collection-name> with the name of your collection
collection = db["DB"]

# check the connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB")
except Exception as e:
    print(e)

document = {"name": "Daniel","age": 36}

# Insert the document into the collection
insert_result = collection.insert_one(document)

# Print the ID of the inserted document 
print("Inserted Document ID:", insert_result.inserted_id)

client.close()