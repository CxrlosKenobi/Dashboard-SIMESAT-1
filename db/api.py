import sqlite3
import pandas as pd
import datetime as dt

def get_current_time():
    now = dt.datetime.now()
    total_time = (now.hour * 3600) + (now.minute * 60) + (now.second)
    return total_time

def get_bmp_data(start, end):
    con = sqlite3.connect('data.db')
    statement = f'SELECT bmp280 FROM data WHERE timeinsec > {start} AND timeinsec <= {end};'
    df = pd.read_sql_query(statement, con)
    return df
