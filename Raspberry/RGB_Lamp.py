from machine import Pin, PWM
from time import sleep

red = PWM(Pin(4))
green = PWM(Pin(5))
blue = PWM(Pin(6))

red.freq(1000)
green.freq(1000)
blue.freq(1000)

def set_coulor(r,g,b):
    red.duty_u16(r*257)  
    green.duty_u16(g*257)  
    blue.duty_u16(b*257)   

while True:
    r = 200
    g = 0
    b = 0
    set_coulor(r,g,b)

