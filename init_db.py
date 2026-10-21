from database import engine, Base, sessao, _Sessao
from models import Livro, Autor, Leitor, leitores_livros_tabela
from sqlalchemy import select

Base.metadata.create_all(bind = engine)
""" 
with _Sessao() as sessao:
    autor = Autor(
        nome = "clarice lispecter"
    )
    leitor = Leitor(
        nome = "joao pedro"
    )
    sessao.add_all([autor,leitor])
    sessao.commit()
"""

""" with _Sessao() as sessao:
    query = select(Autor).where(Autor.nome == "clarice lispecter")
    autor_existente = sessao.scalar(query)

    if autor_existente:
        livro = Livro(
            titulo = "hora da estrela", ano = 1950, autor_id = autor_existente.id
        )
        sessao.add(livro)
        sessao.commit()
 """

""" with _Sessao() as sessao:
    query = select(Livro).join(Autor, Livro.autor_id == Autor.id)
    livros = sessao.scalars(query).all()
    for livro in livros:
        print(f"Livro: {livro.titulo} | Autor: {livro.autor.nome}")
 """

with _Sessao() as sessao:
    query = select(Leitor).where(Leitor.nome == "joao pedro")
    leitores_existente = sessao.scalar(query)

    query_ivro = select(Livro).where(Livro.titulo == "hora da estrela")
    livro_existe = sessao.scalar(query)

    if leitores_existente and livro_existe:
        leitor_livro = leitores_livros_tabela(leitor_id = leitores_existente.id, livros_id = livro_existe.id)
        sessao.add(leitor_livro)
        sessao.commit()
