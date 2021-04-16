from flask import Flask, request, jsonify
from flask_cors import cross_origin
from controllers.product_controller import ProductController


app = Flask(__name__)


@app.route('/')
def index():
    return 'Backend Server Starts.'


@app.route('/product', methods=['POST', 'GET'])
@cross_origin()
def product():
    if request.method == 'POST':
        product_details = request.get_json()
        print(dict(product_details))
        ProductController().add_product(product=product_details)
        return {"status": 200}
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
        return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)