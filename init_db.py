from database import engine,  sessao, _Sessao, criar_banco
from models import Livro, Autor, Leitor, leitores_livros_tabela
from sqlalchemy import select


criar_banco()

""" with _Sessao() as sessao:
    autor = Autor(
        nome = "clarice lispecter"
    )
    leitor = Leitor(
        nome = "joao pedro"
    )
    sessao.add_all([autor,leitor])
    sessao.commit()

with _Sessao() as sessao:
    query = select(Autor).where(Autor.nome == "clarice lispecter")
    autor_existente = sessao.scalar(query)

    if autor_existente:
        livro = Livro(
            titulo = "hora da estrela", ano = 1950, autor_id = autor_existente.id
        )
        sessao.add(livro)
        sessao.commit()
 

with _Sessao() as sessao:
    query = select(Livro).join(Autor, Livro.autor_id == Autor.id)
    livros = sessao.scalars(query).all()
    for livro in livros:
       print(f"Livro: {livro.titulo} | Autor: {livro.autor.nome}")


with _Sessao() as sessao:
    query = sessao.scalar(select(Leitor).where(Leitor.nome == "joao pedro"))

    query_livro = sessao.scalar(select(Livro).where(Livro.titulo == "hora da estrela"))


    if query and query_livro:
        query.livro_leitor.append(query_livro)
        query_livro.empretado = True
        sessao.commit()

        

        TESTE DO BANCO: TODOS FUNCIONAM
 """