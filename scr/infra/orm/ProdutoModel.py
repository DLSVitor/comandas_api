import db
from sqlalchemy import Column, VARCHAR, BLOB, Integer, DECIMAL

# ORM
class ProdutoDB(db.Base):
    __tablename__ = 'tb_produto'
    
    id_produto = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False, index=True)
    descricao = Column(VARCHAR(120), nullable=True)
    foto = Column(BLOB)
    valor_unitario = Column(DECIMAL)

    def __init__(self, id_produto, nome, descricao, foto, valor_unitario):
        self.id_produto = id_produto
        self.nome = nome
        self.descricao = descricao
        self.foto = foto
        self.valor_unitario = valor_unitario