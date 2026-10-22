from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass


engine = create_engine("sqlite:///biblioteca.db", echo = True)
_Sessao = sessionmaker( bind = engine)
sessao = _Sessao()

def criar_banco():
    Base.metadata.create_all(bind = engine)