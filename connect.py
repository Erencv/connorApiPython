from pymongo import MongoClient


# First of all, install the pymongo using pip
# python -m pip install "pymongo[srv]"
def connectDB():
    # Replace the connection string with your MongoDB connection string
    # You can obtain the connection string from your MongoDB Atlas dashboard or configure it locally
    # For example, if your database is running on localhost, the connection string might look like this:
    # "mongodb://localhost:27017/"

    connection_string = "mongodb://admin:pass@localhost:27017/?authMechanism=DEFAULT"
    client = MongoClient(connection_string)

    # Access a specific database (replace "your_database_name" with your actual database name)
    db = client.connor
    print("Connection established to your db")
    return db
    # Close the connection when you're done
    # client.close()

