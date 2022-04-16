import asyncio
import websockets
import numpy as np
import json 
import sympy
import time 

def process_json(list_dict_response):
    """ Computa la información de un bloque de 100 diccionarios
     que vienen en una lista 
    """
    a = [_dict["a"] for _dict in list_dict_response]
    b = [_dict["b"] for _dict in list_dict_response]
    _max_number =max(b)
    min_number =min(b)
    firts_number =b[0]
    last_number =b[-1]
    number_of_prime_numbers =sum([sympy.isprime(x) for x in b])
    number_of_even_numbers =sum([x%2 == 0 for x in b])
    number_of_odd_numbers =sum([x%2 != 0 for x in b])
    return {'_max_number':_max_number,
            'min_number':min_number,
            'fist_number':firts_number,
            'last_number':last_number,
            'number_of_prime_numbers':number_of_prime_numbers,
            'number_of_even_numbers':number_of_even_numbers,
            'number_of_odd_numbers':number_of_odd_numbers}
async def test():
    # Se conecta con el server
    async with websockets.connect('ws://localhost:8000') as websocket:
        while True:
            data=[]
            # Se leen 600 datos de 100 bloques equivalente a 1 minuto de información
            for i in range (600):
                response = await websocket.recv()
                list = json.loads(response)
                data.append(list)

            result = process_json(np.array(data).reshape(-1,))
            print(result)
asyncio.get_event_loop().run_until_complete(test())