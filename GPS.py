# Dependancy: 
# sudo apt-get update
# sudo apt-get install python3-serial
# sudo pip3 install adafruit-circuitpython-gps
# Ensure that UART is enabled on the Raspberry Pi via the raspi-config tool.

import time
import serial
import adafruit_gps

# Set up the serial connection to the GPS module
# Assuming the GPS HAT is connected to /dev/serial0 (default serial port)
uart = serial.Serial('/dev/serial0', baudrate=9600, timeout=10)

# Create the GPS instance
gps = adafruit_gps.GPS(uart)

# Set the GPS to read data (you can configure it to output specific data)
gps.update()

def get_gps_data():
    while True:
        # Update the GPS object with the latest data
        gps.update()

        # If the GPS data is available
        if gps.has_fix:
            # Get the latitude, longitude, and other details
            latitude = gps.latitude
            longitude = gps.longitude
            print(f"Latitude: {latitude}, Longitude: {longitude}")
        else:
            print("Waiting for GPS fix...")

        time.sleep(1)

if __name__ == "__main__":
    try:
        print("Starting GPS tracking...")
        get_gps_data()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")

#Run in terminal: python3 gps_coordinates.py
