from typing import Union
from fastapi import FastAPI
import dask.dataframe as dd
import pandas as pd


app = FastAPI()

flights_data = dd.read_csv("../nycflights.csv")
dta = flights_data.compute()


@app.get("/")
def read_root():
    j = pd.DataFrame.to_json(dta)
    return j


@app.get("/flight/{tailnum}")
def read_item(tailnum: str):
    result = dta[dta["tailnum"] == tailnum]
    j = pd.DataFrame.to_json(result)
    return j
