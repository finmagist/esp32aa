import time
from machine import Pin

cDelay = 143 #задержка

#pins=[15,2,0,4,5,18,19,21,22,23]
pins=[15,2,16,4,5,18,19,21,22,23]



ledsoff = [0,0,0,0,0,0,0,0,0,0]

#matrix = [1,1,1,1,1,0,0,1,0,0]


matrix = [1,1,1,1,0,0,0,0,0,0]
       
def clearall():
    length=len(pins)
    for i in range(0,length):
        led=Pin(pins[i],Pin.OUT)
        led.value(ledsoff[i])
        
def showmatrix():
    length=len(pins)
    for i in range(0,length):
        led=Pin(pins[i],Pin.OUT)
        led.value(matrix[i])        
    time.sleep_ms(cDelay)
    
    
def movematrixrigth():
    length=len(matrix)    
    last = matrix [length-1]   
    for i in range(length-1,0,-1):
         matrix[i] = matrix[i-1]         
    matrix[0] = last

def movematrixleft():
    length=len(matrix)    
    first = matrix [0]   
    for i in range(0, length-1):
         matrix[i] = matrix[i+1]         
    matrix[length-1] = first
    
def showled():
     for i in range (0,48):
        showmatrix()
        movematrixrigth()
     for i in range (0,48):   
        showmatrix()
        movematrixleft()

def showled1():
     for i in range (0,7):
        showmatrix()
        movematrixrigth()
     for i in range (0,7):   
        showmatrix()
        movematrixleft()


clearall()

while True:
    showled1()