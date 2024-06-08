# main.py
from fastapi import FastAPI, HTTPException
from models import Item, Buyer, Bid
from datetime import datetime
from typing import List

app = FastAPI()

items = []
buyers = []
bids = []

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

@app.post("/buyers/", response_model=Buyer)
def create_buyer(buyer: Buyer):
    buyers.append(buyer)
    return buyer

@app.post("/bids/")
def place_bid(bid: Bid):
    item = next((item for item in items if item.id == bid.item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if bid.bid_amount <= (item.current_bid or item.initial_bid):
        raise HTTPException(status_code=400, detail="Bid must be higher than the current bid")
    item.current_bid = bid.bid_amount
    bids.append(bid)
    return bid

@app.get("/items/", response_model=List[Item])
def list_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = next((item for item in items if item.id == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
    