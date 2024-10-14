from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

#Criando a conexão com o BD SQLite

engine = create_engine('sqlite:///meubanco.db', echo=True) 

print('Conexão com SQLite estabelecida.')

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    
#Criar as tabelas no bd
Base.metadata.create_all(engine)