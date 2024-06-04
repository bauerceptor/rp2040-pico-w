from machine import Pin
from time import sleep

main_led = Pin('LED', Pin.OUT)        # targets the LED on the Pico W

while True:
    main_led.toggle()                 # automatically toggles the LED on/off
    sleep(.3)
