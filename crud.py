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

        return "autor não existe"
        
#busca por titulo do livros
def buscar_livro_titulo(titulo):
    with _Sessao() as sessao:
        query = select(Livro).where(Livro.titulo == titulo)
        livro_encontrado = sessao.scalar(query)

        if livro_encontrado:
            return livro_encontrado.titulo

        return "livro não existe"
        

#função para o emprestimo do livro
def emprestar_livro(livro, leitor_nome):
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
    query = sessao.scalars(select(Leitor))
    lista_leitor = []
    if query:
        for i in query:
            lista_leitor.append(i.nome)
             
    return lista_leitor

#retorna uma lista e busca livros emprestados
def filtrar_livros_emprestados():
    query = select(Livro).where(Livro.emprestado == True)
    livro_empretado = sessao.scalars(query)

    lista_livro = []

    if livro_empretado:
       for i in livro_empretado:
            lista_livro.append(i.titulo)
       
    return lista_livro 

def filtra_livros_genero(genero):
    query = select(Livro).where(Livro.genero == genero)
    livro_genero = sessao.scalars(query)

    lista_livro = []

    if livro_genero:
       for i in livro_genero:
            lista_livro.append(i.titulo)

    return lista_livro 

def filtrar_livros_autor(autor):
    query = select(Livro).join(Autor, Livro.autor_id == Autor.id).where(Autor.nome == autor)
    livro_existe = sessao.scalars(query)

    lista_livro = []

    if livro_existe:
       for i in livro_existe:
            lista_livro.append(i.titulo)
        

    return lista_livro 

