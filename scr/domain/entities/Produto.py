from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class Produto(BaseModel):
    id_produto: int = None
    nome_produto: str
    descricao: Optional[str] = None
    foto: bytes
    valor_unitario: Decimal
 