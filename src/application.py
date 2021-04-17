from flask import Flask, request, jsonify, Response
from controllers.product_controller import ProductController
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/product/*": {"origins": "*"}})

@app.route('/')
def index():
    resp = Response('Backend Server Starts.')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/product', methods=['POST', 'GET'])
def product():
    if request.method == 'POST':
        product_details = request.get_json()
        print(dict(product_details))
        ProductController().add_product(product=product_details)
        resp = Response({"status": 200})
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    else:
        category_name = request.args.get("category")
        id = request.args.get("id")
        if category_name:
            if category_name == "all":
                result = ProductController().get_product()
            else:
                result = ProductController().get_product_category(category=category_name)
        if id:
            result = ProductController().get_product_id(id=id)
        resp = Response(jsonify(result))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0')
