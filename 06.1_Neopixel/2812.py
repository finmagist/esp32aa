from machine import Pin
import neopixel
import time
pin = Pin(21, Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

#brightness :0-255
brightness=255                                
colors=[
        [0,0,brightness],                    #blue
        [0,brightness,0],                    #green
        [0,brightness,brightness],           #
        [brightness,0,0],                    #red
        [brightness,0,brightness],           #
        [brightness,brightness,0],           #             
        [brightness,brightness,brightness]   #white        
       ]                                     #close
    
while True:
    for i in range(0,7):
        for j in range(0,1):
            np[j]=colors[i]
            np.write()
            time.sleep_ms(50)
        time.sleep_ms(500)
    time.sleep_ms(500)
    
    