from flask import Blueprint

livros_bp = Blueprint("livros", __name__, template_folder="templates" )

from blueprints.livros import routes