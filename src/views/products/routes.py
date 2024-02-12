from flask import render_template, redirect, url_for, Blueprint

from src.models import Product



product_blueprint = Blueprint("product", __name__)

@product_blueprint.route('/product/<int:id>')
def product(id):
    product_id = Product.query.get(id)
    return render_template('products/product.html', product=product_id)


@product_blueprint.route('/products')
def products():
    products = Product.query.all()
    return render_template('products/product_list.html', products=products)




