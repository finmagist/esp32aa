from machine import Pin, SoftI2C
import time
import ssd1306
#from time import sleep


# ESP32 Pin assignment 
trigPin=Pin(13,Pin.OUT,0)
echoPin=Pin(14,Pin.IN,0)

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

# ESP8266 Pin assignment
#i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

soundVelocity=340
distance=0

def getSonar():
    trigPin.value(1)
    time.sleep_us(10)
    trigPin.value(0)
    while not echoPin.value():
        pass
    pingStart=time.ticks_us()
    while echoPin.value():
        pass
    pingStop=time.ticks_us()
    pingTime=time.ticks_diff(pingStop,pingStart)
    distance=pingTime*soundVelocity//2//10000
    urn int(distance)

time.sleep_ms(1000)
#distance2=getSonar()
while True:
    time.sleep_ms(500)
 #   if  distance2!=getSonar():
 #      distance2=getSonar()
    oled.fill(0)
    oled.text("Distance: "+str(getSonar()) +" cm",0,0)
    oled.show()
#    time.sleep_ms(5)
#    print('Distance: ',getSonar(),'cm' )
    