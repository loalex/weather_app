import requests

def fetch_weatherapp_data():

    api_key = '0d1764dc7eace6612e7d9a5e1168371f'

    city = input('Enter city name: ')

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        temp = temp - 273.15
        wind_speed = data['wind']['speed']
        wind_direction = data['wind']['deg']
        desc = data['weather'][0]['description']
        print(f'Temperature: {temp} C')
        print(f'Wind speed: {wind_speed} m/s' )
        print(f'Wind direction: {wind_direction}')
        print(f'Description: {desc}')
    else:
        print('Error fetching weather data')
