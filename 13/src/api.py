from typing import Union

from fastapi import Depends, FastAPI

from piccolo.table import Table
from piccolo.columns import ForeignKey, Integer, Varchar, Serial
from pydantic import BaseModel

from piccolo.engine.sqlite import SQLiteEngine

DB = SQLiteEngine(path='piccolo.sqlite')


class Band(Table, db=DB):
    id = Serial()
    name = Varchar()
    popularity = Integer()


app = FastAPI()

@app.get("/")
async def read_root():
    return await Band.select()


@app.get("/Band/{id}")
async def read_item(id: int, q: Union[str, None] = None):
    return await Band.select().where(Band.id==id)
