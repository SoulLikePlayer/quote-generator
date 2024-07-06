from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

quotes = [
    "La seule limite à notre réalisation de demain est nos doutes d'aujourd'hui. - Franklin D. Roosevelt",
    "Le futur appartient à ceux qui croient en la beauté de leurs rêves. - Eleanor Roosevelt",
    "Ne regarde pas l'horloge; fais comme elle, avance. - Sam Levenson"
]

@app.get("/quote")
def get_quote():
    return {"quote": random.choice(quotes)}

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("templates/index.html") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)
