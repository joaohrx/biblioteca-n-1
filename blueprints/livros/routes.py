from flask import render_template, request,  redirect, url_for,flash, session
from blueprints.livros import livros_bp
from models import Livro
import database


# Por enquanto em manutenção !!


@livros_bp.route("/")
def index():
    return render_template("index.html")
    


@livros_bp.route("/adicionar_livro", methods=["GET", "POST"])
def adicionar_livro():
    return render_template("adicionar_livro.html")


@livros_bp.route("/livros/editar/<int:livro_id>", methods=["GET", "POST"])
def editar_livro():
    return render_template("editar_livro.html")

@livros_bp.route("/home")
def home():
    return render_template("home.html")

@livros_bp.route("/perfil")
def perfil():
    return render_template("perfil.html")