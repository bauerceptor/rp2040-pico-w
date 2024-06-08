from machine import Pin
from time import sleep


##  the LEDs are in numbered in reverse order than Pico pins
##  because binary is interpreted right-to-left

led1 = Pin(15, Pin.OUT)
led2 = Pin(14, Pin.OUT)
led3 = Pin(13, Pin.OUT)
led4 = Pin(12, Pin.OUT)


while True:
	# displays 0 on the LED in bit-pattern
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    sleep(.5)
    
    # displays 1 on the LED in bit-pattern
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(1)
    sleep(.5)
    
    # displays 2 on the LED in bit-pattern
    led1.value(0)
    led2.value(0)
    led3.value(1)
    led4.value(0)
    sleep(.5)
    
    # displays 3 on the LED in bit-pattern
    led1.value(0)
    led2.value(0)
    led3.value(1)
    led4.value(1)
    sleep(.5)
    
    # displays 4 on the LED in bit-pattern
    led1.value(0)
    led2.value(1)
    led3.value(0)
    led4.value(0)
    sleep(.5)
    
    # displays 5 on the LED in bit-pattern
    led1.value(0)
    led2.value(1)
    led3.value(0)
    led4.value(1)
    sleep(.5)
    
    # displays 6 on the LED in bit-pattern
    led1.value(0)
    led2.value(1)
    led3.value(1)
    led4.value(0)
    sleep(.5)
    
    # displays 7 on the LED in bit-pattern
    led1.value(0)
    led2.value(1)
    led3.value(1)
    led4.value(1)
    sleep(.5)
    
    # displays 8 on the LED in bit-pattern
    led1.value(1)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    sleep(.5)
    
    # displays 9 on the LED in bit-pattern
    led1.value(1)
    led2.value(0)
    led3.value(0)
    led4.value(1)
    sleep(.5)
    
    # displays 10 on the LED in bit-pattern
    led1.value(1)
    led2.value(0)
    led3.value(1)
    led4.value(0)
    sleep(.5)
    
    # displays 11 on the LED in bit-pattern
    led1.value(1)
    led2.value(0)
    led3.value(1)
    led4.value(1)
    sleep(.5)
    
    # displays 12 on the LED in bit-pattern
    led1.value(1)
    led2.value(1)
    led3.value(0)
    led4.value(0)
    sleep(.5)
    
    # displays 13 on the LED in bit-pattern
    led1.value(1)
    led2.value(1)
    led3.value(0)
    led4.value(1)
    sleep(.5)
    
    # displays 14 on the LED in bit-pattern
    led1.value(1)
    led2.value(1)
    led3.value(1)
    led4.value(0)
    sleep(.5)
    
    # displays 15 on the LED in bit-pattern
    led1.value(1)
    led2.value(1)
    led3.value(1)
    led4.value(1)
    sleep(.5)
