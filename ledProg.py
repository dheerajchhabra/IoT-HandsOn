import RPi.GPIO as GPIO
import time as t

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2, GPIO.OUT, initial=GPIO.LOW) #Set Pin2 to Low initialy

numbers = [1, 2, 3, 4, 5]
#number = 1

#While Loop
#while number in numbers: 

#For Loop
for number in numbers: 
    print("LED On")
    GPIO.output(2, GPIO.HIGH)
    t.sleep(1)
    print("LED Off")
    GPIO.output(2, GPIO.LOW)
    t.sleep(1)
number +=1