from flask import render_template, Blueprint, request
from sqlalchemy import or_


from src.models import Product


search_blueprint = Blueprint("search", __name__)



@search_blueprint.route("/search/", methods=['GET'])
def search():
    search_term = request.args.get('query', '').lower()

    if search_term:
        # Split the search term into individual keywords
        keywords = search_term.split()

        # Construct a dynamic OR condition for each keyword for title and price
        condition_title = or_(*[Product.title.ilike(f'%{keyword}%') for keyword in keywords])
        condition_price = or_(*[Product.price.ilike(f'%{keyword}%') for keyword in keywords])
    

        # Combine the conditions using OR for title and price
        combined_condition = or_(condition_title, condition_price)

        # Use the combined condition in the query
        search_results = Product.query.filter(combined_condition).all()
    else:
        search_results = []

    return render_template('search/search_result.html', search_term=search_term, results=search_results)



