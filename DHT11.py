from machine import Pin
from time import sleep 
from dht import DHT11 
from machine import Pin, PWM
from simple import MQTTClient
import network

ssid = 'iPhone_12_Pro'
password = 'g8xw341m80m3q'

wifi = network.WLAN(network.STA_IF)
wifi.active(True)

wifi.connect(ssid, password)

print('Försöker ansluta till WiFi...')
while not wifi.isconnected():
    sleep(1)

print('Ansluten till WiFi!')
print('IP-adress:', wifi.ifconfig()[0])

ADAFRUIT_AIO_USERNAME = "Rhaggy_"
ADAFRUIT_AIO_KEY   = "ja"
ADAFRUIT_IO_FEED = "Rhaggy_/feeds/temperature"

def send_data(temp):
    client = MQTTClient("umqtt_client", "io.adafruit.com", user = ADAFRUIT_AIO_USERNAME, password = ADAFRUIT_AIO_KEY)
    client.connect()
    print("Ansluten till Adafruit IO")
    #publicera  
    client.publish(ADAFRUIT_IO_FEED, str(temp))
    print(f"Tempratur {temp} sickad till {ADAFRUIT_IO_FEED}")

sensor = DHT11(Pin(28))

while True:
    try:
    
        sleep(1)
        sensor.measure()
        temp = sensor.temperature()
        humidity = sensor.humidity()
        print(f"Temp:{temp} C, Humidity:{humidity}%")
        send_data(temp)
        sleep(60)
    except Exception as e:
        print("Errr reading from DHT11:", e)
