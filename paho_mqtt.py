from paho.mqtt import client as mqtt_client
import logging
import time

# 指定服务器（MQTT代理地址）此处是腾讯购买的服务器地址
# 服务器启动了EMQX服务
broker = 'mqtt://101.43.132.163/'  
port = 1883
topic = "on"
client_id = "python_king"

# username:admin
# password:kingipr1314

"""
    Next, we need to write the on_connect callback function for connecting the broker. 
    This function is called after the client has successfully connected,
    and we can check the connection status using the rc parameter. Typically, 
    we'll also create a client object that connects to broker.emqx.io at the same time.
    
"""

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

FIRST_RECONNECT_DELAY = 1
RECONNECT_RATE = 2
MAX_RECONNECT_COUNT = 12
MAX_RECONNECT_DELAY = 60

def on_disconnect(client, userdata, rc):
    logging.info("Disconnected with result code: %s", rc)
    reconnect_count, reconnect_delay = 0, FIRST_RECONNECT_DELAY
    while reconnect_count < MAX_RECONNECT_COUNT:
        logging.info("Reconnecting in %d seconds...", reconnect_delay)
        time.sleep(reconnect_delay)

        try:
            client.reconnect()
            logging.info("Reconnected successfully!")
            return
        except Exception as err:
            logging.error("%s. Reconnect failed. Retrying...", err)

        reconnect_delay *= RECONNECT_RATE
        reconnect_delay = min(reconnect_delay, MAX_RECONNECT_DELAY)
        reconnect_count += 1
    logging.info("Reconnect failed after %s attempts. Exiting...", reconnect_count)


client.on_disconnect = on_disconnect
