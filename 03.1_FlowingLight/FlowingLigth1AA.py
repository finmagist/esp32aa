import time
from machine import Pin

cDelay = 75 #задержка

pins=[15,2,0,4,5,18,19,21,22,23]
#Заполняем справа-налево
def fill(to):
    length=len(pins)
    for i in range(0,to):
        led=Pin(pins[i],Pin.OUT)
        led.value(1)
        time.sleep_ms(cDelay)
#Чистим справа-налево       
def clear(to):
    length=len(pins)
    for i in range(0,to):
        led=Pin(pins[i],Pin.OUT)
        led.value(0)
        time.sleep_ms(cDelay)    
       
  
        
def showled():
    for i in range(11):
        fill(i)    
        clear(i)
  
    
clear(10)
while True:
    showled()