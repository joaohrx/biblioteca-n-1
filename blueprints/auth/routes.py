from flask import render_template, request, session, redirect, url_for,flash
from models import Leitor
from werkzeug.security import generate_password_hash,check_password_hash

from blueprints.auth import auth_bp
import database

@auth_bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":

        nome=request.form.get("nome")
        email=request.form.get("email")
        senha=request.form.get("senha")

        if not nome or not email or not senha:
            flash("Preencha todos os campos.", "erro")
            return render_template("cadastro.html")

        flash("Cadastro realizado com sucesso!")
        return redirect(url_for("auth.login"))

    return render_template("cadastro.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email= request.form.get("email")
        senha= request.form.get("senha")

        usuario = Usuario.query.filter_by(email=email).first()

        if usuario and check_password_hash(usuario.senha, senha):
            session["usuario"] = usuario.id
            return redirect(url_for("livro.html"))

        flash("E-mail ou senha incorretos.")

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login.html"))