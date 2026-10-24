from flask import render_template, request,  redirect, url_for,flash, session
from blueprints.livros import livros_bp
from models import Livro
import database


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
        quantidade = request.form.get("quantidade")

        if not titulo or not autor:
            flash("Preencha o título e o autor.", "erro")
            return render_template("livros/formulario.html")

        livro = Livro(
            titulo=titulo,
            autor=autor,
            ano=int(ano) if ano else None,
            quantidade=int(quantidade),
            disponiveis=int(quantidade)
        )

        db.session.add(livro)
        db.session.commit()

        flash("Livro cadastrado com sucesso!")
        return redirect(url_for("livros.home"))

    return render_template("adicionar_livro.html")




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
        return redirect(url_for("livros.index"))

    return render_template("livros/editar.html", livro=livro)



@livros_bp.route("/livros/excluir/<int:id>", methods=["POST"])
def excluir_livro(id):
    livro = Livro.query.filter_by(id=id).first()

    if livro is None:
        return " O Livro não foi  encontrado"

    database.db.session.delete(livro)
    database.db.session.commit()

    flash("Livro excluído com sucesso!")
    return redirect(url_for("livros.index"))

@livros_bp.route("/home")
def home():
    livros_cadastrados = Livro.query.all()
    return render_template("home.html", livros_cadastrados=livros_cadastrados)

@livros_bp.route("/perfil")
def perfil():
    return render_template("perfil.html")

