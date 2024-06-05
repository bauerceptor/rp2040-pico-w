from machine import Pin
from time import sleep

led = Pin(15, Pin.OUT)                # using GPIO pin 15 for output to the LED

while True:
    led.value(0)                      # individually turning the LED off instead of toggling
    sleep(.3)
    led.value(1)                      # individually turning the LED on instead of toggling
    sleep(.6)
