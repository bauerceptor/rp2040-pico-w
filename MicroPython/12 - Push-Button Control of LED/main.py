from machine import Pin
from time import sleep


# GPIO pin for the button and LED
button_pin = 14
led_pin = 15

# Setting up the button and LED with the Pico W
button = Pin(button_pin, Pin.IN, Pin.PULL_UP)
led = Pin(led_pin, Pin.OUT)

btn_state_old = 0
led_state = False

while True:
    btn_state_new = button.value()   # Get button state (0 or 1)
    
    # Toggle LED state when button is pressed and released (basically the LED toggles when the button is released)
    if btn_state_new == 1 and btn_state_old == 0:
    # condition below turn the LED on when the button goes down during the press
    #if btn_state_new == 0 and btn_state_old == 1:
        led_state = not led_state
        led.value(led_state)
    btn_state_old = btn_state_new
    sleep(.5)
