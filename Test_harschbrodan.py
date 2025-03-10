from machine import Pin
import time

lysdiod1 = Pin(26, Pin.OUT)

while True:
        lysdiod1.value(1)
        time.sleep(1)
        lysdiod1.value(0)
        time.sleep(1)
        print("1")
