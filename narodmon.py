#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# by Pavlov Sergey psp911 @ yandex.ru

import socket
import Adafruit_DHT as dht


# MAC адрес прибора. Заменить на свой! Без двоеточий
DEVICE_MAC = '0123456789012'



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


# создание сокета
sock = socket.socket()

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
