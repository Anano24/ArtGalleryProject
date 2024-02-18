from flask import render_template, redirect, url_for, Blueprint, request


from src.models import Product




product_blueprint = Blueprint("product", __name__)

@product_blueprint.route('/product/<int:id>')
def product(id):
     # Get the current product
    product_id = Product.query.get_or_404(id)

    # Query other products excluding the current one
    other_products = Product.query.filter(Product.id != id)

    # Pagination for other products
    page = request.args.get('page', 1, type=int)
    per_page = 4  # Number of other products per page
    other_products_pagination = other_products.paginate(page=page, per_page=per_page, error_out=False)
    other_products_on_page = other_products_pagination.items
    total_pages = other_products_pagination.pages

    return render_template('products/product.html', product=product_id, other_products=other_products_pagination, other_products_on_page=other_products_on_page, total_pages=total_pages, page=page)




@product_blueprint.route('/products')
def products():

    page = request.args.get('page', 1, type=int)
    per_page = 5  # Number of products per page
    pagination = Product.query.paginate(page=page, per_page=per_page, error_out=False)
    products_on_page = pagination.items
    total_pages = pagination.pages

    return render_template('products/product_list.html', products=pagination, total_pages=total_pages, products_on_page=products_on_page, page=page)




