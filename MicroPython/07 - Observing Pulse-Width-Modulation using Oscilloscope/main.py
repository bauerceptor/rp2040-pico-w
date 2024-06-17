from machine import PWM, Pin
from time import sleep

out_pin = 16
analog_out = PWM(Pin(out_pin))
analog_out.freq(1000)

analog_out.duty_u16(0)

while True:
    my_voltage = float(input("What voltage would you like to observe: "))
    pwm_value = (65535 / 3.3) * my_voltage
    analog_out.duty_u16(int(pwm_value))
    sleep(.1)
