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

for i in range(1400):
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
    
    mpu9250_gy_x = float(mpu9250_gy[0])
    mpu9250_gy_y = float(mpu9250_gy[1])
    mpu9250_gy_z = float(mpu9250_gy[2])

    mpu9250_ma_x = float(mpu9250_ma[0])
    mpu9250_ma_y = float(mpu9250_ma[1])
    mpu9250_ma_z = float(mpu9250_ma[2])


    cur.execute('''
        INSERT INTO data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
        (timestamp, timeinsec, bmp280_pr, bmp280_te, hdc1080_te, hdc1080_hu, 
        neo6m_la, neo6m_lo, neo6m_al, mpu9250_ac_x, mpu9250_ac_y, mpu9250_ac_z, mpu9250_gy_x, mpu9250_gy_y, mpu9250_gy_z, mpu9250_ma_x, mpu9250_ma_y, mpu9250_ma_z))
    t.sleep(1)
    conn.commit()

cur.close()

# payload = f"{now.strftime('%d/%m, %H:%M:%S')};{get_current_time()};{bmp280_pr},{bmp_al};{hdc1080_te},{hdc1080_hu};{neo6m_la},{neo6m_lo};{mpu9250_ac};{mpu9250_gy};{mpu9250_ma}" 
# 10/05, 00:54:37;3277;953.1327266909368,-9.843237336326638e-12;28.0,33.0;NO DATA,NO DATA;[0.00022, 0.000744, 0.999976];[-0.264238, 0.029215, 0.27838];[-0.748734, 1.074211, 0.075914]

# (bytearray(b'10/05, 12:33:06;45186;952.03,-0.0;28.4,31.7;NO DATA,NO DATA;[-0.005955, 0.001066, 0.996308];[-0.005024, -0.181059, 0.011165];[0.088003, 0.0, 0.425541]'), -53, '10/05, 12:33:06;45186;952.03,-0.0;28.4,31.7;NO DATA,NO DATA;[-0.005955, 0.001066, 0.996308];[-0.005024, -0.181059, 0.011165];[0.088003, 0.0, 0.425541]')
# (bytearray(b'10/05, 12:33:06 ; 45186; 952.03,-0.0; 28.4,31.7 ; NO DATA,NO DATA ; [-0.005955, 0.001066, 0.996308] ; [-0.005024, -0.181059, 0.011165] ; [0.088003, 0.0, 0.425541]'), -53, '10/05, 12:33:06;45186;952.03,-0.0;28.4,31.7;NO DATA,NO DATA;[-0.005955, 0.001066, 0.996308];[-0.005024, -0.181059, 0.011165];[0.088003, 0.0, 0.425541]')
