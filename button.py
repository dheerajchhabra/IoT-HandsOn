import RPi.GPIO as GPIO
from time import sleep as s

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

#While Loop
while True: 
    if GPIO.input(18) == GPIO.HIGH:
        print("Button Switched On")
        #GPIO.input(2, GPIO.LOW)
        s(1)
    elif GPIO.input(18) == GPIO.LOW:
        print("Button Switched Off")
        #GPIO.input(2, GPIO.HIGH)
        s(1)
    else:
        print("Error in Button")
