'''Читаем данные из конфига, подключаемся к БД
   При изменении в БД генерируем событие на websocket
'''

import serial

def hme280Data ()
  return

#import websockets
ser = serial.Serial("/dev/ttyACM0")
ser.baudrate = 9600
 
while True :
  print (ser.readline())
  