import paho.mqtt.client as mqtt
import sys


host = 'localcost'
port = 1883

sender = sys.argv[1]
receiver = sys.argv[2]


def on_message(client, userdata, message):
        print("\b\b\b=============msg============")
        print(message.topic, " : ", message.payload.decode("utf-8"))
        print("============================")
        print(">>>", end=" ", flush=True)

client = mqtt.Client(sender)
client.username_pw_set(sender, password=sender)
client.connect(host, port)
client.on_message = on_message
client.subscribe(receiver)
client.loop_start()

while True:
    line = input('>>>')
    if line == 'endchat':
        break
    result = client.publish(sender, line, qos=0, retain=False)
client.loop_stop() 





