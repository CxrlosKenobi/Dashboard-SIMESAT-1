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

for i in range(1, 700):
    print(f'[ {i} ] Running ...')
    now = datetime.now()
    timestamp = now.strftime("%d/%m, %H:%M:%S ")
    bmp280 = random.randint(1, 100)
    hdc1080 = random.randint(1, 100)
    neo6m = random.randint(1, 100)
    mpu9250 = random.randint(1, 100)
    camera = random.randint(1, 100)
    cur.execute('INSERT INTO data VALUES (?, ?, ?, ?, ?, ?, ?)', (timestamp, get_current_time(), bmp280, hdc1080, neo6m, mpu9250, camera))
    t.sleep(1)
    conn.commit()

cur.close()
