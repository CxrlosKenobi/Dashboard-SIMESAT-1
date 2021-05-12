from sqlalchemy import Table
from sqlalchemy.sql import select
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from config import engine

import sqlite3
import csv
import os

inp = input('\nAre you sure to delete data.db ? y/n: ')
if inp == 'n':
    exit()

os.system('rm -rf data.db && touch data.db')
conn = sqlite3.connect('data.db')
cur = conn.cursor()
print('\n[ ok ] Now connected to the database!')

cur.execute(
"""
CREATE TABLE data(
    timestamp VARCHAR(40),
    timeinsec VARCHAR(40),
    bmp280_te VARCHAR(40),
    bmp280_pr VARCHAR(40),
    hdc1080_te VARCHAR(40),
    hdc1080_hu VARCHAR(40),
    neo6m_la VARCHAR(40),
    neo6m_lo VARCHAR(40),
    neo6m_al VARCHAR(40),
    mpu9250_ac_x VARCHAR(40),
    mpu9250_ac_y VARCHAR(40),
    mpu9250_ac_z VARCHAR(40),
    mpu9250_gy_x VARCHAR(40),
    mpu9250_gy_y VARCHAR(40),
    mpu9250_gy_z VARCHAR(40),
    mpu9250_ma_x VARCHAR(40),
    mpu9250_ma_y VARCHAR(40),
    mpu9250_ma_z VARCHAR(40),
    PRIMARY KEY (timestamp),
    UNIQUE (timestamp)
);
"""
)
conn.commit()
cur.close()

print('[ ok ] Db has been sucesfully created!')

db = SQLAlchemy()

class Data(db.Model):
    timestamp = db.Column(db.String(40), primary_key=True, unique=True) 
    timeinsec = db.Column(db.String(40))
    bmp280_te = db.Column(db.String(40))
    bmp280_pr = db.Column(db.String(40))
    hdc1080_te = db.Column(db.String(40))
    hdc1080_hu = db.Column(db.String(40)) 
    neo6m_la = db.Column(db.String(40))
    neo6m_lo = db.Column(db.String(40))
    neo6m_al = db.Column(db.String(40))
    mpu9250_ac_x = db.Column(db.String(40))
    mpu9250_ac_y = db.Column(db.String(40))
    mpu9250_ac_z = db.Column(db.String(40))
    mpu9250_gy_x = db.Column(db.String(40))
    mpu9250_gy_y = db.Column(db.String(40))
    mpu9250_gy_z = db.Column(db.String(40))
    mpu9250_ma_x = db.Column(db.String(40))
    mpu9250_ma_y = db.Column(db.String(40))
    mpu9250_ma_z = db.Column(db.String(40))

Data_tbl = Table('data', Data.metadata)


def create_data_table():
    Data.metadata.create_all(engine)

def add_data(timestamp, timeinsec, bmp280_te, bmp280_pr, hdc1080_te, hdc1080_hu, 
neo6m_la, neo6m_lo, neo6m_al, mpu9250_ac_x, mpu9250_ac_y, mpu9250_ac_z, mpu9250_gy_x, 
mpu9250_gy_y, mpu9250_gy_z, mpu9250_ma_x, mpu9250_ma_y, mpu9250_ma_z):
    ins = Data_tbl.insert().values(
        timestamp=timestamp,
        timeinsec=timeinsec,
        bmp280_te=bmp280_te,
        bmp280_pr=bmp280_pr,
        hdc1080_te=hdc1080_te, 
        hdc1080_hu=hdc1080_hu,
        neo6m_la=neo6m_la, 
        neo6m_lo=neo6m_lo, 
        neo6m_al=neo6m_al,
        mpu9250_ac_x=mpu9250_ac,
        mpu9250_ac_y=mpu9250_ac_y,
        mpu9250_ac_z=mpu9250_ac_z, 
        mpu9250_gy_x=mpu9250_gy_x,
        mpu9250_gy_y=mpu9250_gy_y,
        mpu9250_gy_z=mpu9250_gy_z, 
        mpu9250_ma_x=mpu9250_ma_x,
        mpu9250_ma_y=mpu9250_ma_y,
        mpu9250_ma_z=mpu9250_ma_z
    )
    conn = engine.connect()
    conn.execute(ins)
    conn.close()

# def del_data(code):
#     delete = Data_tbl.delete().where(Data_tbl.c.timestamp == timestamp)
#     conn = engine.connect()
#     conn.execute(delete)
#     conn.close()


# def show_data():
#     select_st = select([Data_tbl.c.timestamp, Data_tbl.c.timeinsec, Data_tbl.c.bmp280, Data_tbl.c.hdc1080, Data_tbl.c.neo6m, Data_tbl.c.mpu9250, Data_tbl.c.camera])
#     conn = engine.connect()
#     rs = conn.execute(select_st)
#     for row in rs:
#         print(row)

