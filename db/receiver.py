import adafruit_rfm9x
import digitalio
import time as t
import board
import busio

from datetime import datetime
import datetime as dt
import time as t
import random
import csv
import sqlite3
import pandas as pd

from api import get_current_time

def receivePackets():
    RADIO_FREQ_MHZ = 915.0
    CS = digitalio.DigitalInOut(board.CE1)
    RESET = digitalio.DigitalInOut(board.D25)
    spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

    rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ, baudrate=1000000)
    rfm9x.tx_power = 23

    times = 0

    packet = rfm9x.receive(timeout=3)

    if packet is not None:
        packet_text = str(packet, 'ascii')
        rssi = rfm9x.last_rssi
        times += 1

        return packet, rssi, packet_text # RAW bytes, signal strength, ASCII

    elif packet is None:
        return '[ ! ] The conection is interrupted.'


conn = sqlite3.connect('data.db')
cur = conn.cursor()

for i in range(1200):
    now = datetime.now()
    packet = receivePackets()
    print(packet)

    timestamp = packet.split(';')[0]
    timeinsec = int(packet.split(';')[1])

    bmp_280 = packet.split(';')[2]
    bmp_280_pr = float(bmp_280.split(',')[0])
    bmp_280_al = float(bmp_280.split(',')[1])

    hdc1080 = packet.split(';')[3]
    hdc1080_te = float(hdc1080.split(',')[0])
    hdc1080_hu = float(hdc1080.split(',')[1])

    neo6m = packet.split(';')[4]
    neo6m_la = float(neo6m.split(',')[0])
    neo6m_lo = float(neo6m.split(',')[1])

    #mpu9250_ac = float(packet.split(';')[5])
    mpu9250_gy = packet.split(';')[6]
    #mpu9250_ma = float(packet.split(';')[7])

    cur.execute('''
        INSERT INTO data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
        (timestamp, timeinsec, bmp280_te, bmp280_pr, hdc1080_te, hdc1080_hu, 
        neo6m_la, neo6m_lo, neo6m_al, mpu9250_ac, mpu9250_gy, mpu9250_ma))
    t.sleep(1)
    conn.commit()

cur.close()

# payload = f"{now.strftime('%d/%m, %H:%M:%S')};{get_current_time()};{bmp280_pr},{bmp_al};{hdc1080_te},{hdc1080_hu};{neo6m_la},{neo6m_lo};{mpu9250_ac};{mpu9250_gy};{mpu9250_ma}" 
# 10/05, 00:54:37;3277;953.1327266909368,-9.843237336326638e-12;28.0,33.0;NO DATA,NO DATA;[0.00022, 0.000744, 0.999976];[-0.264238, 0.029215, 0.27838];[-0.748734, 1.074211, 0.075914]
