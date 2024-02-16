from flask.cli import with_appcontext
import click

from src.extentions import db
from src.models import Product, Image

@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Database creation in progress")
    db.drop_all()
    db.create_all()
    click.echo("Database created!")


# @click.command("populate_db")
# @with_appcontext
# def populate_db():

#     click.echo("Creating products")
#     product1 = Product(title='Shirt', price=100, img='angel-black-01.png')
#     product2 = Product(title='Shoes', price=200, img='medusa-black-01.png')
#     product3 = Product(title= "Angel", price=300, img="fish-black-01.png")
#     product4 = Product(title='Shoes', price=200, "images": ["medusa-black-01.png", "shoes-02.png"])
#     product5 = Product(title= "Angel", price=300, img="angel-black-01.png")
#     product6 = Product(title= "Angel", price=300, img="fish-black-01.png")


#     product1.create()
#     product2.create()
#     product3.create()
#     product4.create()
#     product5.create()
#     product6.create()
#     click.echo("Created products")


#     click.echo("Database populated!")
    

@click.command("populate_db")
@with_appcontext
def populate_db():

    click.echo("Creating products")
    product_data = [
        {"title": "Shirt", "price": 100, "description":"", "images": ["angel-black-01.png"]},
        {"title": "Shoes", "price": 200, "description":"", "images": ["medusa-black-01.png"]},
        {"title": "Angel", "price": 300, "description":"", "images": ["fish-black-01.png"]},
        {"title": "Shirt", "price": 100, "description":"", "images": ["9qa.png"]},
        {"title": "Shoes", "price": 200, "description":"Add some description", "images": ["1.j.jpg", "1.j.jpg"]},
        {"title": "Angel", "price": 300, "description":"Add some description for this artwork.", "images": ["1-01.jpeg", "angel-black-01.png"]},
        # Add more products as needed
    ]

    for data in product_data:
        product = Product(title=data["title"], price=data["price"], description=data["description"])
        product.create()

        # Create image objects for the product
        for filename in data["images"]:
            image = Image(filename=filename, product_id=product.id)
            image.create()

    click.echo("Database populated!")
