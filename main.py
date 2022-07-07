from fastapi import FastAPI
import src.scraper as _scraper

app = FastAPI()

@app.get("/")
async def route():
    return {"message":"Willkommen zu dieser Edeka Angebote API"}

@app.get("/get_offers")
async def get_offers(adress: str):
    return _scraper.get_offers(adress)