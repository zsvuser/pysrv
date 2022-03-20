'''Читаем данные из конфига, подключаемся к БД
   При изменении в БД генерируем событие на websocket
'''

import serial
import asyncio
import websockets

def hme280Data ():
  ser = serial.Serial("/dev/ttyACM0")
  ser.baudrate = 9600
  while True :
    print (ser.readline())
  return

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())





  