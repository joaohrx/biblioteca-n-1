from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass


engine = create_engine("sqlite:///biblioteca.db", echo = True)
_sessao = sessionmaker( bind = engine)
sessao = _sessao()
