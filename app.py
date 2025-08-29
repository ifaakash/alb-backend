from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import json

app = FastAPI()

# Allow traffic from the frontend ( to avoid CORS issue )
origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # list of allowed origins
    allow_credentials=True,
    allow_methods=["*"],          # GET, POST, etc.
    allow_headers=["*"],          # allow all headers
)

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
