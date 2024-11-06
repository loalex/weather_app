from weatherbit.api import Api

def fetch_weatherbit_data():
# API KEY obtained from https://www.weatherbit.io
    api_key = "e7f4bdfe9101470982721ecc9e87f4f3"


    lat = 38.00
    lon = -125.75

    api = Api(api_key)

# Set the granularity of the API - Options: ['daily','hourly','subhourly']
# Depends on supported granularity of API - please see https://www.weatherbit.io/api
# Currently supported:
# History: daily, hourly, subhourly
# Forecast: daily, hourly
# Air quality: hourly
# Will only affect forecast requests.
    api.set_granularity('daily')

# Query by lat/lon
    forecast = api.get_forecast(lat=lat, lon=lon)

# You can also query by city:
    forecast = api.get_forecast(city="Raleigh,NC")

# Or City, state, and country:
    forecast = api.get_forecast(city="Raleigh", state="North Carolina", country="US")

    # To get a daily forecast of temperature, and precipitation:
    print(forecast.get_series(['temp', 'precip', 'solar_rad']))

    # Get an hourly air quality forecast for a lat/lon
    forecast_AQ = api.get_forecast(source='airquality', lat=lat, lon=lon)
    print(forecast_AQ.get_series(['aqi', 'pm10', 'no2']))


# Get hourly history by lat/lon
    api.set_granularity('hourly')
    history = api.get_history(lat=lat, lon=lon, start_date='2018-02-01', end_date='2018-02-02')

# To get an hourly time series of temperature, precipitation, and rh:
    print(history.get_series(['precip', 'temp', 'rh', 'solar_rad']))

# Get historical air quality data
    history_AQ = api.get_history(source='airquality', lat=lat, lon=lon, start_date='2018-02-01', end_date='2018-02-02')
    print(history_AQ.get_series(['aqi', 'pm10', 'no2']))

### Current Conditions

# Get current air quality
    AQ = api.get_current(source='airquality', city="Raleigh", state="North Carolina", country="US")
    print(AQ.get_series(['aqi', 'pm10', 'pm25']))

# Get current conditions
    current_weather = api.get_current(city="Raleigh", state="North Carolina", country="US")
    print(current_weather.get_series(['weather', 'temp', 'precip']))

#nie dziala