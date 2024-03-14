'''API: Application Programming interface
Nasa API: https: //api.nasa.gov/
API_KEY_NASA: a8u4kO1Kt9vFlS8FzbGtJbUixhOzZu38xl7LzjBq
Developer: John J Erazo
Date: 24012024
Scrip description: Get and read data from NASA API about comets
'''


import requests
import os


os.system('clear')
def get_comet_data(api_key):
    print(":::COMET INFORMATION:::")
    url = f"https://?api_key={api_key}"

    try:
        #Realizar la solicitud a la API 
        response =requests.get(url)
        response.raise_for_status()#=> Valida si se presenta algún error en la petición
        #Convertir la respuesta a formato JSON (JS Object Notation)
        datos = response.json()

        print(f"comet name: {datos['name']}")
        print(f"Absolute magnitude: {datos['absolute_magnitude_h']}")
        print(f"Estimated diameter max (KM): {datos['absolute_magnitude_h']}")
        except requests.exceptions.RequestException as e:
        print(f"Error al realizar la petición a la API de Nasa: {e}")
        

    api_key_nasa = 'a8u4kO1Kt9vFlS8FzbGtJbUixhOzZu38xl7LzjBq'
    get_comet_data(api_key_nasa)



