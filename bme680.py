# Dependancy: sudo pip3 install adafruit-circuitpython-bme680

import time
import board
import busio
import adafruit_bme680

# Create I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize the BME680 sensor
sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c)

# Function to read data from BME680
def read_sensor():
    if sensor.begin():
        # Wait for the sensor to be ready
        print("Sensor initialized successfully!")
        while True:
            # Retrieve the sensor readings
            temperature = sensor.temperature
            humidity = sensor.humidity
            pressure = sensor.pressure
            gas = sensor.gas

            # Print the readings
            print(f"Temperature: {temperature:.2f} °C")
            print(f"Humidity: {humidity:.2f} %")
            print(f"Pressure: {pressure:.2f} hPa")
            print(f"Gas Resistance: {gas} ohms")
            print("-" * 40)

            time.sleep(2)  # Wait for 2 seconds before the next reading
    else:
        print("Failed to initialize sensor. Check your connections.")

# Main function
def main():
    try:
        read_sensor()
    except KeyboardInterrupt:
        print("Program interrupted by user.")
        pass

if __name__ == "__main__":
    main()
