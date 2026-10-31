from database import _Sessao, criar_banco
from models import Livro, Autor, Leitor, leitores_livros_tabela
from sqlalchemy import delete



criar_banco()


with _Sessao() as sessao:

    autores = {
        "Italo Calvino": [
            {
                "titulo": "As Cidades Invisíveis",
                "ano": 1972,
                "genero": "Literatura fantástica",
                "descricao": "Uma viagem por cidades imaginárias."
            },
            {
                "titulo": "Se um Viajante numa Noite de Inverno",
                "ano": 1979,
                "genero": "Metaficção",
                "descricao": "Um romance sobre a experiência da leitura."
            },
            {
                "titulo": "O Barão nas Árvores",
                "ano": 1957,
                "genero": "Fantasia",
                "descricao": "A história de um jovem que decide viver nas árvores."
            }
        ],

        "Jorge Luis Borges": [
            {
                "titulo": "Ficções",
                "ano": 1944,
                "genero": "Contos fantásticos",
                "descricao": "Contos sobre labirintos, espelhos e infinitos."
            },
            {
                "titulo": "O Aleph",
                "ano": 1949,
                "genero": "Contos fantásticos",
                "descricao": "Contos que exploram o infinito e a realidade."
            },
            {
                "titulo": "O Livro de Areia",
                "ano": 1975,
                "genero": "Contos fantásticos",
                "descricao": "Narrativas sobre o tempo, a memória e o infinito."
            }
        ],

        "Lygia Fagundes Telles": [
            {
                "titulo": "Ciranda de Pedra",
                "ano": 1954,
                "genero": "Romance",
                "descricao": "Um romance sobre conflitos familiares e amadurecimento."
            },
            {
                "titulo": "Antes do Baile Verde",
                "ano": 1970,
                "genero": "Contos",
                "descricao": "Coletânea de contos sobre relações humanas."
            },
            {
                "titulo": "As Meninas",
                "ano": 1973,
                "genero": "Romance",
                "descricao": "A trajetória de três jovens durante a ditadura brasileira."
            }
        ]
    }

    for nome_autor, livros in autores.items():

        autor = Autor(nome=nome_autor)
        sessao.add(autor)
        sessao.flush()

        for dados in livros:
            livro = Livro(
                titulo=dados["titulo"],
                ano=dados["ano"],
                genero=dados["genero"],
                descricao=dados["descricao"],
                autor_id=autor.id
            )

            sessao.add(livro)

    sessao.commit()

print("Banco de dados inicializado com sucesso!")