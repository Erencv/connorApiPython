from connect import connectDB
from pymongo import errors
import json
from bson.objectid import ObjectId
from bson import json_util


def read_all_data(db, collection_name):
    try:
        collection = db[collection_name]

        result = collection.find()

        for document in result:
            print(document)

    except Exception as e:
        print(f"An error occurred: {e}")

def to_json(data):
    return json.dumps(data)

def home():
    db = connectDB()
    try:
        collection = db["comment"]

        result = collection.find()
        
        return to_json(result)
        #for document in result:
            #return document

    except Exception as e:
        print(f"An error occurred: {e}")
    
def find_orders_containing_item(db, collection_name, item_name,lhs):
    try:
        collection = db[collection_name]

        query = { lhs : item_name}

        cursor = collection.find(query)

        result = list(cursor)

        for document in result:
            print(document)

        return result

    except Exception as e:
        print(f"An error occurred: {e}")

'''
@app.route('/connor/fight/<fight_id>/', methods=['GET'])
def get_fight_by_id(fight_id): 
    try:
        db = connectDB()
        documents = []  
        collection = db["fight"]
        query = {"fightId": fight_id }
        print(f"fight_id: {fight_id}")
        print(f"query: {query}") 
        cursor = collection.find(query)
        result = list(cursor)
        for document in result:
            documents.append(parse_json(document))
        return {'data': documents}
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return {'error': str(e)}
'''
#find_orders_containing_item(connectDB(), "fight", "15", "fightId")


def parse_json(data):
    return json.loads(json_util.dumps(data))

def get_collection(collection_name):
    db = connectDB()
    documents = []
    try:
        collection = db[collection_name]
        result = collection.find()
        for document in result:
            documents.append(parse_json(document))
        return {'data': documents}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {'error': str(e)}


print(get_collection("comment"))