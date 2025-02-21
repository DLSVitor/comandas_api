from pydantic import BaseModel
from decimal import Decimal

class Produto(BaseModel):
    id_produto: int = None
    nome: str
    descrição: str = None
    foto: str
    valor_unitario: Decimal
 