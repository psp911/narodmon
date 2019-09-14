#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# by Roman Vishnevsky aka.x0x01 @ gmail.com

import socket
import Adafruit_DHT as dht
import sys


# MAC адрес прибора. Заменить на свой!
#DEVICE_MAC = '0123456789012'
#b8:27:eb:5c:95:a8
DEVICE_MAC = 'b827eb5c95a8'


# идентификатор прибора, для простоты добавляется 01 (02) к mac прибора
SENSOR_ID_1 = DEVICE_MAC + '01'
SENSOR_ID_2 = DEVICE_MAC + '02'

#Получаем данные с датчика на улице
sensor = 22
pin2 = 18
humidity2, temperature2 = dht.read_retry(sensor, pin2)

# значения датчиков, тип float/integer
# sensor_value_1 = 20
sensor_value_1 = temperature2
#sensor_value_2 = -20.25
sensor_value_2 = humidity2

if (humidity2 is not None) and (temperature2 is not None):
    # создание сокета
    sock = socket.socket()
else:
    print("Exit, Error DHT: value None")
    sys.exit()



# обработчик исключений
try:
    # подключаемся к сокету
    sock.connect(('narodmon.ru', 8283))

    # пишем в сокет единичное значение датчика
    #sock.send("#{}\n#{}#{}\n##".format(DEVICE_MAC, SENSOR_ID_1, sensor_value_1))

    # пишем в сокет множественные значение датчиков
    sock.send("#{}\n#{}#{}\n#{}#{}\n##".format(DEVICE_MAC, SENSOR_ID_1, sensor_value_1, SENSOR_ID_2, sensor_value_2))

    # читаем ответ
    data = sock.recv(1024)
    sock.close()
    print data
except socket.error, e:
    print('ERROR! Exception {}'.format(e))
