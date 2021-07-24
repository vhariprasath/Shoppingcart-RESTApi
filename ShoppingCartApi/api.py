from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS


app = Flask(__name__)
client = MongoClient("mongodb://hariprasath:12345@localhost:27017/ShoppingCart")
db = client['ShoppingCart']
CORS(app)


@app.route('/item', methods=['POST', 'GET'])
def data():
    
    # POST a data to database
    if request.method == 'POST':
        body = request.json
        
        prod_name = body['name']
        prod_desc = body['description']
        prod_qty = body['quantity']
        prod_price = body['price']

        
        db['CartItems'].insert_one({
            
            "prod_name": prod_name,
            "prod_desc":prod_desc,
            "prod_qty":prod_qty,
            "prod_price":prod_price
        })
        return jsonify({
            'status': 'Data is posted to MongoDB!',
            
            'name': prod_name,
            'desc':prod_desc,
            'qty':prod_qty,
            'price':prod_price
        })
    
    # GET all data from database
    if request.method == 'GET':
        allData = db['CartItems'].find()
        dataJson = []
        for data in allData:
            id = data['_id']
            name = data['prod_name'],
            desc = data['prod_desc'],
            qty = data['prod_qty'],
            price = data['prod_price']
            dataDict = {
                'Id': str(id),
                'Name':name,
                'Description':desc,
                'Quantity':qty,
                'Price':price
                }
            dataJson.append(dataDict)
        print(dataJson)
        return jsonify(dataJson)

@app.route('/item/<string:id>', methods=['GET', 'DELETE', 'PUT'])
def onedata(id):

    # GET a specific data by id
    if request.method == 'GET':
        data = db['CartItems'].find_one({'_id': ObjectId(id)})
        prod_name = data['prod_name']
        prod_desc = data['prod_desc']
        prod_qty = data['prod_qty']
        prod_price=data['prod_price']
        dataDict = {
            'name': prod_name,
            'description': prod_desc,
            'quantity':prod_qty,
            'price':prod_price
        }
        print(dataDict)
        return jsonify(dataDict)
        
    # DELETE a data
    if request.method == 'DELETE':
        db['CartItems'].delete_many({'_id': ObjectId(id)})
        print('\n # Deletion successful # \n')
        return jsonify({'status': 'Data id: ' + id + ' is deleted!'})

    # UPDATE a data by id
    if request.method == 'PUT':
        body = request.json
        
        prod_name = body['name']
        prod_desc = body['description']
        prod_qty = body['quantity']
        prod_price = body['price']

        db['CartItems'].update_one(
            {'_id': ObjectId(id)},
            {
                "$set": {
                    "prod_name":prod_name,
                    "prod_desc":prod_desc,
                    "prod_qty":prod_qty,
                    "prod_price":prod_price
                }
            }
        )

        print('\n # Update successful # \n')
        return jsonify({'status': 'Item id: ' + id + ' is updated!'})

if __name__ == '__main__':
    app.debug = True
    app.run()