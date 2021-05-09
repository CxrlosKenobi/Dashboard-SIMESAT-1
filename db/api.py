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

packet = '08-05,14:57:21;15512;38.66,950.60;36.8,29.1;-36.121,-71.814,190.985;-0.00179,0.007725,1.001726;-0.00179,0.007725,1.001726;-0.00179, 0.007725,1.001726'
# 08-05,14:57:21 ; 15512 ; 38.66,950.60 ; 36.8,29.1 ; -36.121,-71.814,190.985 ; -0.00179,0.007725,1.001726 ; -0.00179,0.007725,1.001726 ; -0.00179, 0.007725,1.001726

timestamp = packet.split(';')[0]
timeinsec = packet.split(';')[1]

bmp_280 = packet.split(';')[2]
bmp_280_te = float(bmp_280.split(',')[0])
bmp_280_pr = float(bmp_280.split(',')[1])

hdc1080 = packet.split(';')[3]
hdc1080_te = float(hdc1080.split(',')[0])
hdc1080_hu = float(hdc1080.split(',')[1])

neo6m = packet.split(';')[4]
neo6m_la = float(neo6m.split(',')[0])
neo6m_lo = float(neo6m.split(',')[1])
neo6m_al = float(neo6m.split(',')[2])

mpu9250_ac = float(packet.split(';')[5])
mpu9250_gy = float(packet.split(';')[6])
mpu9250_ma = float(packet.split(';')[7])
