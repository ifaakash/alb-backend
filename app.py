from fastapi import FastAPI
import random
import json

app = FastAPI()

# Load quotes from a JSON file
with open("quotes.json") as f:
    quotes = json.load(f)

@app.get("/")
def root():
    return {"message": "Welcome to the Quote Generator API"}

@app.get("/api/quote")
def get_random_quote():
    return {"quote": random.choice(quotes)}

@app.get("/api/quotes")
def get_all_quotes():
    return {"quotes": quotes}
