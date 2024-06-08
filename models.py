# models.py
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Item(BaseModel):
    id: int
    title: str
    description: str
    initial_bid: float
    current_bid: Optional[float] = None
    end_time: datetime

class Comprador(BaseModel):
    id: int
    name: str

class Oferta(BaseModel):
    item_id: int
    comprador_id: int
    oferta_valor: float
    oferta_hora: datetime
