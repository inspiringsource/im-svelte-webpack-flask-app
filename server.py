from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
import random

app = Flask(__name__, static_folder='frontend/public')
CORS(app)

basedir = os.path.abspath(os.path.dirname(__file__))
db_dir = os.path.join(basedir, 'DB')
os.makedirs(db_dir, exist_ok=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(db_dir, 'test.db')

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "quantity": self.quantity
        }

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product = db.relationship('Product', backref=db.backref('orders', lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id
        }

@app.route("/products", methods=["GET", "POST"])
def products():
    if request.method == "GET":
        products = Product.query.all()
        return jsonify([product.to_dict() for product in products])
    else:
        new_product_data = request.json
        new_product = Product(name=new_product_data["name"], description=new_product_data["description"], quantity=new_product_data["quantity"])
        db.session.add(new_product)
        db.session.commit()
        return jsonify(new_product.to_dict()), 201

@app.route("/products/<int:id>", methods=["PUT"])
def update_product(id):
    product = Product.query.get(id)
    product_data = request.json
    product.name = product_data["name"]
    product.description = product_data["description"]
    product.quantity = product_data["quantity"]
    db.session.commit()
    return jsonify(product.to_dict())

@app.route("/orders", methods=["GET", "POST"])
def orders():
    if request.method == "GET":
        orders = Order.query.all()
        return jsonify([order.to_dict() for order in orders])
    else:
        new_order_data = request.json
        product = Product.query.get(new_order_data["productId"])
        product.quantity -= new_order_data["quantity"]
        new_order = Order(product_id=product.id)
        db.session.add(new_order)
        db.session.commit()
        return jsonify(new_order.to_dict()), 201

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
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)
