import smbus2
import bme280
import os
import time
import MySQLdb


port= 1
address = 0x77
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus,address)

#single reading return an object



db = MySQLdb.connect("localhost","mysql_user","*****","DB_POMIARY")
c = db.cursor()



while 1:
    data = bme280.sample(bus,address,calibration_params)
    temp = round(data.temperature,3)
    hum =round(data.humidity,2)
    pres = round(data.pressure,2)
    sql="INSERT INTO TAB_POMIARY (TEMP, HUMI, PRES) VALUES(%s,%s,%s)"
    pomiar=(temp,hum,pres)
    c.execute(sql,pomiar)
    db.commit()
    print(data.temperature)
    print(data.humidity)
    print(data.pressure)
    time.sleep(1800)
        
