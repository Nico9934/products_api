from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/products-api"
mongo = PyMongo(app)

@app.route("/v1/api/products", methods=['GET'])
def get_products():
    product_list = []
    data = mongo.db.products.find()
    for product in data:
        product['_id'] = str(product['_id'])
        product_list.append(product)
    return jsonify(product_list)


@app.route("/v1/api/products", methods=['POST'])
def add_product():
    product_found = mongo.db.products.find_one({
        "product" : request.json['product']
    })
    if product_found:
        return jsonify({'message': "El producto ya existe"})
    new_product = {
        'product' : request.json['product'],
        'category' : request.json['category'],
        'salePrice' : request.json['salePrice'],
        'costPrice' : request.json['costPrice']
    }

    saved_product = mongo.db.products.insert_one(new_product)
    new_product['_id'] = str(saved_product.inserted_id)
    print(new_product)
    return jsonify({'message': 'Producto agregado con exito'})


@app.route("/v1/api/products/<product_id>", methods=['GET'])
def get_product(product_id):
    product_object_id = ObjectId(product_id)
    product_found = mongo.db.products.find_one({'_id' : product_object_id})
    if not product_found:
        return jsonify({"message" : "El producto no existe"})
    product_found['_id'] = str(product_object_id)
    return jsonify(product_found)


@app.route("/v1/api/products/<product_id>", methods=['DELETE'])
def remove_product(product_id):
    product_object_id = ObjectId(product_id)
    product_found = mongo.db.products.find_one({'_id' : product_object_id})
    if not product_found: 
        return jsonify({"message" : "El producto no existe"})
    product_removed = mongo.db.products.delete_one({'_id' : product_object_id})

    return jsonify({'message:' : "Producto eliminado con exito"})


@app.route("/v1/api/products/<product_id>", methods=['PUT'])
def edit_product(product_id):
    product_object_id = ObjectId(product_id)
    product_found = mongo.db.products.find_one({'_id': product_object_id})
    if not product_found: 
        return jsonify({'message' : "El producto no existe"})
    
    product_update = {
        '_id' : product_object_id, 
        "product" : request.json.get('product') or product_found['product'],
	    "category": request.json.get('category') or product_found['category'],
	    "costPrice": request.json.get('costPrice') or product_found['costPrice'],
        "salePrice": request.json.get('salePrice') or product_found['salePrice'], 
    }
    
    response = mongo.db.products.find_one_and_update({'_id' : product_object_id}, {'$set': product_update })
    product_update['_id'] = str(product_update['_id'])
    print(response)
    return jsonify({'message': "Producto actualizado con exito"})

if __name__ == "__main__":
    app.run(debug=True)
    with app.app_context():
        print(f"Base de datos conectada: {mongo.db}")