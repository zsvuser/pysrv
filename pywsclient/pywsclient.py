''' Подписываемся на websocket из конфига
    выводим полученные данные в терминал
'''
import asyncio
import websockets

async def hello():
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send("Hello world!")
        await websocket.recv()

asyncio.run(hello())