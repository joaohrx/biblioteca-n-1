from database import  sessao, _Sessao
from models import Livro, Autor, Leitor
from sqlalchemy import select

#usar dicionario, adicao, e string, ator.
def adicionar_livro(adicao, autor):
    with _Sessao() as sessao:
        query = select(Autor).where(Autor.nome == autor)
        autor_existe = sessao.scalar(query)

        if autor_existe:
            livro = Livro(
                titulo = adicao["titulo"], ano = adicao["ano"], genero = adicao["genero"],
                autor_id = autor_existe.id
            )
            sessao.add(livro)
            sessao.commit()

        return "autor não existe"
        

def buscar_livro_titulo(titulo):
    with _Sessao() as sessao:
        query = select(Livro).where(Livro.titulo == titulo)
        livro_encontrado = sessao.scalar(query)

        if livro_encontrado:
            return livro_encontrado.titulo
        
        return None
