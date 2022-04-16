import asyncio
from unittest import result
import websockets
import json 
import sympy
import time 
# Se conecta con el server y muestra los resultados
async def test():
    async with websockets.connect('ws://localhost:8000') as websocket:
        while True:
            response = await websocket.recv()
            result = json.loads(response)
            print(result)
asyncio.get_event_loop().run_until_complete(test())