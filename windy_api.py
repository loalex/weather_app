import json
import requests

def fetch_windy_data():
    API_KEY = "tvt0g6AqPDQ5tYN2e58BAVvAoRrjAaH3"
    API_URL = "https://api.windy.com/api/point-forecast/v2"

    headers = {
        'Content-Type': 'application/json',
    }

    payload = {
        "lat": 54.516,
        "lon": 18.556,
        "model": "gfs",
        "parameters": ["wind", "dewpoint", "rh", "pressure"],
        "levels": ["surface", "800h", "300h"],
        "key": API_KEY
    }

    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(response.json())
            print(f"Błąd podczas pobierania danych: {response.status_code}")
            print(f"Treść odpowiedzi: {response.text}")
            return None
    except requests.RequestException as e:
        print(f"Wystąpił błąd sieci: {e}")
        return None

##fetch_windy_data()
