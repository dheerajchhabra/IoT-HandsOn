import RPi.GPIO as GPIO

def button_release(channel):
    print("Button Released")

def button_press(channel):
    print("Button Pressed")
    

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

GPIO.add_event_detect(18, GPIO.RISING, callback=button_press) # Rising event
#GPIO.add_event_detect(18, GPIO.FALLING, callback=button_release) # Falling event

message=input("Quit Now... Testing Complete\n\n")
GPIO.cleanup() #clean up