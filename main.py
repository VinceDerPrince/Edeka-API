from fastapi import FastAPI
import src.scraper as _scraper

app = FastAPI()

#The route of the api, a kind welcome message
@app.get("/")
async def route():
    return {"message":"Willkommen zu dieser Edeka Angebote API"}

#The get function which calls the get_offers function from scraper.py
@app.get("/get_offers")
async def get_offers(adress: str):
    return _scraper.get_offers(adress)