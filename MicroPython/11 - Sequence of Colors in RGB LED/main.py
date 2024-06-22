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


print("There are a total of 10 colors, which are:\n-Red (r)\t\t-Green (g)\n-Blue (b)\t\t-Cyan (c)\n-Magenta (m)\t\t-Yellow (y)\n-Sea Green (s)\t\t-Violet (v)\n-Orange (o)\t\t-White (w)")
colors = []
num_colors = int(input("\nHow many colors are in your sequence: "))

for i in range(num_colors):
    user_color = input("Enter a color: ").lower()
    colors.append(user_color)


while True:
    for color in colors:
        if color == 'red':
            r_bright = 65535
            g_bright = 0
            b_bright = 0
        elif color == 'green':
            r_bright = 0
            g_bright = 65535
            b_bright = 0
        elif color == 'blue':
            r_bright = 0
            g_bright = 0
            b_bright = 65535
        elif color == 'cyan':
            r_bright = 0
            g_bright = 65535
            b_bright = 65535
        elif color == 'magenta':
            r_bright = 65535
            g_bright = 0
            b_bright = 65535
        elif color == 'yellow':
            r_bright = 65535
            g_bright = 65535
            b_bright = 0
        elif color == 'sea green':
            r_bright = 10000
            g_bright = 65535
            b_bright = 0
        elif color == 'violet':
            r_bright = 10000
            g_bright = 0
            b_bright = 65535
        elif color == 'orange':
            r_bright = 65535
            g_bright = 10000
            b_bright = 0
        elif color == 'white':
            r_bright = 65535
            g_bright = 65535
            b_bright = 65535
    
        r_led.duty_u16(r_bright)
        g_led.duty_u16(g_bright)
        b_led.duty_u16(b_bright)
        sleep(2)
