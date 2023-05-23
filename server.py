from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS
import os
import random

PRODUCTS = [
    {"id": 1, "name": "Product 1", "description": "This is product 1", "quantity": 10},
    {"id": 2, "name": "Product 2", "description": "This is product 2", "quantity": 20},
]

ORDERS = [
    # We will add orders here later
]

app = Flask(__name__, static_folder='frontend/public')

@app.route("/products", methods=["GET", "POST"])
def products():
    if request.method == "GET":
        return jsonify(PRODUCTS)
    else:
        # For simplicity, we're not doing any validation here
        new_product = request.json
        new_product["id"] = max(p["id"] for p in PRODUCTS) + 1
        PRODUCTS.append(new_product)
        return jsonify(new_product), 201

@app.route("/products/<int:id>", methods=["PUT"])
def update_product(id):
    product = next(p for p in PRODUCTS if p["id"] == id)
    product.update(request.json)
    return jsonify(product)

@app.route("/orders", methods=["GET", "POST"])
def orders():
    if request.method == "GET":
        return jsonify(ORDERS)
    else:
        new_order = request.json
        product = next(p for p in PRODUCTS if p["id"] == new_order["productId"])
        product["quantity"] -= new_order["quantity"]
        new_order["id"] = max((o["id"] for o in ORDERS), default=0) + 1
        ORDERS.append(new_order)
        return jsonify(new_order), 201

CORS(app)

@app.route("/rand")
def hello():
    return str(random.randint(0, 100))

@app.route("/", defaults={"path": ''})
@app.route("/<path:path>")
def home(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    app.run(debug=True, port=5001)
