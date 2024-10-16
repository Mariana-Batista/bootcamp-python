from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

#Criando a conexão com o BD SQLite

engine = create_engine('sqlite:///meubanco.db', echo=True) 

print('Conexão com SQLite estabelecida.')

#Criando tabelas no banco de dados
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    
#Criar as tabelas no bd
Base.metadata.create_all(engine)

#Inserindo dados na tabela
Session = sessionmaker(bind=engine)
session = Session()

# try:
#     novo_usuario = Usuario(nome='João', idade=28)
#     session.add(novo_usuario)
#     session.commit()
# except:
#     session.rollback()
#     raise
# finally:
#     session.close()
# print('Usuário inserido com sucesso.')

#Consultando dados através de query
usuario = session.query(Usuario).filter_by(nome='João').first()
print(f"Usuário encontrado: {usuario.nome}, Idade: {usuario.idade}")

