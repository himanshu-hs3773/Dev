from datetime import datetime
from typing import Union

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, ORJSONResponse, HTMLResponse
from pydantic import BaseModel
from fastapi import FastAPI, Response


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: Union[str, None] = None


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/index")
async def root():
    return {"message": "Hello USA"}


@app.put("/items/{idx}")
def update_item(idx: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    return JSONResponse(content=json_compatible_item_data)


@app.get("/legacy/")
def get_legacy_data():
    data = """<?xml version="1.0"?>
    <shampoo>
    <Header>
        Apply shampoo here.
    </Header>
    <Body>
        You'll have to use soap here.
    </Body>
    </shampoo>
    """
    return Response(content=data, media_type="application/xml")


@app.get("/a/", response_class=ORJSONResponse)
async def read_items():
    return ORJSONResponse([{"item_id": "Foo"}])


@app.get("/b/", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
