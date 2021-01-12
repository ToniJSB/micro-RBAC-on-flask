from flask import Blueprint
from app_flask.app.cli.generate import create_admin, create_db
from app_flask.app.cli.babel import init,update,compile
gen = Blueprint('gen',__name__,cli_group='generate')
gen.cli.add_command(create_db)
gen.cli.add_command(create_admin)

translate = Blueprint('trans',__name__,cli_group='babel')
translate.cli.add_command(init)
translate.cli.add_command(compile)
translate.cli.add_command(update)