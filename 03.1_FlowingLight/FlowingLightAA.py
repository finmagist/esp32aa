import time
from machine import Pin

cDelay = 25 #задержка

pins=[15,2,0,4,5,18,19,21,22,23]
#Заполняем справа-налево
def fill():
    length=len(pins)
    for i in range(0,length):
        led=Pin(pins[i],Pin.OUT)
        led.value(1)
        time.sleep_ms(cDelay)
#Чистим справа-налево       
def clear():
    length=len(pins)
    for i in range(0,length):
        led=Pin(pins[i],Pin.OUT)
        led.value(0)
        time.sleep_ms(cDelay)    
#Бежим 1-8
def runLR():
    length=len(pins)               
    for i in range(0,length):
        led=Pin(pins[i],Pin.OUT)
        led.value(1)
        time.sleep_ms(cDelay)
        led.value(0)
#Бежим 8-1
def runRL():
    length=len(pins)               
    for i in range(0,length):
        led=Pin(pins[(length-i-1)],Pin.OUT)
        led.value(1)
        time.sleep_ms(cDelay)
        led.value(0)
        
        
        
def showled():
      
#    runLR()
#    runLR()
#    runRL()
#    runRL()

    fill()    
    clear()
    fill()    
    clear()
    
    
clear()
while True:
    showled()