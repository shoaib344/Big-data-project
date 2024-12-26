import paho.mqtt.client as mqtt
import time

# MQTT broker settings
broker_address = "your_broker_address"
broker_port = 1883
topic = "vehicle_tracking_system/maintenance_alert"

# Callback function for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

# Callback function for when a message is published.
def on_publish(client, userdata, mid):
    print("Message published")

# Create a MQTT client instance
client = mqtt.Client()

# Set callback functions
client.on_connect = on_connect
client.on_publish = on_publish

# Connect to the broker
client.connect(broker_address, broker_port, 60)

# Start the loop
client.loop_start()

# Simulate vehicle data
vehicle_data = {
    "fuel_level": 20,  # Example fuel level in percentage
    "speed": 80  # Example speed in km/h
}

# Publish maintenance alerts
while True:
    if vehicle_data["fuel_level"] < 10:
        client.publish(topic, "Fuel alert: Low fuel level detected")
    if vehicle_data["speed"] > 120:
        client.publish(topic, "Speed alert: Exceeding maximum speed limit")

    # Simulate delay
    time.sleep(5)  # Adjust delay as needed

# Stop the loop
client.loop_stop()
client.disconnect()