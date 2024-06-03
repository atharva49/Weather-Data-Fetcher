import requests
from config import API_KEY,API_URL
from database import create_weather_table, insert_weather_data

def fetch_weather_data(city):
    response = requests.get(API_URL, params={
        'q' : city,
        'appid' : API_KEY,
        'units' : 'metrics'
    })
    return response.json()

def main():
    create_weather_table()

    cities = ['London','New York','Tokyo']

    for city in cities:
        data = fetch_weather_data(city)
        if data and data['cod'] == 200:
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            insert_weather_data(city, temperature, description)
            print(f"Data for {city} inserted successfully.")
        else:
            print(f"Failed to fetch data for {city}. Error: {data['message']}")
        pass

    

if __name__ == '__main__':
    main()    