from flask import render_template, request,  redirect, url_for,flash, session
from blueprints.livros import livros_bp
from models import Livro
import database


from crud import (
    adicionar_livro,buscar_livro_titulo
)

# Por enquanto em manutenção !!


@livros_bp.route("/")
def index():
    return render_template("index.html")
    


@livros_bp.route("/livros/adicionar/<int:livro_id>", methods=["GET", "POST"])
def adicionar_livro():
    if request.method == "POST":
        titulo = request.form.get("titulo")
        autor = request.form.get("autor")
        ano = request.form.get("ano")
        genero = request.form.get("genero")
        descricao = request.form.get("descricao")

        if not titulo or not autor or not ano or not genero or not descricao:
            flash("Preencha todos os devidos campos por favor !")
            return render_template("")

        adicao = {
            "titulo": titulo,
            "ano": int(ano),
            "genero": genero,
            "descricao": descricao
        }

        cadastrar_livro(adicao, autor)


        flash("Livro cadastrado com sucesso!")
        return redirect(url_for(""))

    return render_template("")


@livros_bp.route("/livros/buscar", methods=["GET", "POST"])
def buscar_livro():

    livro=None

    if request.method == "POST":
        titulo = request.form.get("titulo")

        if titulo:
            livro = buscar_livro_titulo(titulo)

        if livro is None:
            flash("Livro não encontrado.")

    return render_template("", livro=livro)




@livros_bp.route("/livros/editar/<int:id>", methods=["GET", "POST"])
def editar_livro(id):
    livro=Livro.query.filter_by(id=id).first()

    if livro is None:
        return "Livro não encontrado"

    if request.method == "POST":
        livro.titulo =request.form.get("titulo")
        livro.autor =request.form.get("autor")

        ano = request.form.get("ano")
        quantidade = request.form.get("quantidade")

        livro.ano = int(ano) if ano else None
        livro.quantidade = int(quantidade)

        database.db.session.commit()

        flash("Livro atualizado com sucesso!")
        return redirect(url_for(""))

    return render_template("", livro=livro)



@livros_bp.route("/livros/excluir/<int:id>", methods=["POST"])
def excluir_livro(id):
    livro = Livro.query.filter_by(id=id).first()

    if livro is None:
        return " O Livro não foi  encontrado"

    database.db.session.delete(livro)
    database.db.session.commit()

    flash("Livro excluído com sucesso!")
    return redirect(url_for(""))





@livros_bp.route("/livros/emprestar/<int:id>", methods=["POST"])
def emprestar_livro(id):

    livro=Livro.query.filter_by(id=id).first()

    if livro is None:
        return "Livro não encontrado"

    if livro.disponiveis > 0:

        livro.disponiveis = livro.disponiveis - 1

        database.db.session.commit()
        flash("Livro emprestado!")
    else:
        flash("Não há livros disponíveis para empréstimo no momento!.")

    return redirect(url_for(""))




@livros_bp.route("/livros/devolver/<int:id>", methods=["POST"])
def devolver_livro(id):
    livro = Livro.query.filter_by(id=id).first()

    if livro is None:
        return "Livro não encontrado"

    if livro.disponiveis < livro.quantidade:
        livro.disponiveis = livro.disponiveis + 1
        database.db.session.commit()
        flash("Livro devolvido com sucesso!")
    else:
        flash("Todos os livros já estão disponíveis.")

    return redirect(url_for(""))


@livros_bp.route("/home")
def home():
    livros_cadastrados = Livro.query.all()
    return render_template("home.html", livros_cadastrados=livros_cadastrados)

@livros_bp.route("/perfil")
def perfil():
    return render_template("perfil.html")

