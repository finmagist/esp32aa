from machine import Pin
import neopixel
import time
PIN_LED = 48
pin = Pin(PIN_LED, Pin.OUT)
np = neopixel.NeoPixel(pin, 1)
delayblink = 25
#brightness :0-255
brightness=255                                
colors=[
        [0,0,brightness],                    #blue
        [0,brightness,0],                    #green
        [0,brightness,brightness],           #
        [brightness,0,0],                    #red
        [brightness,0,brightness],           #
        [brightness,brightness,0],           #             
        [brightness,brightness,brightness],  #white
        [0,0,0]
       ]                                     #close
def flash(j,i):
    np[j]=colors[i]
    np.write()
    time.sleep_ms(delayblink)
    np[j]=colors[7]            
    np.write()
    time.sleep_ms(delayblink)
    
while True:
    for i in range(0,7):
        for j in range(0,1):
            flash(j,i)
            flash(j,i)
            flash(j,i)                
        time.sleep_ms(500)
    time.sleep_ms(50)