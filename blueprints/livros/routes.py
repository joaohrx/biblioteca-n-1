from flask import render_template, request, session, redirect, url_for
from blueprints.auth import auth_bp
import database


@auth_bp.route("/")
def index():
    pass
