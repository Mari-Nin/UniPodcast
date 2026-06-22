import click
from flask.cli import with_appcontext
from click import command

from src.models import User,Video,Rubric,Category
from src.ext import db

@command('init_db')
@with_appcontext
def init_db():
    click.echo('Initializing database...')

    db.drop_all()
    db.create_all()
    admin_admin = User(username='admin',password='123456',role='admin')
    db.session.add(admin_admin)
    db.session.commit()

    click.echo('Done!')

@command('populate_db')
@with_appcontext
def populate_db():
    click.echo('Populating database...')



    click.echo('Done!')
