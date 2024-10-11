import asyncio
import os
import python_weather
from output1 import output 

async def get_weather(city):
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather = await client.get(city)
        return f"Current temperature in {city}: {weather.temperature}°C"

def temperature():
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    city = input("Enter the city you want to see the temperature for: ")
    weather_info = asyncio.run(get_weather(city))
    output(weather_info)