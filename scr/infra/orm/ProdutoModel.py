import db
from sqlalchemy import Column, VARCHAR, BLOB, Integer, DECIMAL


# ORM
class ProdutoDB(db.Base):
    __tablename__ = 'tb_produto'
    
    id_produto = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome_produto = Column(VARCHAR(100), nullable=False, index=True)
    descricao = Column(VARCHAR(200), nullable=False)
    foto = Column(BLOB, nullable=False)
    valor_unitario = Column(DECIMAL, nullable=False)
    

    def __init__(self, id_produto, nome_produto, descricao, foto, valor_unitario):
        self.id_produto = id_produto
        self.nome_produto = nome_produto
        self.descricao = descricao
        self.foto = foto
        self.valor_unitario = valor_unitario

from db import Base, engine
