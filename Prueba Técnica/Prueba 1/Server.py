import asyncio
import websockets
import json
import random 
import time
#Esta función se encarga de generar los datos 
def data():
    dict_ = {"a": random.randint(1,101),
            "b": random.randint(0, 2**32)}
    return dict_
#Función para garantizar el envío de 100 json cada 100ms
def Tim():
    time.sleep(0.1)
# Crea una conexión y envía los datos
async def Server(websocket, path):
    while True:
        await websocket.send(json.dumps([data() for i in range(100)]))
        Tim()
start_server = websockets.serve(Server, "localhost", 8000)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()