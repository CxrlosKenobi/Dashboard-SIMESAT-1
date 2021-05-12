from datetime import datetime
import datetime as dt
import time as t
import random
import csv
import sqlite3
import pandas as pd

from api import get_current_time

conn = sqlite3.connect('datarand.db')
cur = conn.cursor()

for i in range(1, 1400):
    print(f'[ {i} ] Running ...')
    now = datetime.now()
    #   Asign random values to test
    timestamp = now.strftime('%d/%m, %H:%M:%S')
    timeinsec = get_current_time()
    bmp_280 = 0
    bmp280_pr = random.randint(953, 980)
    bmp280_te = random.randint(20, 22)

    hdc1080 = 0
    hdc1080_hu = random.randint(0, 100)
    hdc1080_te = random.randint(20, 22)

    neo6m = 0
    neo6m_la = 0
    neo6m_lo = 0
    neo6m_al = 0

    mpu9250_ac = random.randint(1, 100)
    mpu9250_gy = random.randint(1, 100)
    mpu9250_ma = random.randint(1, 100)

    mpu9250_ac_x = random.randint(0, 100)
    mpu9250_ac_y = random.randint(0, 100)
    mpu9250_ac_z = random.randint(0, 100)

    mpu9250_gy_x = random.randint(0, 100)
    mpu9250_gy_y = random.randint(0, 100)
    mpu9250_gy_z = random.randint(0, 100)

    mpu9250_ma_x = random.randint(0, 100)
    mpu9250_ma_y = random.randint(0, 100)
    mpu9250_ma_z = random.randint(0, 100)

    
    packet = f"""{now.strftime('%d/%m, %H:%M:%S')};{get_current_time()};{bmp280_te},{bmp280_pr};{hdc1080_te},{hdc1080_hu};{neo6m_la},{neo6m_lo},{neo6m_al};{mpu9250_ac_x};{mpu9250_ac_y};{mpu9250_ac_z};{mpu9250_gy_x};{mpu9250_gy_y};{mpu9250_gy_z};{mpu9250_ma_x};{mpu9250_ma_y};{mpu9250_ma_z}"""

    cur.execute('''
        INSERT INTO data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
        (timestamp, timeinsec, bmp280_te, bmp280_pr, hdc1080_te, hdc1080_hu,
        neo6m_la, neo6m_lo, neo6m_al, mpu9250_ac, mpu9250_gy, mpu9250_ma, mpu9250_ac_x, mpu9250_ac_y, mpu9250_ac_z, mpu9250_gy_x, mpu9250_gy_y, mpu9250_gy_z, mpu9250_ma_x, mpu9250_ma_y, mpu9250_ma_z))
    t.sleep(1)
    conn.commit()

cur.close()
