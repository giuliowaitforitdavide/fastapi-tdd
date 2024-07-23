import re

from fastapi import FastAPI

app = FastAPI()


@app.get("/{number}")
async def create_counter_from_our_number(number: str):
    ans = {}
    for i in range(0, 10):
        occurences = len(re.findall(f"{i}", number))
        if occurences:
            ans[str(i)] = occurences

    return ans
