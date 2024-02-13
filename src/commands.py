from flask.cli import with_appcontext
import click

from src.extentions import db
from src.models import Product

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
    product1 = Product(title='Shirt', price=100, img='angel-black-01.png')
    product2 = Product(title='Shoes', price=200, img='medusa-black-01.png')
    product3 = Product(title= "Angel", price=300, img="fish-black-01.png")
    product4 = Product(title='Shoes', price=200, img='medusa-black-01.png')
    product5 = Product(title= "Angel", price=300, img="angel-black-01.png")
    product6 = Product(title= "Angel", price=300, img="fish-black-01.png")


    product1.create()
    product2.create()
    product3.create()
    product4.create()
    product5.create()
    product6.create()
    click.echo("Created products")


    click.echo("Database populated!")