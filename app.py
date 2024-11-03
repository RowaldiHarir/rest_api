from flask import Flask, jsonify, request

app = Flask(__name__)

# Data dummy
products = [
    {"id": 1, "name": "Produk 1", "price": 10000},
    {"id": 2, "name": "Produk 2", "price": 20000},
]

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((prod for prod in products if prod["id"] == product_id), None)
    return jsonify(product) if product else ('', 404)

@app.route('/api/products', methods=['POST'])
def add_product():
    new_product = request.get_json()
    products.append(new_product)
    return jsonify(new_product), 201

if __name__ == '__main__':
    app.run(debug=True)
