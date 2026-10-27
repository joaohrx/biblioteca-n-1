from database import  sessao, _Sessao
from models import Livro, Autor, Leitor
from sqlalchemy import select

#usar dicionario, adicao, e string, ator, para poder adicionar o livro 
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

        
#busca por titulo do livros
def buscar_livro_titulo(titulo):
    with _Sessao() as sessao:
        query = select(Livro).where(Livro.titulo == titulo)
        livro_encontrado = sessao.scalar(query)

        if livro_encontrado:
            return livro_encontrado

        

#função para o emprestimo do livro
def emprestar_livro(livro, leitor_nome):
    with _Sessao() as sessao:
        query = select(Livro).where(Livro.titulo == livro)
        livro_existe = sessao.scalar(query)

        query = select(Leitor).where(Leitor.nome == leitor_nome)
        leitor_existe = sessao.scalar(query)

        if livro_existe and leitor_existe:
            leitor_existe.livro_leitor.append(livro_existe)
            livro_existe.emprestado = True

            sessao.commit()


#vai buscar todos os usuarios existente no sistema e retorna uma lista
def leitor_existe():
    with _Sessao() as sessao:
        query = sessao.scalars(select(Leitor))
        lista_leitor = []
        if query:
            for i in query:
                lista_leitor.append(i.nome)

        return lista_leitor

#retorna uma lista e busca livros emprestados
def filtrar_livros_emprestados():
    with _Sessao() as sessao:
        query = select(Livro).where(Livro.emprestado == True)
        livro_empretado = sessao.scalars(query)

        lista_livro = []

        if livro_empretado:
           for i in livro_empretado:
                lista_livro.append(i.titulo)

        return lista_livro 

def filtra_livros_genero(genero):
    with _Sessao() as sessao:
        query = select(Livro).where(Livro.genero == genero)
        livro_genero = sessao.scalars(query)

        lista_livro = []

        if livro_genero:
           for i in livro_genero:
                lista_livro.append(i.titulo)

        return lista_livro 

def filtrar_livros_autor(autor):
    with _Sessao() as sessao:
        query = select(Livro).join(Autor, Livro.autor_id == Autor.id).where(Autor.nome == autor)
        livro_existe = sessao.scalars(query)

        lista_livro = []

        if livro_existe:
           for i in livro_existe:
                lista_livro.append(i.titulo)


        return lista_livro 

# desfaz o relacionamento da tabela auxiliar, e altera para false 
def devolver_livro(titulo, nome):
    with _Sessao() as sessao:
        query = select(Livro).join(Livro.leitor).where(Livro.titulo == titulo and Leitor.titulo == nome)
        livro_existe = sessao.scalar(query)

        query = select(Leitor).join(Leitor.livro_leitor).where(Leitor.nome == nome)
        usuario_existe = sessao.scalar(query)

        if livro_existe and usuario_existe:
            livro_existe.leitor.remove(usuario_existe)
            livro_existe.emprestado = False
            sessao.commit()


def editar_livros(titulo, auteracao):
    with _Sessao() as sessao:
        query = select(Livro).where(Livro.titulo == titulo)
        livro_encontrado = sessao.scalar(query)

        if livro_encontrado:
            livro_encontrado.descricao = auteracao
            sessao.commit()

editar_livros("hora da estrela", "bom é pouco, ele é massa")