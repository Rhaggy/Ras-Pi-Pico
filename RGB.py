from machine import Pin, PWM
from time import sleep
import random

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

while True:
    for i in range(10):
        set_coulor(255,0,0)
    