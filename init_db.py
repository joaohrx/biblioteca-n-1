from database import  sessao, _Sessao, criar_banco
from models import Livro, Autor, Leitor
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
            titulo = "hora da estrela", ano = 1977, genero = "romance", descricao = "Livro mais ou menos", autor_id = autor_existente.id
        )
        livro2 = Livro(
            titulo = "O Lustre", ano = 1946, genero = "romance", descricao = "Livro sei la", autor_id = autor_existente.id
        )
        livro3 = Livro(
            titulo = "A Maçã no Escuro", ano = 1961, genero = "romance", descricao = "Livro ne", autor_id = autor_existente.id
        )
        sessao.add_all([livro, livro2, livro3])
        sessao.commit()


    if query_augusto:
        livro = Livro(
            titulo = "O Homem Mais Inteligente da História", ano = 2016, 
            genero = "ficção psicológica", descricao = "Livro massa", autor_id = query_augusto.id
        )
        livro2 = Livro(
            titulo = "O Vendedor de Sonhos: O Chamado", ano = 2008,
            genero = "ficção psicológica", descricao = "Livro boa", autor_id = query_augusto.id
        )
        livro3 = Livro(
            titulo = "O Vendedor de Sonhos 2: A Revolução dos Anônimos", ano = 2009,
            genero = "ficção psicológica", descricao = "Livro hehehe", autor_id = query_augusto.id
        )
        livro4 = Livro(
            titulo = "O Vendedor de Sonhos 3: O Semeador de Ideias", ano = 2010,
            genero = "ficção psicológica", descricao = "Livro opa", autor_id = query_augusto.id
        )
        sessao.add_all([livro, livro2, livro3, livro4])
        sessao.commit()
 
        
with _Sessao() as sessao:
    leitor = Leitor(
        nome = "joao pedro",
        #hash falso
        senha_hash = "skdpasdpoaskdpaoskd"
    )
    sessao.add(leitor)
    sessao.commit()


