
//A program to fetch and display weather information for a city using an API.
import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        print(f"Temperature: {main['temp']}°C")
        print(f"Weather: {weather['description']}")
    else:
        print("City not found.")

city = input("Enter city name: ")
get_weather(city)
