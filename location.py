import requests

def get_coordinates(place_name):

    url = f"https://api.opencagedata.com/geocode/v1/json?q=52.3877830%2C9.7334394&&key=03705712e0b943f6b062e7059a912eba"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()['results']
        if results:
            lat = results[0]['geometry']['lat']
            lon = results[0]['geometry']['lng']
            return lat, lon
    print("Nie udało się znaleźć lokalizacji.")
    return None, None