#     conn.close()


inp = input('\nAre you sure to delete datarand.db ? y/n: ')
if inp == 'n':
    exit()

os.system('rm -rf datarand.db && touch datarand.db')
conn = sqlite3.connect('datarand.db')
cur = conn.cursor()
print('\n[ ok ] Now connected to the rand database!')

cur.execute(
"""
CREATE TABLE data(
    timestamp VARCHAR(40),
    timeinsec VARCHAR(40),
    bmp280_te VARCHAR(40),
    bmp280_pr VARCHAR(40),
    hdc1080_te VARCHAR(40),
    hdc1080_hu VARCHAR(40),
    neo6m_la VARCHAR(40),
    neo6m_lo VARCHAR(40),
    neo6m_al VARCHAR(40),
    mpu9250_ac VARCHAR(40),
    mpu9250_gy VARCHAR(40),
    mpu9250_ma VARCHAR(40),
    mpu9250_ac_x VARCHAR(40),
    mpu9250_ac_y VARCHAR(40),
    mpu9250_ac_z VARCHAR(40),
    mpu9250_gy_x VARCHAR(40),
    mpu9250_gy_y VARCHAR(40),
    mpu9250_gy_z VARCHAR(40),
    mpu9250_ma_x VARCHAR(40),
    mpu9250_ma_y VARCHAR(40),
    mpu9250_ma_z VARCHAR(40),
    PRIMARY KEY (timestamp),
    UNIQUE (timestamp)
);
"""
)
conn.commit()
cur.close()

print('[ ok ] Db (rand) has been sucesfully created!')

db = SQLAlchemy()

class Data(db.Model):
    timestamp = db.Column(db.String(40), primary_key=True, unique=True) 
    timeinsec = db.Column(db.String(40))
    bmp280_te = db.Column(db.String(40))
    bmp280_pr = db.Column(db.String(40))
    hdc1080_te = db.Column(db.String(40))
    hdc1080_hu = db.Column(db.String(40)) 
    neo6m_la = db.Column(db.String(40))
    neo6m_lo = db.Column(db.String(40))
    neo6m_al = db.Column(db.String(40))
    mpu9250_ac = db.Column(db.String(40))
    mpu9250_gy = db.Column(db.String(40))
    mpu9250_ma = db.Column(db.String(40))
    mpu9250_ac_x = db.Column(db.String(40))
    mpu9250_ac_y = db.Column(db.String(40))
    mpu9250_ac_z = db.Column(db.String(40))
    mpu9250_gy_x = db.Column(db.String(40))
    mpu9250_gy_y = db.Column(db.String(40))
    mpu9250_gy_z = db.Column(db.String(40))
    mpu9250_ma_x = db.Column(db.String(40))
    mpu9250_ma_y = db.Column(db.String(40))
    mpu9250_ma_z = db.Column(db.String(40))

Data_tbl = Table('data', Data.metadata)


def create_data_table():
    Data.metadata.create_all(engine)

def add_data(timestamp, timeinsec, bmp280_te, bmp280_pr, hdc1080_te, hdc1080_hu, 
neo6m_la, neo6m_lo, neo6m_al, mpu9250_ac, mpu9250_gy, mpu9250_ma, mpu9250_ac_x, mpu9250_ac_y, mpu9250_ac_z, mpu9250_gy_x, 
mpu9250_gy_y, mpu9250_gy_z, mpu9250_ma_x, mpu9250_ma_y, mpu9250_ma_z):
    ins = Data_tbl.insert().values(
        timestamp=timestamp,
        timeinsec=timeinsec,
        bmp280_te=bmp280_te,
        bmp280_pr=bmp280_pr,
        hdc1080_te=hdc1080_te, 
        hdc1080_hu=hdc1080_hu,
        neo6m_la=neo6m_la, 
        neo6m_lo=neo6m_lo, 
        neo6m_al=neo6m_al,
        mpu9250_ac=mpu9250_ac,
        mpu9250_gy=mpu9250_gy,
        mpu9250_ma=mpu9250_ma,
        mpu9250_ac_x=mpu9250_ac,
        mpu9250_ac_y=mpu9250_ac_y,
        mpu9250_ac_z=mpu9250_ac_z, 
        mpu9250_gy_x=mpu9250_gy_x,
        mpu9250_gy_y=mpu9250_gy_y,
        mpu9250_gy_z=mpu9250_gy_z, 
        mpu9250_ma_x=mpu9250_ma_x,
        mpu9250_ma_y=mpu9250_ma_y,
        mpu9250_ma_z=mpu9250_ma_z
    )
    conn = engine.connect()
    conn.execute(ins)
    conn.close()
