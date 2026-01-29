# Work with sensor data in JSON format (how AWS IoT Core receives data)

sensor_data = {
    "device_id": "ESP32_001",
    "location": "Zone_A",
    "timestamp": "2026-01-24T10:30:15",
    "temperature": 34.5,
    "humidity": 65.2,
    "status": "online"
}

print("Device ID:", sensor_data["temperature"])
print("Device ID:", sensor_data["device_id"])
print("Location:", sensor_data["location"])

if sensor_data["temperature"] > 30:
    print("Warning: High temperature detected!")

# Now we add new field to the data

sensor_data["battery_level"] = 78.5  # in percentage
print("Updated Sensor Data:", sensor_data)


# Finally, we will convert the updated sensor data to a JSON string

import json
sensor_data_json = json.dumps(sensor_data, indent=4)
print("Sensor Data in JSON format:")    
print(sensor_data_json)

# now we Create a list of 5 sensor readings

sensor_readings = [
    {
        "device_id": "ESP32_001",
        "timestamp": "2026-01-24T10:30:15",
        "temperature": 34.5,
        "humidity": 65.2
    },
    {
        "device_id": "ESP32_002",
        "timestamp": "2026-01-24T10:31:20",
        "temperature": 28.3,
        "humidity": 70.1
    },
    {
        "device_id": "ESP32_003",
        "timestamp": "2026-01-24T10:32:25",
        "temperature": 31.0,
        "humidity": 60.5
    },
    {
        "device_id": "ESP32_004",
        "timestamp": "2026-01-24T10:33:30",
        "temperature": 29.8,
        "humidity": 68.0
    },
    {
        "device_id": "ESP32_005",
        "timestamp": "2026-01-24T10:34:35",
        "temperature": 33.2,
        "humidity": 64.3
    }
]

for sensor_readings in sensor_readings:
    if sensor_readings["temperature"] > 30:
        new = (sensor_readings["temperature"])
        print(sensor_readings["temperature"])

# Save all readings to a JSON file
with open("sensor_readings.json", "w") as json_file:
    json.dump(sensor_readings, json_file, indent=4)
print("Sensor readings saved to 'sensor_readings.json'")
