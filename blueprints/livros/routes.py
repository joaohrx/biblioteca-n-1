from flask import render_template, request, redirect, url_for,flash
from blueprints.livros import livros_bp
from models import Livro
from database import \_Sessao
from sqlalchemy import select


from crud import (
    adicionar_livro as cadastrar_livro,
    buscar_livro_titulo,
    emprestar_livro as realizar_emprestimo,
    leitor_existe,
    filtrar_livros_emprestados,
    filtra_livros_genero,
    filtrar_livros_autor,
    devolver_livro as realizar_devolucao,
    editar_livros
)



*# Por enquanto em manutenção !!*


@livros_bp.route("/")
def index():
    return render_template("index.html")



@livros_bp.route("/livros/adicionar/", methods=["GET", "POST"])
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



@livros_bp.route("/livros/editar", methods=["GET", "POST"])
def editar_livro():
    if request.method == "POST":

        titulo = request.form.get("titulo")
        descricao = request.form.get("descricao")

        if titulo and descricao:
            editar_livros(titulo, descricao)
            flash("Descrição atualizada")
        else:
            flash("Informe o título e a nova descrição.")

        return redirect(url_for(""))

    return render_template("")

@livros_bp.route("/livros/excluir/\<int:id>", methods=["POST"])
def excluir_livro(id):
    with \_Sessao() as sessao:
        livro = sessao.get(Livro, id)

        if livro is None:
            flash("Livro não encontrado.")
            return redirect(url_for(""))

        if livro.leitor:
            flash("Não é possível excluir um livro emprestado.")
            return redirect(url_for(""))

        sessao.delete(livro)
        sessao.commit()

    flash("Livro excluído com sucesso!")
    return redirect(url_for(""))


@livros_bp.route("/livros/emprestar", methods=["GET", "POST"])
def emprestar_livro():
    leitores = leitor_existe()

    if request.method == "POST":
        titulo = request.form.get("titulo")
        leitor_nome = request.form.get("leitor_nome")

        if titulo and leitor_nome:
            realizar_emprestimo(titulo, leitor_nome)
            flash("Empréstimo processado. Confira se o livro e o leitor existem e se o livro está disponível.")
        else:
            flash("Informe o título do livro e o nome do leitor.")

        return redirect(url_for("livros.emprestar_livro"))

    return render_template("emprestar_livro.html", leitores=leitores)



@livros_bp.route("/livros/devolver", methods=["GET", "POST"])
def devolver_livro():
    if request.method == "POST":
        titulo = request.form.get("titulo")
        leitor_nome = request.form.get("leitor_nome")

        if titulo and leitor_nome:
            realizar_devolucao(titulo, leitor_nome)
            flash("Devolução processada. Confira se o empréstimo existia.")
        else:
            flash("Informe o título do livro e o nome do leitor.")

        return redirect(url_for("livros.devolver_livro"))

    return render_template(
        "devolver_livro.html",
        leitores=leitor_existe()
    )



@livros_bp.route("/livros/filtrar", methods=["GET", "POST"])
def filtrar_livro():
    livros = []
    tipo = request.values.get("tipo")
    valor = request.values.get("valor")

    if tipo == "genero" and valor:
        livros = filtra_livros_genero(valor)

    elif tipo == "autor" and valor:
        livros = filtrar_livros_autor(valor)

    elif tipo == "emprestados":
        livros = filtrar_livros_emprestados()

    return render_template(
        "filtrar_livro.html",
        livros=livros
    )



@livros_bp.route("/home")
def home():
    with \_Sessao() as sessao:
        livros_cadastrados = sessao.scalars(select(Livro)).all()

    return render_template(
        "home.html",
        livros_cadastrados=livros_cadastrados
    )

@livros_bp.route("/perfil")
def perfil():
    return render_template("perfil.html")