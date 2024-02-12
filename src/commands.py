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
    product1 = Product(title='Shirt', price=100, img='1.j.jpg')
    product2 = Product(title='Shoes', price=200, img='1-01.jpeg')

    product1.create()
    product2.create()
    click.echo("Created products")


    click.echo("Database populated!")