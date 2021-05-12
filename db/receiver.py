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
delete = ['(', ')', 'bytearray', 'b', "'"]
subdelete = ['[', ']']

while True:
    try:
        now = datetime.now()
        packet = receivePackets()
        print(packet)

        packet = str(packet[0])
        for i in delete:
            packet = packet.replace(f"{i}", '')
        packet = packet.split(';')

        timestamp = packet[0]
        timeinsec = int(packet[1])

        bmp280 = packet[2]
        bmp280_pr = float(bmp280.split(',')[0])
        bmp280_te = float(bmp280.split(',')[1])

        hdc1080 = packet[3]
        hdc1080_te = float(hdc1080.split(',')[0])
        hdc1080_hu = float(hdc1080.split(',')[1])

        neo6m = packet[4]
        neo6m_la = '01'
        neo6m_lo = '01'
        neo6m_al = '01'
        # neo6m_la = float(neo6m.split(',')[0])
        # neo6m_lo = float(neo6m.split(',')[1])

        mpu9250_ac = str(packet[5])
        mpu9250_gy = str(packet[6])
        mpu9250_ma = str(packet[7])

        for i in subdelete:
            mpu9250_ac = mpu9250_ac.replace(f"{i}", '')
            mpu9250_gy = mpu9250_gy.replace(f"{i}", '')
            mpu9250_ma = mpu9250_ma.replace(f"{i}", '')

        mpu9250_ac = mpu9250_ac.split(',')
        mpu9250_gy = mpu9250_gy.split(',')
        mpu9250_ma = mpu9250_ma.split(',')

        mpu9250_ac_x = float(mpu9250_ac[0])
        mpu9250_ac_y = float(mpu9250_ac[1])
        mpu9250_ac_z = float(mpu9250_ac[2])
        
        mpu9250_gy_x = round(float(mpu9250_gy[0]), 3)
        mpu9250_gy_y = round(float(mpu9250_gy[1]), 3)
        mpu9250_gy_z = round(float(mpu9250_gy[2]), 3)

        mpu9250_ma_x = float(mpu9250_ma[0])
        mpu9250_ma_y = float(mpu9250_ma[1])
        mpu9250_ma_z = float(mpu9250_ma[2])


        cur.execute('''
            INSERT INTO data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
            (timestamp, timeinsec, bmp280_pr, bmp280_te, hdc1080_te, hdc1080_hu, 
            neo6m_la, neo6m_lo, neo6m_al, mpu9250_ac_x, mpu9250_ac_y, mpu9250_ac_z, mpu9250_gy_x, mpu9250_gy_y, mpu9250_gy_z, mpu9250_ma_x, mpu9250_ma_y, mpu9250_ma_z))
        t.sleep(1)
        conn.commit()

    except (UnicodeDecodeError, IndexError):
        print('\n[ ! ] Error with UnicodeDecode or IndexError ...')
    