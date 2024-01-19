from flask import Flask, request, jsonify
from connect import connectDB
from pymongo import errors
import json
from bson.objectid import ObjectId
from bson import json_util

app = Flask(__name__)

def parse_json(data):
    return json.loads(json_util.dumps(data))

def to_json(data):
    return json.dumps(data, default=json_util.default)

@app.route('/connor/getall/<collection_name>/', methods=['GET'])
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

@app.route('/connor/fight/<fight_id>/', methods=['GET'])
def get_fight_by_id(fight_id): 
    try:
        db = connectDB()
        documents = []  
        collection = db["fight"]
        query = {"fightId": fight_id }
        cursor = collection.find(query)
        result = list(cursor)
        for document in result:
            documents.append(parse_json(document))
        return {'data': documents}
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return {'error': str(e)}

@app.route('/connor/fighter/<fighter_id>/', methods=['GET'])
def get_fighter_by_id(fighter_id): 
    try:
        db = connectDB()
        documents = []  
        collection = db["fighter"]
        query = {"fighterId": fighter_id }
        cursor = collection.find(query)
        result = list(cursor)
        for document in result:
            documents.append(parse_json(document))
        return {'data': documents}
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return {'error': str(e)}

@app.route('/connor/comment/<comment_id>/', methods=['GET'])
def get_comment_by_id(comment_id): 
    try:
        db = connectDB()
        documents = []  
        collection = db["comment"]
        query = {"commentId": comment_id }
        cursor = collection.find(query)
        result = list(cursor)
        for document in result:
            documents.append(parse_json(document))
        return {'data': documents}
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return {'error': str(e)}

@app.route('/connor/post/comment/', methods=['POST'])
def post_comment():
    try:
        db = connectDB()
        collection = db["comment"]
        data = request.get_json()
        result = collection.insert_one(data)
        if result.acknowledged:
            return {'message': 'Comment successfully created', 'id': str(result.inserted_id)}
        else:
            return {'error': 'Comment creation failed'}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {'error': str(e)}

if __name__ == '__main__':
    app.run(debug=True)
