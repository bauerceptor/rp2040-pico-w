##  the project focuses on using an analog-to-digital converter pin on the Pico
##  to read analog signals and then convert them to digital info/signal through the Pico
##  the digital output value will be displayed by this code when it is executed on the Pico setup

from machine import ADC
from time import sleep


##  this time, i am using variables to store GPIO pin number on the Pico's pin layout
##  refer to the Pico W pin schematics for more information

adc_pin = 28						                  # analog-to-digital pin which is GPIO pin 28, on the Pico

potentiometer = ADC(adc_pin)		          # a potentiometer object initialized to read from the actual potentiometer 
									                        # connected to the GPIO pin 28 of the Pico via the "adc_pin" variable
									
while True:
	pot_value = potentiometer.read_u16()		# reads input data from physical potentiometer in binary format and 
												                  # then converts it to unsigned 16-bit integer values
	
	# the calculation below converts the bit reading on a scale of 0 to 65,536
	# to a user-friendly voltage reading from 0 to 3.3
	# the 3.3 voltage is selected because Pico gives out 3.3v at physical pin 36
	voltage = ((3.3 / 65106) * pot_value) - ((430 * 3.3) / 65106)
	
	print(voltage)					                # the output could be a little distored instead of clean 0 to 3.3 
									                        # because of differences in the binary to digital volatage conversion above
	sleep(.2)
