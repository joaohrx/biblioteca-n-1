
from flask import render_template, request, redirect,url_for, flash, session
from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload

from blueprints.livros import livros_bp
from database import _Sessao
from models import Livro, Autor, Leitor



@livros_bp.route("/")
def index():
    return render_template("index.html")


@livros_bp.route("/home")
def home():
    with _Sessao() as sessao:
        query = select(Livro).options(joinedload(Livro.autor))
        livros = sessao.scalars(query).all()
        usuario = sessao.get(Leitor, session.get("usuario"))

        return render_template("home.html", livros=livros, usuario=usuario)


@livros_bp.route("/livros/adicionar/", methods=["GET", "POST"])
def adicionar_livro():
    with _Sessao() as sessao:
        usuario = sessao.get(Leitor, session.get("usuario"))

        if request.method == "POST":
            titulo = request.form.get("titulo")
            nome_autor = request.form.get("autor")
            ano = request.form.get("ano")
            genero = request.form.get("genero")
            descricao = request.form.get("descricao")

            if not all([titulo, nome_autor, ano, genero, descricao]):
                flash("Preencha todos os campos.", "erro")
                return render_template(
                    "adicionar_livro.html", usuario=usuario
                )

            try:
                ano = int(ano)
            except ValueError:
                flash("Informe um ano válido.", "erro")
                return render_template(
                    "adicionar_livro.html", usuario=usuario
                )

            autor = sessao.scalar(
                select(Autor).where(Autor.nome == nome_autor)
            )

            if autor is None:
                autor = Autor(nome=nome_autor)
                sessao.add(autor)
                sessao.flush()

            livro = Livro(
                titulo=titulo,
                ano=ano,
                genero=genero,
                descricao=descricao,
                autor_id=autor.id
            )

            sessao.add(livro)
            sessao.commit()

            flash("Livro cadastrado com sucesso!", "sucesso")
            return redirect(url_for("livros.home"))

        return render_template("adicionar_livro.html", usuario=usuario)



@livros_bp.route("/livro/<int:id>")
def detalhes_livro(id):
    with _Sessao() as sessao:
        usuario = sessao.get(Leitor, session.get("usuario"))

        query = (
            select(Livro)
            .options(joinedload(Livro.autor))
            .where(Livro.id == id)
        )
        livro = sessao.scalar(query)

        if livro is None:
            flash("Livro não encontrado.", "erro")
            return redirect(url_for("livros.home"))

        emprestado_pelo_usuario = (
            usuario is not None and livro in usuario.livro_leitor
        )

        return render_template(
            "livro.html",
            livro=livro,
            usuario=usuario,
            emprestado_pelo_usuario=emprestado_pelo_usuario
        )




@livros_bp.route("/livros/editar/<int:id>", methods=["GET", "POST"])
def editar_livro(id):
    with _Sessao() as sessao:
        usuario = sessao.get(Leitor, session.get("usuario"))
        livro = sessao.get(Livro, id)

        if livro is None:
            flash("Livro não encontrado.", "erro")
            return redirect(url_for("livros.home"))

        if request.method == "POST":
            titulo = request.form.get("titulo")
            nome_autor = request.form.get("autor")
            genero = request.form.get("genero")
            descricao = request.form.get("descricao")
            ano = request.form.get("ano")

            if not all([titulo, nome_autor, genero, ano]):
                flash("Preencha todos os campos obrigatórios.", "erro")
                return render_template(
                    "editar_livro.html",
                    livro=livro,
                    usuario=usuario
                )

            try:
                ano = int(ano)
            except ValueError:
                flash("Informe um ano válido.", "erro")
                return render_template(
                    "editar_livro.html",
                    livro=livro,
                    usuario=usuario
                )

            autor = sessao.scalar(
                select(Autor).where(Autor.nome == nome_autor)
            )

            if autor is None:
                autor = Autor(nome=nome_autor)
                sessao.add(autor)

            livro.titulo = titulo
            livro.autor = autor
            livro.genero = genero
            livro.descricao = descricao
            livro.ano = ano

            sessao.commit()

            flash("Livro atualizado com sucesso!", "sucesso")

            return redirect(
                url_for("livros.detalhes_livro", id=id)
            )

        return render_template(
            "editar_livro.html",livro=livro, usuario=usuario
        )

# Excluir livro
@livros_bp.route("/livros/excluir/<int:id>", methods=["POST"])
def excluir_livro(id):
    with _Sessao() as sessao:
        livro = sessao.get(Livro, id)

        if livro is None:
            flash("Livro não encontrado.", "erro")

        elif livro.leitor:
            flash("Não é possível excluir um livro emprestado.", "erro")

        else:
            sessao.delete(livro)
            sessao.commit()
            flash("Livro excluído com sucesso!", "sucesso")

    return redirect(url_for("livros.home"))


# Emprestar livro
@livros_bp.route("/livros/emprestar/<int:id>", methods=["POST"])
def emprestar_livro(id):
    leitor_id = session.get("usuario")

    if leitor_id is None:
        flash("Faça login para emprestar livros.", "erro")
        return redirect(url_for("auth.login"))

    with _Sessao() as sessao:
        livro = sessao.get(Livro, id)
        leitor = sessao.get(Leitor, leitor_id)

        if livro is None or leitor is None:
            flash("Livro ou leitor não encontrado.", "erro")

        elif livro.emprestado:
            flash("Este livro já está emprestado.", "erro")

        else:
            leitor.livro_leitor.append(livro)
            livro.emprestado = True
            sessao.commit()
            flash("Empréstimo realizado com sucesso!", "sucesso")

    return redirect(url_for("livros.detalhes_livro", id=id))


# Devolver livro
@livros_bp.route("/livros/devolver/<int:id>", methods=["POST"])
def devolver_livro(id):
    leitor_id = session.get("usuario")

    if leitor_id is None:
        flash("Faça login para devolver livros.", "erro")
        return redirect(url_for("auth.login"))

    with _Sessao() as sessao:
        livro = sessao.get(Livro, id)
        leitor = sessao.get(Leitor, leitor_id)

        if livro is None or leitor is None:
            flash("Livro ou leitor não encontrado.", "erro")

        elif livro not in leitor.livro_leitor:
            flash("Você não possui esse livro emprestado.", "erro")

        else:
            leitor.livro_leitor.remove(livro)
            livro.emprestado = False
            sessao.commit()
            flash("Livro devolvido com sucesso!", "sucesso")

    return redirect(url_for("livros.detalhes_livro", id=id))


# Perfil do leitor
@livros_bp.route("/perfil")
def perfil():
    leitor_id = session.get("usuario")

    if leitor_id is None:
        flash("Faça login para acessar seu perfil.", "erro")
        return redirect(url_for("auth.login"))

    with _Sessao() as sessao:
        query = (
            select(Leitor)
            .options(
                selectinload(Leitor.livro_leitor)
                .joinedload(Livro.autor)
            )
            .where(Leitor.id == leitor_id)
        )

        usuario = sessao.scalar(query)

        if usuario is None:
            session.pop("usuario", None)
            flash("Usuário não encontrado.", "erro")
            return redirect(url_for("auth.login"))

        livros = list(usuario.livro_leitor)
        nome_usuario = usuario.nome

        return render_template(
            "perfil.html",
            usuario=usuario,
            livros=livros
        )
