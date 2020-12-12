from flask import Blueprint
from app_flask.app.generate.commands import create_admin, create_db
gen = Blueprint('gen',__name__,cli_group='generate')

gen.cli.add_command(create_db)
gen.cli.add_command(create_admin)
