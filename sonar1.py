import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIG = 14
ECHO = 15
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG, False)
print ('Initialising')
time.sleep(2)
GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)
while GPIO.input(ECHO)==0:
 pulse_start = time.time()
while GPIO.input(ECHO)==1:
 pulse_end = time.time()
pulse_duration = pulse_end - pulse_start
distance = pulse_duration * 17165
distance = (round(distance, 1))/100
print ('Distance:',distance,'m')
GPIO.cleanup()
