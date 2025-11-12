# In dieser Datei liegen die API-Endpunkte.

from fastapi import FastAPI, HTTPException
from api import crud

app = FastAPI()

@app.get("/shorts/{short_id}")
async def read_item(short_id: int):
    item = crud.get_item(short_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/shorts/")
async def create_item(short_url: str):
    return crud.create_item(short_url)
