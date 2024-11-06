from weatherapi import WeatherPoint

def fetch_weatherapi_data():
  # ustawienie punktu
  api_key = '32ac4dbcfb684f52b9275344240311'
  latitude = 54.31
  longitude = 18.31

 # Initializing the WeatherPoint
  point = WeatherPoint(latitude, longitude)

 # Setting the key for data access
  point.set_key(api_key)

 # get current weather data
  point.get_current_weather()


  print(point.temp_c)  # temperature in celsius
  print(point.wind_kph) # wind in kilometers per hour
  print(point.localtime) # local datetime of the request

