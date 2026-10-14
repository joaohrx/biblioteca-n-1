from flask import render_template, request, session, redirect, url_for
from blueprints.auth import auth_bp
import database


@auth_bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    pass

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    pass


@auth_bp.route("/logout")
def logout():
    pass