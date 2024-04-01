from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Auth Service - Root URL"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {
        "MSG": "Auth Service - ITEM URL",
        "item_id": item_id
    }