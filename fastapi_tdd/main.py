from collections import Counter

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"msg": "Hello World!"}


@app.get("/{number}")
async def create_counter_from_our_number(number: str):
    return Counter(number)
