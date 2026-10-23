from database import  sessao, _Sessao, criar_banco
from models import Livro, Autor
from sqlalchemy import select


criar_banco()
"""
    ADIÇÃO DE AUTORES
"""
with _Sessao() as sessao:
    autor = Autor(
        nome = "clarice lispecter"
    )
    autor2 = Autor(
        nome = "Augusto Cury"
    )
    autor3 = Autor(
        nome = "C. S. Lewis"
    )
    sessao.add_all([autor, autor2,autor3])
    sessao.commit()

"""
ADIÇÕES DO LIVROS DO AUTOR CLARICE E CURY
"""
with _Sessao() as sessao:
    query = select(Autor).where(Autor.nome == "clarice lispecter")
    autor_existente = sessao.scalar(query)

    query_augusto= sessao.scalar(select(Autor).where(Autor.nome == "Augusto Cury"))

    if autor_existente:
        livro = Livro(
            titulo = "hora da estrela", ano = 1977, genero = "romance", autor_id = autor_existente.id
        )
        livro2 = Livro(
            titulo = "O Lustre", ano = 1946, genero = "romance", autor_id = autor_existente.id
        )
        livro3 = Livro(
            titulo = "A Maçã no Escuro", ano = 1961, genero = "romance", autor_id = autor_existente.id
        )
        sessao.add_all([livro, livro2, livro3])
        sessao.commit()


    if query_augusto:
        livro = Livro(
            titulo = "O Homem Mais Inteligente da História", ano = 2016, 
            genero = "ficção psicológica", autor_id = query_augusto.id
        )
        livro2 = Livro(
            titulo = "O Vendedor de Sonhos: O Chamado", ano = 2008,
            genero = "ficção psicológica", autor_id = query_augusto.id
        )
        livro3 = Livro(
            titulo = "O Vendedor de Sonhos 2: A Revolução dos Anônimos", ano = 2009,
            genero = "ficção psicológica", autor_id = query_augusto.id
        )
        livro4 = Livro(
            titulo = "O Vendedor de Sonhos 3: O Semeador de Ideias", ano = 2010,
            genero = "ficção psicológica", autor_id = query_augusto.id
        )
        sessao.add_all([livro, livro2, livro3, livro4])
        sessao.commit()
 
        


