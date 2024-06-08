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

class Buyer(BaseModel):
    id: int
    name: str

class Bid(BaseModel):
    item_id: int
    buyer_id: int
    bid_amount: float
    bid_time: datetime
