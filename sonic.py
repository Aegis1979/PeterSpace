#Raspberry Pi 4.0 code for interfacing with ultrasonic sensor

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG_PIN=11
ECHO_PIN=12

GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.output(TRIG_PIN, GPIO.LOW)

time.sleep(2)

GPIO.output(TRIG_PIN,GPIO.HIGH)

time.sleep(0.00001)
GPIO.output(TRIG_PIN, GPIO.LOW)

while GPIO.input(ECHO_PIN)==0:
  pulse_send=time.time()

while GPIO.input(ECHO_PIN)==1:
  pulse_received=time.time()

pulse_duration= pulse_received- pulse_send

pulse_duration= round(pulse_duration/2)

distance=34000*pulse_duration

print('Distance to object:',distance)
GPIO.cleanup()
