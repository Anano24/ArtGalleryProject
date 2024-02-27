from flask.cli import with_appcontext
import click

from src.extentions import db
from src.models import Product, Image, User, Role

@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Database creation in progress")
    db.drop_all()
    db.create_all()
    click.echo("Database created!")



@click.command("populate_db")
@with_appcontext
def populate_db():

    click.echo("Creating products")
    product_data = [
        {"title": "Shirt", "price": 100, "description":"", "images": ["gallery-she-01.png", "angel-black-01.png"]},
        {"title": "Shoes", "price": 200, "description":"", "images": ["gallery-gold-01.png", "medusa-black-01.png"]},
        {"title": "Angel", "price": 300, "description":"", "images": ["gallery-medusa-01.png", "fish-black-01.png"]},
        {"title": "Shirt", "price": 100, "description":"", "images": ["gallery-back-01.png"]},
        {"title": "Shoes", "price": 200, "description":"Add some description", "images": ["gallery-fish-01.png", "1.j.jpg"]},
        {"title": "Angel", "price": 300, "description":"Add some description for this artwork.", "images": ["gallery-angel-01.png", "angel-black-01.png"]},
        # Add more products as needed
    ]

    for data in product_data:
        product = Product(title=data["title"], price=data["price"], description=data["description"])
        product.create()

        # Create image objects for the product
        for filename in data["images"]:
            image = Image(filename=filename, product_id=product.id)
            image.create()




    click.echo("Creating role")
    adminrole = Role(name="Admin")
    userrole = Role(name='User')
    adminrole.create()
    userrole.create()

    click.echo("Creating test admin")
    user = User(
        username="adminuser",
        password="Admin1234",
        email="ananorobakidze24@gmail.com",
        role_id=adminrole.id,
    )

    user1 = User(username="Anano", password="Anano1234", email="test24@gmail.com", role_id=userrole.id)
    
    user.create()
    user1.create()


    click.echo("Database populated!")
