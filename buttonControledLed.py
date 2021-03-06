import RPi.GPIO as GPIO

led_State = GPIO.LOW

def button_release(channel1, channel2):
    if (GPIO.input(18) and led_State == GPIO.LOW):
        #print("Led On")
        GPIO.output(23, GPIO.HIGH)
        led_State = GPIO.HIGH
    elif (GPIO.input(18) and led_State == GPIO.HIGH):
        #print("Led Off")
        GPIO.output(23, GPIO.HIGH)
        led_State = GPIO.HIGH
    elif (NOT GPIO.input(18) and led_State == GPIO.HIGH):
        #print("Led On")
        GPIO.output(23, GPIO.LOW)
        led_State = GPIO.LOW
    elif (NOT GPIO.input(18) and led_State == GPIO.LOW):
        #print("Led Off")
        GPIO.output(23, GPIO.LOW)
        led_State = GPIO.LOW
    

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)

#GPIO.add_event_detect(18, GPIO.RISING, callback=button_press) # Rising event
#GPIO.add_event_detect(18, GPIO.FALLING, callback=button_release) # Falling event
GPIO.add_event_detect(18, GPIO.BOTH, callback=button_release) # Both RISING and FALLNG event

message=input("Quit Now... Testing Complete\n\n")
GPIO.cleanup() #clean up
