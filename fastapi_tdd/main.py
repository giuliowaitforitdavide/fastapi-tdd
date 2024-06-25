import re
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"msg": "Hello World!"}


@app.get("/{number}")
async def create_counter_from_our_number(number: int, ans: Union[int, None] = None):
    string_number = str(number)
    ans = {}
    for i in range(1, 10):
        occurences = len(re.findall(f"{i}", string_number))
        if occurences:
            ans[str(i)] = occurences

    return ans
