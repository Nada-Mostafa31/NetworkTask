import paho.mqtt.client as mqtt
import ssl
import time
import random


MQTT_BROKER = "a2300e158dee4f46bfbdb78f22083476.s1.eu.hivemq.cloud"
MQTT_PORT = 8883
MQTT_TOPIC = "NetworkTask/NadaMostafa"
MQTT_USERNAME = "NADA31"
MQTT_PASSWORD = "Sic1122004"


def publisher():
    client = mqtt.Client()
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
    client.tls_set(tls_version=ssl.PROTOCOL_TLS)  
    client.connect(MQTT_BROKER, MQTT_PORT, 60)

    while True:
        temp = random.randint(20, 35)  
        client.publish(MQTT_TOPIC, temp)
        print(f"Published: {temp} °C")
        time.sleep(2)


def subscriber():
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code", rc)
        client.subscribe(MQTT_TOPIC)

    def on_message(client, userdata, msg):
        print(f"Received: {msg.payload.decode()} °C")

    client = mqtt.Client()
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
    client.tls_set(tls_version=ssl.PROTOCOL_TLS)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_forever()
