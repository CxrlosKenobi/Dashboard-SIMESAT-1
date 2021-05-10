import sqlite3
import pandas as pd
import datetime as dt
import pathlib



# <script src='https://api.mapbox.com/mapbox-gl-js/v2.1.1/mapbox-gl.js'></script>
# <link href='https://api.mapbox.com/mapbox-gl-js/v2.1.1/mapbox-gl.css' rel='stylesheet' />

DB_FILE = pathlib.Path(__file__).resolve().parent.joinpath("data.db").resolve()

def get_current_time():
    now = dt.datetime.now()
    total_time = (now.hour * 3600) + (now.minute * 60) + (now.second)
    return total_time

def get_bmp_pr_data(start, end):
    con = sqlite3.connect(str(DB_FILE))
    statement = f'SELECT bmp280_pr FROM data WHERE timeinsec > {start} AND timeinsec <= {end};'
    df = pd.read_sql_query(statement, con)
    return df

def get_hdc_te_data(start, end):
    con = sqlite3.connect(str(DB_FILE))
    statement = f'SELECT hdc1080_te FROM data WHERE timeinsec > {start} AND timeinsec <= {end};'
    df = pd.read_sql_query(statement, con)
    return df

def get_hdc_hu_data(start, end):
    con = sqlite3.connect(str(DB_FILE))
    statement = f'SELECT hdc1080_hu FROM data WHERE timeinsec > {start} AND timeinsec <= {end};'
    df = pd.read_sql_query(statement, con)
    return df

def get_mpu9250_ac_data(start, end):
    con = sqlite3.connect(str(DB_FILE))
    statement = f'SELECT mpu9250_ac FROM data WHERE timeinsec > {start} AND timeinsec <= {end};'
    df = pd.read_sql_query(statement, con)
    return df

def get_mpu9250_gy_data(start, end):
    con = sqlite3.connect(str(DB_FILE))
    statement = f'SELECT mpu9250_gy FROM data WHERE timeinsec > {start} AND timeinsec <= {end};'
    df = pd.read_sql_query(statement, con)
    return df

def get_mpu9250_ma_data(start, end):
    con = sqlite3.connect(str(DB_FILE))
    statement = f'SELECT mpu9250_ma FROM data WHERE timeinsec > {start} AND timeinsec <= {end};'
    df = pd.read_sql_query(statement, con)
    return df
