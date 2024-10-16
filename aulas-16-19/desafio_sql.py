"""Este desafio focará na criação de duas tabelas relacionadas, Produto e Fornecedor, utilizando SQLAlchemy. 
Cada produto terá um fornecedor associado, demonstrando o uso de chaves estrangeiras para estabelecer relações entre tabelas. 
Além disso, você realizará inserções nessas tabelas para praticar a manipulação de dados."""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

# Criando a conexão com o banco de dados
engine = create_engine('sqlite:///bancodesafio.db', echo=True)
print('Estabelecida conexão com o banco de dados.')

# Criando a base declarativa
Base = declarative_base()

# Definindo a tabela 'Produto'
class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome_produto = Column(String, nullable=False)
    id_fornecedor = Column(Integer, ForeignKey('fornecedores.id_fornecedor'))

# Definindo a tabela 'Fornecedor'
class Fornecedor(Base):
    __tablename__ = 'fornecedores'
    id_fornecedor = Column(Integer, primary_key=True)
    nome_fornecedor = Column(String, nullable=False)

# Criando as tabelas no banco de dados
Base.metadata.create_all(engine)
print('Tabelas criadas.')

# Criando a sessão
Session = sessionmaker(bind=engine)
session = Session()

try:
    # Inserindo fornecedores
    fornecedores = [
        Fornecedor(id_fornecedor=1, nome_fornecedor='Tech Supplies'),
        Fornecedor(id_fornecedor=2, nome_fornecedor='Office World')
    ]

    # Inserindo produtos
    produtos = [
        Produto(nome_produto='Notebook Lenovo', id_fornecedor=1),
        Produto(nome_produto='Impressora Epson', id_fornecedor=1),
        Produto(nome_produto='Cadeira de Escritório', id_fornecedor=2)
    ]

    # Adicionando e confirmando no banco
    session.add_all(fornecedores + produtos)
    session.commit()
    print('Novos dados inseridos com sucesso.')

except Exception as e:
    # Tratando erros e revertendo transação em caso de falha
    session.rollback()
    print(f'Ocorreu um erro: {e}')
    raise

finally:
    # Fechando a sessão
    session.close()
    
'''
Retorno da execução:

Estabelecida conexão com o banco de dados.
2024-10-16 13:30:41,746 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-16 13:30:41,746 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("produtos")
2024-10-16 13:30:41,747 INFO sqlalchemy.engine.Engine [raw sql] ()
2024-10-16 13:30:41,750 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("produtos")
2024-10-16 13:30:41,750 INFO sqlalchemy.engine.Engine [raw sql] ()
2024-10-16 13:30:41,751 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("fornecedores")
2024-10-16 13:30:41,751 INFO sqlalchemy.engine.Engine [raw sql] ()
2024-10-16 13:30:41,752 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("fornecedores")
2024-10-16 13:30:41,752 INFO sqlalchemy.engine.Engine [raw sql] ()
2024-10-16 13:30:41,753 INFO sqlalchemy.engine.Engine
CREATE TABLE fornecedores (
        id_fornecedor INTEGER NOT NULL,
        nome_fornecedor VARCHAR NOT NULL,
        PRIMARY KEY (id_fornecedor)
)


2024-10-16 13:30:41,754 INFO sqlalchemy.engine.Engine [no key 0.00073s] ()
2024-10-16 13:30:41,758 INFO sqlalchemy.engine.Engine 
CREATE TABLE produtos (
        id INTEGER NOT NULL,
        nome_produto VARCHAR NOT NULL,
        id_fornecedor INTEGER,
        PRIMARY KEY (id),
        FOREIGN KEY(id_fornecedor) REFERENCES fornecedores (id_fornecedor)
)


2024-10-16 13:30:41,759 INFO sqlalchemy.engine.Engine [no key 0.00111s] ()
2024-10-16 13:30:41,762 INFO sqlalchemy.engine.Engine COMMIT
Tabelas criadas.
2024-10-16 13:30:41,765 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-16 13:30:41,766 INFO sqlalchemy.engine.Engine INSERT INTO fornecedores (id_fornecedor, nome_fornecedor) VALUES (?, ?)
2024-10-16 13:30:41,767 INFO sqlalchemy.engine.Engine [generated in 0.00035s] [(1, 'Tech Supplies'), (2, 'Office World')]
2024-10-16 13:30:41,769 INFO sqlalchemy.engine.Engine INSERT INTO produtos (nome_produto, id_fornecedor) VALUES (?, ?) RETURNING id
2024-10-16 13:30:41,769 INFO sqlalchemy.engine.Engine [generated in 0.00011s (insertmanyvalues) 1/3 (ordered; batch not supported)] ('Notebook Lenovo', 1)
2024-10-16 13:30:41,770 INFO sqlalchemy.engine.Engine INSERT INTO produtos (nome_produto, id_fornecedor) VALUES (?, ?) RETURNING id
2024-10-16 13:30:41,770 INFO sqlalchemy.engine.Engine [insertmanyvalues 2/3 (ordered; batch not supported)] ('Impressora Epson', 1)
2024-10-16 13:30:41,771 INFO sqlalchemy.engine.Engine INSERT INTO produtos (nome_produto, id_fornecedor) VALUES (?, ?) RETURNING id
2024-10-16 13:30:41,771 INFO sqlalchemy.engine.Engine [insertmanyvalues 3/3 (ordered; batch not supported)] ('Cadeira de Escritório', 2)
2024-10-16 13:30:41,773 INFO sqlalchemy.engine.Engine COMMIT
Novos dados inseridos com sucesso.

'''
