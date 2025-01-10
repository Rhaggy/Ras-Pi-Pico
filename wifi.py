import network
from time import sleep

wifi = network.WLAN(network.STA_IF)
wifi.active(True)

ssid = 'iPhone_12_Pro'
password = 'g8xw341m80m3q'

wifi.connect(ssid, password)

print('Försöker ansluta till WiFi...')
while not wifi.isconnected():
    sleep(1)

print('Ansluten till WiFi!')
print('IP-adress:', wifi.ifconfig()[0])
