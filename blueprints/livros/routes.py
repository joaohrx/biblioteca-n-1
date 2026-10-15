from flask import render_template, request, session, redirect, url_for
from blueprints.auth import auth_bp
import database


# @auth_bp.route("/")
# def index():
#     livros = Livro.query.all()
#     return render_template("livros/index.html", livros=livros)
    


# @auth_bp.route("/livros/adicionar", methods=["GET", "POST"])
# def adicionar_livro():
#     if request.method == "POST":
#         titulo = request.form.get("titulo")
#         autor = request.form.get("autor")
#         ano = request.form.get("ano")
#         quantidade = request.form.get("quantidade")

#         if not titulo or not autor:
#             flash("Preencha o título e o autor.", "erro")
#             return render_template("livros/formulario.html")

#         livro = Livro(
#             titulo=titulo,
#             autor=autor,
#             ano=int(ano) if ano else None,
#             quantidade=int(quantidade),
#             disponiveis=int(quantidade)
#         )

#         db.session.add(livro)
#         db.session.commit()

#         flash("Livro cadastrado com sucesso!", "sucesso")
#         return redirect(url_for("livros.index"))

#     return render_template("livros/formulario.html")

