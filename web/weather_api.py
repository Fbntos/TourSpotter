import requests
from decouple import config

API_KEY = config('API_KEY')
to_celcius = lambda x : round(float(x) - 273.15, 1)
lang = 'es'

# Funcion para obtener la latitud de una ciudad a traves de la API
def get_geo(ciudad:str): 
    # URL de la api en donde se introducen la ciudad y la API KEY definida anteriormente
    api_url = f'http://api.openweathermap.org/geo/1.0/direct?q={ciudad}&limit=5&appid={API_KEY}'
    # Almaceno la respuesta en la variable R a traves de la funcion .get de requests 
    r = requests.get(api_url)

    if r.text == '[]' or ciudad == '':
        return None
    else:
        name = r.json()[0]['name']
        country = r.json()[0]['country']
        lat = r.json()[0]['lat']
        lon = r.json()[0]['lon']
        return {'name':name,'country':country,'lat':lat,'lon':lon}
    
def get_clima(lon: str, lat:str):
    api_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&lang={lang}&units=metric'
    r = requests.get(api_url)
    # Alternativa de convertir R al tiro en json
    # r = requests.get(api_url).json()
    if r.text == '[]':
        return None
    else:
        clima = r.json()['weather'][0]
        # response -> {'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}
        
        #Agrego una nueva clave al diccionario 
        clima['img'] = f"http://openweathermap.org/img/wn/{clima['icon']}@2x.png"
        main = r.json()['main']
        # CON EL CAMBIO QUE HICE EN LA API URL ME DEVUELVE LOS DATOS EN CELCIUS &units=metrics
        # main['celcius'] = to_celcius(main['temp'])
        # main['min'] = to_celcius(main['temp_min'])
        # main['max'] = to_celcius(main['temp_max'])
        # En este return se hace un merge, se combinan ambos diccionarios creando uno nuevo con sus clases y valores
        return clima | main


dict = get_geo('valdivia')
lat = dict['lat'] 
lon = dict['lon']
 
print(get_clima(lon,lat))
