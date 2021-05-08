from sqlalchemy import Table
from sqlalchemy.sql import select
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from config import engine

import sqlite3
import csv
import os

os.system('rm -rf data.db && touch data.db')
conn = sqlite3.connect('data.db')
cur = conn.cursor()
print('\n[ ok ] Now connected to the database!')

cur.execute(
"""
CREATE TABLE data(
    timestamp VARCHAR(40),
    bmp280 VARCHAR(40),
    hdc1080 VARCHAR(40),
    neo6m VARCHAR(40),
    mpu9250 VARCHAR(40),
    camera VARCHAR(40),
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
    bmp280 = db.Column(db.String(40))
    hdc1080 = db.Column(db.String(40))
    neo6m = db.Column(db.String(40))
    mpu9250 = db.Column(db.String(40))
    camera = db.Column(db.String(10))

Data_tbl = Table('data', Data.metadata)


def create_data_table():
    Data.metadata.create_all(engine)

def add_data(timestamp, bmp280, hdc1080, neo6m, mpu9250, camera):
    ins = Data_tbl.insert().values(
        timestamp=timestamp,
        bmp280=bmp280,
        hdc1080=hdc1080,
        neo6m=neo6m,
        mpu9250=mpu9250,
        camera=camera
    )
    conn = engine.connect()
    conn.execute(ins)
    conn.close()

def del_data(code):
    delete = Data_tbl.delete().where(Data_tbl.c.timestamp == timestamp)
    conn = engine.connect()
    conn.execute(delete)
    conn.close()


def show_data():
    select_st = select([Data_tbl.c.timestamp, Data_tbl.c.bmp280, Data_tbl.c.hdc1080, Data_tbl.c.neo6m, Data_tbl.c.mpu9250, Data_tbl.c.camera])
    conn = engine.connect()
    rs = conn.execute(select_st)
    for row in rs:
        print(row)

    conn.close()
