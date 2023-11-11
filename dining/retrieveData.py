from pymongo import MongoClient

def fetch_data_from_mongodb():
    # Replace the connection string and database/collection names with your own values
    connection_string = "mongodb+srv://Rayan:Rayan@cluster0.wg76som.mongodb.net/?retryWrites=true&w=majority"
    db_name = "Halls"
    collection_name = "Berk"

    # Connect to MongoDB
    client = MongoClient(connection_string)

    # Access the specified database and collection
    db = client[db_name]
    collection = db[collection_name]

    # Specify your query here
    query = {}

    # Execute the query and retrieve the data
    result = collection.find(query)

    # Print or process the retrieved data
    for document in result:
        print(document)

    # Close the connection
    client.close()
    print("Connection to MongoDB closed")

if __name__ == "__main__":
    fetch_data_from_mongodb()
