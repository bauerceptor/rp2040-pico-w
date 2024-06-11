from machine import Pin, ADC
from time import sleep

pot_pin = 28							# GPIO pin 28 for ADC on the Pico
my_pot = ADC(pot_pin)					# connection for potentiometer

green_led = 3							# GPIO pin 3 for green LED on the Pico
my_green = Pin(green_led, Pin.OUT)

yellow_led = 9							# GPIO pin 9 for yellow LED on the Pico
my_yellow = Pin(yellow_led, Pin.OUT)

red_led = 15							# GPIO pin 15 for red LED on the Pico
my_red = Pin(red_led, Pin.OUT)

while True:
    pot_value = my_pot.read_u16()
    voltage = ((100 / 65103) * pot_val) - ((100 / 65103) * 432)			# calculation present in README
    sleep(.1)
    
    if voltage < 80:
        my_green.value(1)
        my_yellow.value(0)
        my_red.value(0)
    elif 80 <= voltage < 95:
        my_green.value(0)
        my_yellow.value(1)
        my_red.value(0)
    else:
        my_green.value(0)
        my_yellow.value(0)
        my_red.value(1)
