import time
import board
import adafruit_dht

# Initialize the DHT device, with data pin connected to:
# - GPIO 4 (as per [1] and [4])
# - GPIO 17 (as per [5], alternative)
dht_device = adafruit_dht.DHT11(board.D4)  # Use board.D17 for GPIO 17

while True:
    try:
        # Print the values to the serial port
        temperature_c = dht_device.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dht_device.humidity

        print("Temperature: {:.2f}°C / {:.2f}°F".format(temperature_c, temperature_f))
        print("Humidity: {:.2f}%".format(humidity))

    except Exception as e:
        print("Error: {}".format(e))

    time.sleep(1)  # Wait 1 second before taking the next reading