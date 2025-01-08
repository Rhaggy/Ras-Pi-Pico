from machine import Pin
from time import sleep 
from dht import DHT11 





sensor = DHT11(Pin(28))

while True:
    try:
    
     
        sensor.measure()
        temp = sensor.temperature()
        humidity = sensor.humidity()
        sleep(300)
        print(f"Temp:{temp} C, Humidity:{humidity}%")
        
    except Exception as e:
        print("Errr reading from DHT11:", e)