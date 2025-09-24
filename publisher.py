import paho.mqtt.client as mqtt
import time
import random
import ssl

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

if __name__ == "__main__":
    publisher()
