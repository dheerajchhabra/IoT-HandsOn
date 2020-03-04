import paho.mqtt.publish as publish
 
MQTT_SERVER = "192.168.1.101"
MQTT_PATH = "Team_1_Channel"
 
publish.single(MQTT_PATH, "Hello World!", hostname=MQTT_SERVER)