import requests

city = input("Enter city name: ")
api_key = "1e5b7674a9a0089ea36ff7c1e2712803" # Get your API key by signing up at https://openweathermap.org/api

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    weather_data = response.json()
    print(f"Weather in {city}: {weather_data['weather'][0]['description']}, Temperature: {weather_data['main']['temp']}°C")
else:
    print("Error while fetching weather data")
