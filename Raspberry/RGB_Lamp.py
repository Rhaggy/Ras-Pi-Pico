from machine import Pin, PWM
from time import sleep

red = PWM(Pin(2))
green = PWM(Pin(3))
blue = PWM(Pin(4))

red.freq(1000)
green.freq(1000)
blue.freq(1000)

def set_coulor(r,g,b):
    red.duty_u16(r*257)  
    green.duty_u16(g*257)  
    blue.duty_u16(b*257)   

while True:
    r = 0
    g = 255
    b = 0
    
    
    set_coulor(r,g,b)

