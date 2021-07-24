# Shoppingcart-RESTApi
Handles CRUD Operations of Cart Using Flask, Python, MongoDB

Step 1 (Mongo SetUp) - 
```bash
Activate MongoDb Server in a Terminal
$ mongod
Open new terminal
$ mongo
```
Step 2 (Db & Collection Creation) -
```bash
    > use ShoppingCart                                                                 
    > db.createUser({user:'hariprasath', pwd:'12345', roles:['readWrite', 'dbAdmin']})
    > db.createCollection('CartItems')
```
Step 3 (Packages) -
```bash
    Flask , PyMongo
```
Step 4 (Run file) - 
```bash
    python app.py
```
Step 5 (Request to Server - Postman) -
```bash
Sample Request :
  {
            
            "name": "XXX",
            "description":"YYY",
            "quantity":"xxx",
            "price":"yyy"

}
```
Step 6 (Request & Types) -
```bash
    POST http://localhost:5000/item (Create Item)
    
    GET http://localhost:5000/item (Read All Items)
    
    GET http://localhost:5000/item/{:id} (Read Specific Item)
    
    PUT http://localhost:5000/item/{:id} (Update Specific Item)
    
    DELETE http://localhost:5000/item/{:id} (Delete Specific Item)
    

```

