from fastapi import FastAPI
from retriever import fetch_disaster_data
from pathway_ingest import create_index

app = FastAPI()

# Load Pathway index
index = create_index()

@app.get("/")
def home():
    return {"message": "Disaster Management API is Running"}

@app.get("/disasters")
def get_disasters():
    return fetch_disaster_data()

@app.get("/search/{query}")
def search_disaster(query: str):
    results = index.lookup(query)
    return results

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
