import sqlite3
import pandas as pd
import datetime as dt
import pathlib

DB_FILE = pathlib.Path(__file__).resolve().parent.joinpath("data.db").resolve()

def get_current_time():
    now = dt.datetime.now()
    total_time = (now.hour * 3600) + (now.minute * 60) + (now.second)
    return total_time

def get_bmp_data(start, end):
    con = sqlite3.connect(str(DB_FILE))
    statement = f'SELECT bmp280_te FROM data WHERE timeinsec > {start} AND timeinsec <= {end};'
    df = pd.read_sql_query(statement, con)
    return df

def get_hdc_data(start, end):
    con = sqlite3.connect(str(DB_FILE))
    statement = f'SELECT hdc1080_te FROM data WHERE timeinsec > {start} AND timeinsec <= {end};'
    df = pd.read_sql_query(statement, con)
    return df
