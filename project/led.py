from machine import Pin
import time
led=Pin(2,Pin.OUT)
led.value(1)


while True:
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)



