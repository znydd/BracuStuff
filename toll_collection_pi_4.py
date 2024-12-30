# sudo pigpiod

from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Device, AngularServo
import RPi.GPIO as GPIO
import time

#servo
Device.pin_factory = PiGPIOFactory()
servo = AngularServo(17, min_angle=0, max_angle=180, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000) # Here 17 is servo GPIO pin

#ultrasonic
TRIG = 3 # GPIO pin no 
ECHO = 5 # GPIO pin no

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)


def meaesure_dist():
    GPIO.output(TRIG, True)
    time.sleep(0.00001) #10 micro second
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    return round(distance, 2)

try:
    while True:
        distance = meaesure_dist()
        print(f"Distance: {distance} cm")

        if distance < 4:
            print("Openning Gate...")
            servo.angle = 90
            time.sleep(3)

            print("Closing Gate...")
            servo.angle = 0 #it can be 180 idk

        time.sleep(0.1)
except KeyboardInterrupt:
    print("Progrm Stopped")

finally:
    GPIO.cleanup()
