
from flask import render_template, request, session, redirect, url_for, flash
from sqlalchemy import select
from werkzeug.security import generate_password_hash, check_password_hash

from blueprints.auth import auth_bp
from database import _Sessao
from models import Leitor


@auth_bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")

        if not nome or not email or not senha:
            flash("Preencha todos os campos.", "erro")
            return render_template("cadastro.html")

        with _Sessao() as sessao:
            query = select(Leitor).where(
                (Leitor.email == email) | (Leitor.nome == nome)
            )
            usuario_existente = sessao.scalar(query)

            if usuario_existente:
                flash("Nome ou e-mail já cadastrado.", "erro")
                return render_template("cadastro.html")

            novo_leitor = Leitor(
                nome=nome,
                email=email,
                senha_hash=generate_password_hash(senha)
            )

            sessao.add(novo_leitor)
            sessao.commit()

        flash("Cadastro realizado com sucesso!", "sucesso")
        return redirect(url_for("auth.login"))

    return render_template("cadastro.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")

        with _Sessao() as sessao:
            query = select(Leitor).where(Leitor.email == email)
            usuario = sessao.scalar(query)

            if usuario and check_password_hash(usuario.senha_hash, senha):
                session["usuario"] = usuario.id
                return redirect(url_for("livros.home"))

        flash("E-mail ou senha incorretos.", "erro")

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.pop("usuario", None)
    flash("Você saiu da sua conta.", "sucesso")
    return redirect(url_for("auth.login"))
