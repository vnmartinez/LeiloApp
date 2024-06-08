# main.py
from fastapi import FastAPI, HTTPException
from models import Item, Comprador, Oferta
from datetime import datetime
from typing import List

app = FastAPI()

itens = []
compradores = []
ofertas = []

@app.post("/itens/", response_model=Item)
def inserir_item(item: Item):
    itens.append(item)
    return item

@app.post("/compradores/", response_model=Comprador)
def adicionar_comprador(comprador: Comprador):
    compradores.append(comprador)
    return comprador

@app.get("/compradores/", response_model=List[Comprador])
def listar_compradores():
    if not compradores:
        raise HTTPException(status_code=404, detail="Nenhum comprador encontrado")
    return compradores

@app.post("/ofertas/")
def fazer_oferta(oferta: Oferta):
    item = next((item for item in itens if item.id == oferta.item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    if oferta.oferta_valor <= (item.current_bid or item.initial_bid):
        raise HTTPException(status_code=400, detail="A oferta deve ser maior que a oferta atual")
    item.current_bid = oferta.oferta_valor
    ofertas.append(oferta)
    return oferta

@app.get("/ofertas/{item_id}", response_model=List[Oferta])
def listar_ofertas(item_id: int):
    item_ofertas = [oferta for oferta in ofertas if oferta.item_id == item_id]
    if not item_ofertas:
        raise HTTPException(status_code=404, detail="Nenhuma oferta encontrada para este item")
    return item_ofertas

@app.get("/itens/", response_model=List[Item])
def listar_itens():
    return itens

@app.get("/itens/{item_id}", response_model=Item)
def listar_item(item_id: int):
    item = next((item for item in itens if item.id == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return item
    