import random
import json
from datetime import datetime

# List of some major Indian cities
cities = [
    "New Delhi",
    "Ahmedabad",
    "Bengaluru",
    "Bhopal",
    "Chandigarh",
    "Chennai",
    "Dehradun",
    "Dharamshala",
    "Dispur",
    "Gangtok",
    "Hyderabad",
    "Imphal",
    "Itanagar",
    "Jaipur",
    "Kolkata",
    "Lucknow",
    "Mumbai",
    "Nagpur",
    "Panaji",
    "Patna",
    "Puducherry",
    "Raipur",
    "Ranchi",
    "Shimla",
    "Srinagar",
    "Thiruvananthapuram",
    "Tirupati",
    "Udhampur",
    "Vijayawada",
    "Imphal",
    "Kohima",
    "Port Blair"
]

def generate_random_weather_data(city):
    '''
    This function will genrate....
    Random temperature in Celsius (for example: Delhi can have temperatures between 5 to 45 degrees)
    Random pressure in hPa (typical pressure range: 980 to 1050 hPa)
    Random humidity in percentage (usually between 20 to 90%)
    Random AQI (Air Quality Index) value (can range from 0 to 500)
    Current date and time in the format YYYY-MM-DD HH:MM:SS
    '''
    temperature = round(random.uniform(5, 45), 1)
    pressure = round(random.uniform(980, 1050), 1)
    humidity = random.randint(20, 90)
    aqi = random.randint(0, 500)
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Return as a dictionary
    return {
        "city": city,
        "temperature": temperature,
        "pressure": pressure,
        "humidity": humidity,
        "AQI": aqi,
        "datetime": current_datetime
    }

# Generate data for each city and store in a list
weather_data = []
for city in cities:
    data = generate_random_weather_data(city)
    weather_data.append(data)

# # Print the result as a JSON
# print(json.dumps(weather_data, indent=4))

# Define the output JSON file path
output_file = "weatherData.json"

# Write the data to a JSON file

with open(output_file, 'w') as json_file:
    json.dump(weather_data, json_file, indent=4)

print(f"Weather data has been successfully saved to {output_file}")