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
    choice = input("Enter the corresponding key for the color you want.\n-Red (r)\t\t-Green (g)\n-Blue (b)\t\t-Cyan (c)\n-Magenta (m)\t\t-Yellow (y)\n-Sea Green (s)\t\t-Violet (v)\n-Orange (o)\t\t-White (w)").lower()
    if choice == 'r':
        r_bright = 65535
        g_bright = 0
        b_bright = 0
    elif choice == 'g':
        r_bright = 0
        g_bright = 65535
        b_bright = 0
    elif choice == 'b':
        r_bright = 0
        g_bright = 0
        b_bright = 65535
    elif choice == 'c':
        r_bright = 0
        g_bright = 65535
        b_bright = 65535
    elif choice == 'm':
        r_bright = 65535
        g_bright = 0
        b_bright = 65535
    elif choice == 'y':
        r_bright = 65535
        g_bright = 65535
        b_bright = 0
    elif choice == 's':
        r_bright = 10000
        g_bright = 65535
        b_bright = 0
    elif choice == 'v':
        r_bright = 10000
        g_bright = 0
        b_bright = 65535
    elif choice == 'o':
        r_bright = 65535
        g_bright = 10000
        b_bright = 0
    elif choice == 'w':
        r_bright = 65535
        g_bright = 65535
        b_bright = 65535
    else:
        print ("Invalid choice! Select again.")
    
    r_led.duty_u16(r_bright)
    g_led.duty_u16(g_bright)
    b_led.duty_u16(b_bright)
    sleep(5)
