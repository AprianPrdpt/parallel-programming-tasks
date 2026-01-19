from typing import Union

from fastapi import FastAPI

import psycopg


app = FastAPI()


def connect_psql():
    conn = psycopg.connect("dbname=paralel10 user=bpdp password=merdeka host=localhost", autocommit=True)
    return conn

conn = connect_psql()

@app.get("/")
def read_root():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM tabel01")
        return cur.fetchall()


@app.get("/mahasiswa/{nim}")
def read_item(nim: int, q: Union[str, None] = None):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM tabel01 WHERE nim=%s", [nim])
        return cur.fetchall()
    #return {"item_id": item_id, "q": q}
