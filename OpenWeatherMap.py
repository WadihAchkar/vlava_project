import requests
import datetime

def check_country_existence(country):
    url = "https://countriesnow.space/api/v0.1/countries"
    response = requests.get(url)
    data = response.json()
    countries = [country['country'] for country in data['data']]
    return country in countries

def check_city_existence(city, country):
    url = "https://countriesnow.space/api/v0.1/countries"
    response = requests.get(url)
    data = response.json()
    for country_data in data['data']:
        if country_data['country'] == country:
            cities = [city for city in country_data['cities']]
            return city in cities
    return False

def get_weather_data(city):
    #api_key = "http://api.openweathermap.org/data/2.5/weather?q=Berlin%20Tempelhof,DE&units=metric&lang=de&APPID=0815"  # OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=de&APPID=62ecb81fe2c18121a5a0c4029bfb3ccb"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        # Extract the required information from the JSON response
        temperature = data['main']['temp']  # Convert temperature to Celsius
        weather_description = data['weather'][0]['description']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S')
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')
        wind_speed = data['wind']['speed'] * 3.6  # Convert wind speed to km/h
        cloudiness = data['clouds']['all']
        last_updated = datetime.datetime.fromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')

        # Print the information
        print("Temperatur: {:.2f} °C".format(temperature))
        print("Wetter: {}".format(weather_description))
        print("Sonnenaufgang: {}".format(sunrise))
        print("Sonnenuntergang: {}".format(sunset))
        print("Windgeschwindigkeit: {:.2f} km/h".format(wind_speed))
        print("Bewölkung: {} %".format(cloudiness))
        print("Aktualisiert am: {}".format(last_updated))
    else:
        print("Fehler beim Abrufen der Wetterdaten.")

def get_user_input():
    country = input("Bitte geben Sie ein Land ein: ")
    city = input("Bitte geben Sie eine Stadt ein: ")

    if not check_country_existence(country):
        print("Das angegebene Land existiert nicht.")
        return
    if not check_city_existence(city, country):
        print(f"Die Stadt {city} gibt es nicht in {country}.")
        return

    get_weather_data(city)

get_user_input()

#-------------------------------------------------------------------

import streamlit as st
st.write("""Hallo Wadih""")
