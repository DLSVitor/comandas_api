from pydantic import BaseModel
from decimal import Decimal

class Produto(BaseModel):
    id_produto: int = None
    nome: str
    descrição: str = None
    foto: bytes
    valor_unitario: Decimal
 