from datetime import datetime
import datetime as dt
import time as t
import random
import csv
import sqlite3
import pandas as pd

from api import get_current_time

conn = sqlite3.connect('data.db')
cur = conn.cursor()

bmp280_pr=None
hdc1080_hu=None
neo6m_la=None 
neo6m_lo=None 
neo6m_al=None
mpu9250_ac=None 
mpu9250_gy=None 
mpu9250_ma=None

for i in range(1, 700):
    print(f'[ {i} ] Running ...')
    now = datetime.now()
    timestamp = now.strftime("%d/%m, %H:%M:%S ")
    bmp280_te = random.randint(1, 100)
    hdc1080_te = random.randint(1, 100)

    cur.execute('''
        INSERT INTO data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
        (timestamp, get_current_time(), bmp280_te, bmp280_pr, hdc1080_te, hdc1080_hu, 
        neo6m_la, neo6m_lo, neo6m_al, mpu9250_ac, mpu9250_gy, mpu9250_ma))
    t.sleep(1)
    conn.commit()

cur.close()
