from machine import PWM, ADC, Pin
from time import sleep

pot_pin = 28                    # GPIO pin 28 for the potentiometer
red_led = 15                    # GPIO pin 15 for the red LED

my_pot = ADC(Pin(pot_pin))      # Connect ADC to potentiometer at GPIO pin 28
my_red_led = PWM(Pin(red_led))  # Connect PWM to red LED at GPIO 15

my_red_led.freq(1000)           # Set PWM frequency to 1000 Hz
my_red_led.duty_u16(0)          # Initialize LED brightness to 0

while True:
    pot_value = my_pot.read_u16()
    exponent_value = (16 / 65535) * pot_value
    brightness = 2 ** exponent_value
    my_red_led.duty_u16(int(brightness))
    sleep(0.1)
