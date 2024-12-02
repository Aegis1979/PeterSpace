import RPi.GPIO as GPIO
import time

# Set up the GPIO pins
TRIG = 23  # GPIO pin for the trigger
ECHO = 24  # GPIO pin for the echo

# Set up the GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    # Send a short pulse to trigger the sensor
    GPIO.output(TRIG, GPIO.LOW)  # Ensure the trigger is low
    time.sleep(0.5)  # Wait for the sensor to settle

    GPIO.output(TRIG, GPIO.HIGH)  # Send the pulse to trigger
    time.sleep(0.00001)  # Wait for 10 microseconds
    GPIO.output(TRIG, GPIO.LOW)  # Stop the pulse

    # Measure the time taken for the echo to return
    while GPIO.input(ECHO) == GPIO.LOW:
        pulse_start = time.time()  # Start time of pulse

    while GPIO.input(ECHO) == GPIO.HIGH:
        pulse_end = time.time()  # End time of pulse

    # Calculate the distance
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Speed of sound is ~34300 cm/s, so 34300/2 = 17150 cm/s
    distance = round(distance, 2)  # Round to 2 decimal places

    return distance

def main():
    try:
        while True:
            distance = get_distance()
            print(f"Distance: {distance} cm")
            time.sleep(1)  # Delay between measurements

    except KeyboardInterrupt:
        print("Measurement stopped by user")
        GPIO.cleanup()  # Clean up the GPIO settings on exit

if __name__ == "__main__":
    main()
