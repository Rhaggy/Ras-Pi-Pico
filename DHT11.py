from machine import Pin
from time import sleep 
from dht import DHT11 
from machine import Pin, PWM


red = PWM(Pin(21))
green = PWM(Pin(20))
blue = PWM(Pin(19))

red.freq(1000)
green.freq(1000)
blue.freq(1000)

def set_coulor(r,g,b):
    red.duty_u16(r*257)  
    green.duty_u16(g*257)  
    blue.duty_u16(b*257) 

sensor = DHT11(Pin(28))

while True:
    try:
    
        sleep(1)
        sensor.measure()
        temp = sensor.temperature()
        
        humidity = sensor.humidity()
        print(f"Temp:{temp} C, Humidity:{humidity}%")
    except Exception as e:
        print("Errr reading from DHT11:", e)
    if temp >= 20:
        while True:
            r = 0
            g = 255
            b = 0
    
            set_coulor(r,g,b)
    continue
        

    