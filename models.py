from database import Base

from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Livro(Base):
    __tablename__ = 'livros'

    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    titulo: Mapped[str] = mapped_column(String(50))
    ano: Mapped[int] = mapped_column() 

    autor_id: Mapped[int] = mapped_column(ForeignKey("autores.id"))
    autor: Mapped['Autor'] = relationship(back_populates = 'livro')


class Autor(Base):
    __tablename__ = "autores"

    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    nome: Mapped[str] = mapped_column(String(50), unique = True)

    livro: Mapped[List['Livro']] = relationship(back_populates = 'autor')


class Leitor(Base):
    __tablename__ = "leitores"

    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    nome: Mapped[str] = mapped_column(String(50), unique = True)


