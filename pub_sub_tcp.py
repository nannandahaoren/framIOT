# python 3.6

import json
import logging
import random
import time
from paho.mqtt import client as mqtt_client

broker = '101.43.132.163'
port = 1883
topic = "on"
# generate client ID with pub prefix randomly
client_id = "python_king"
username = 'lina'
password = 'lina1314'

first_reconnect_delay = 1
reconnect_rate = 2
max_reconnect_count = 12
max_reconnect_delay = 60

flag_exit = False

# 应该传入client 和 rc
def on_connect(client, userdata, flags, rc):
    if rc == 0 and client.is_connected():
        print("Connected to MQTT Broker!")
        client.subscribe(topic)
    else:
        print(f'Failed to connect, return code {rc}')


def on_disconnect(client, userdata, rc):
    logging.info("Disconnected with result code: %s", rc)
    reconnect_count, reconnect_delay = 0, first_reconnect_delay
    while reconnect_count < max_reconnect_count:
        logging.info("Reconnecting in %d seconds...", reconnect_delay)
        time.sleep(reconnect_delay)

        try:
            client.reconnect()
            logging.info("Reconnected successfully!")
            return
        except Exception as err:
            logging.error("%s. Reconnect failed. Retrying...", err)

        reconnect_delay *= reconnect_rate
        reconnect_delay = min(reconnect_delay, max_reconnect_delay)
        reconnect_count += 1
    logging.info("Reconnect failed after %s attempts. Exiting...", reconnect_count)
    global flag_exit
    flag_exit = True


def on_message(client, userdata, msg):
    print(f'Received `{msg.payload.decode()}` from `{msg.topic}` topic')


def connect_mqtt():
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port, keepalive=60)
    client.on_disconnect = on_disconnect
    return client


def publish(client):
    msg_count = 0
    while not flag_exit:
        msg_dict = {
            'msg': msg_count
        }
        msg = json.dumps(msg_dict)
        if not client.is_connected():
            logging.error("publish: MQTT client is not connected!")
            time.sleep(1)
            continue
        result = client.publish(topic,msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f'Send `{msg}` to topic `{topic}`')
        else:
            print(f'Failed to send message to topic {topic}')
        msg_count += 1
        time.sleep(1)


def run():
    logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s',level=logging.DEBUG)
    client = connect_mqtt()
    client.loop_start()
    time.sleep(1)
    if client.is_connected():
        publish(client)
    else:
        client.loop_stop()


if __name__ == '__main__':
    run()