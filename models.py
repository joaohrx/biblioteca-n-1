from database import Base
from typing import List
from sqlalchemy import String, Integer, Boolean, ForeignKey, Table, Column, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship


leitores_livros_tabela = Table(
    "leitores_livros",
    Base.metadata,
    Column("leitor_id", ForeignKey("leitores.id"), primary_key=True),
    Column("livros_id", ForeignKey("livros.id"), primary_key=True),

)

class Livro(Base):
    __tablename__ = 'livros'

    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    titulo: Mapped[str] = mapped_column(String(50))
    ano: Mapped[int] = mapped_column() 
    emprestado: Mapped[bool] = mapped_column(Boolean, default=False)
    genero: Mapped[str] = mapped_column(String(50))
    descricao: Mapped[str] = mapped_column(String(100))

    autor_id: Mapped[int] = mapped_column(ForeignKey("autores.id"))
    autor: Mapped['Autor'] = relationship(back_populates = 'livro')

    leitor: Mapped[List['Leitor']] = relationship(
        secondary= leitores_livros_tabela, back_populates= 'livro_leitor'
    )

class Autor(Base):
    __tablename__ = "autores"

    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    nome: Mapped[str] = mapped_column(String(50), unique = True)

    livro: Mapped[List['Livro']] = relationship(back_populates = 'autor')


class Leitor(Base):
    __tablename__ = "leitores"

    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    nome: Mapped[str] = mapped_column(String(100), unique = True)
    senha_hash: Mapped[str] = mapped_column(Text)

    livro_leitor: Mapped[List[Livro]] = relationship(
        secondary = leitores_livros_tabela, back_populates='leitor'
    )
