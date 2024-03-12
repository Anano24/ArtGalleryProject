from flask.cli import with_appcontext
import click

from src.extentions import db
from src.models import User, Role

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
