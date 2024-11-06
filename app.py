from windy_api import fetch_windy_data
from location import get_coordinates  # jeśli chcemy obsługiwać nazwy miejscowości
from openweatherapp_api import fetch_weatherapp_data
from weatherapi_api import fetch_weatherapi_data
from bibliotekapyth import getweather
from weatherbit_api import fetch_weatherbit_data
from virtualcrossing_api import fetch_virtualcrossing_data
def get_location_input():
    choice = input(
        "Wybierz sposób wprowadzenia lokalizacji:\n1. Wpisz nazwę miejscowości\n2. Wprowadź współrzędne geograficzne\n> ")

    if choice == "1":
        place_name = input("Wpisz nazwę miejscowości: ")
        lat, lon = get_coordinates(place_name)
        return lat, lon
    elif choice == "2":
        lat = float(input("Podaj szerokość geograficzną: "))
        lon = float(input("Podaj długość geograficzną: "))
        return lat, lon
        print(lon)
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
        return get_location_input()


def main():
    print("Aplikacja pogodowa")

    # Pobieranie danych z API
    #data = fetch_windy_data()
    #data2 = fetch_weatherapp_data()
    #data3 = fetch_weatherapi_data()
    #data4 = asyncio.run(getweather())
    data5 = fetch_weatherbit_data()
    #data6 = fetch_virtualcrossing_data()


if __name__ == "__main__":
    main()
