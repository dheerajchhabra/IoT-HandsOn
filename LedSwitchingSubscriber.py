import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

#MQTT_SERVER = "192.168.1.102"
MQTT_SERVER = "broker.mqttdashboard.com"
MQTT_PORT = 8000
MQTT_TIMEOUT = 60
MQTT_PATH = "testtopic/1"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if str(msg.payload) == "b'LED ON'":
        GPIO.output(23, GPIO.HIGH)
    elif str(msg.payload) == "b'LED OFF'":
        GPIO.output(23, GPIO.LOW)
    else:
        print("Go to hell")
    
    #print(msg.topic+" "+str(msg.payload))
    # more callbacks, etc

# GPIO Initiation
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
#client.connect(MQTT_SERVER, 1883, 60)
client.connect(MQTT_SERVER, MQTT_PORT, MQTT_TIMEOUT)
 
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
