from machine import Pin, PWM
from time import sleep


# GPIO pins for each color of RGB LED
red_pin = 13
green_pin = 14
blue_pin = 15


# Setting up LED control through PWM
r_led = PWM(Pin(red_pin))
g_led = PWM(Pin(green_pin))
b_led = PWM(Pin(blue_pin))


# Configuring the frequency and duty-cycle for each color of LED
r_led.freq(1000)
r_led.duty_u16(0)

g_led.freq(1000)
g_led.duty_u16(0)

b_led.freq(1000)
b_led.duty_u16(0)

while True:
    # toggle between 65535 and 0 for these values
    # the color with 65535 value will turn active
    # and the color with 0 value will stay off
    r_bright = 0
    g_bright = 0
    b_bright = 65535
    
    r_led.duty_u16(r_bright)
    g_led.duty_u16(g_bright)
    b_led.duty_u16(b_bright)
    sleep(.1)
