#Create a Python script 
# that generates fake temperature readings like a sensor would.

import random
from datetime import datetime

def gen_temp():
    temp = round(random.uniform(20.0, 35.0))  # Generate a random temperature between 20.0 and 35.0
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Get the current timestamp
    return f"{timestamp} - Temperature: {temp}°C"


for i in range(10):
    print(gen_temp())


# This script generates 10 fake temperature readings with timestamps.

# How to save readings to a text file in same folder:

with open("temperature_readings.txt", "w") as file:
    for i in range(10):
        file.write(gen_temp() + "\n")

# This will create a file named 'temperature_readings.txt' with the generated readings.

# Now we will calculate the average temperature from the generated readings:

def calculate_average_temperature(filename):
    with open(filename, "r") as file:
        temperatures = []
        for line in file:
            temp_str = line.split(" - Temperature: ")[1].replace("°C", "")
            temperatures.append(float(temp_str))
    average_temp = sum(temperatures) / len(temperatures)
    return round(average_temp, 2)
average_temperature = calculate_average_temperature("temperature_readings.txt")
print(f"Average Temperature: {average_temperature}°C")

# This will read the temperatures from the file and calculate the average temperature.

