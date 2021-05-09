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

#   Example of packet's format
# packet = '08-05,14:57:21;15512;38.66,950.60;36.8,29.1;-36.121,-71.814,190.985;-0.00179,0.007725,1.001726;-0.00179,0.007725,1.001726;-0.00179,0.007725,1.001726'
# 08-05,14:57:21 ; 15512 ; 38.66,950.60 ; 36.8,29.1 ; -36.121,-71.814,190.985 ; -0.00179,0.007725,1.001726 ; -0.00179,0.007725,1.001726 ; -0.00179, 0.007725,1.001726

#   Decoding
# timestamp = packet.split(';')[0]
# timeinsec = packet.split(';')[1]

# bmp_280 = packet.split(';')[2]
# bmp_280_te = float(bmp_280.split(',')[0])
# bmp_280_pr = float(bmp_280.split(',')[1])

# hdc1080 = packet.split(';')[3]
# hdc1080_te = float(hdc1080.split(',')[0])
# hdc1080_hu = float(hdc1080.split(',')[1])

# neo6m = packet.split(';')[4]
# neo6m_la = float(neo6m.split(',')[0])
# neo6m_lo = float(neo6m.split(',')[1])
# neo6m_al = float(neo6m.split(',')[2])

# mpu9250_ac = float(packet.split(';')[5])
# mpu9250_gy = float(packet.split(';')[6])
# mpu9250_ma = float(packet.split(';')[7])

for i in range(1, 700):
    print(f'[ {i} ] Running ...')
    now = datetime.now()
    #   Asign random values to test
    timestamp = now.strftime('%d/%m, %H:%M:%S')
    timeinsec = get_current_time()
    bmp_280 = 0
    bmp280_pr = 0

    hdc1080 = 0
    hdc1080_hu = 0

    neo6m = 0
    neo6m_la = 0
    neo6m_lo = 0
    neo6m_al = 0

    mpu9250_ac = 0
    mpu9250_gy = 0
    mpu9250_ma = 0

    bmp280_te = random.randint(1, 100)
    hdc1080_te = random.randint(1, 100)
    
    packet = f"""{now.strftime('%d/%m, %H:%M:%S')};{get_current_time()};{bmp280_te},{bmp280_pr};{hdc1080_te},{hdc1080_hu};{neo6m_la},{neo6m_lo},{neo6m_al};{mpu9250_ac};{mpu9250_gy};{mpu9250_ma}"""

    cur.execute('''
        INSERT INTO data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
        (timestamp, timeinsec, bmp280_te, bmp280_pr, hdc1080_te, hdc1080_hu, 
        neo6m_la, neo6m_lo, neo6m_al, mpu9250_ac, mpu9250_gy, mpu9250_ma))
    t.sleep(1)
    conn.commit()

cur.close()
