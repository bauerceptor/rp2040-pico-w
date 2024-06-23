## Push-Button Control of LED with Pico W
This project demonstrates how to control an LED using a push-button with the Raspberry Pi Pico W. When the button is pressed, the LED toggles its state between on and off.


## Required Components
- Raspberry Pi Pico W
- Wires
- 220 ohm resistor (1)
- Push-button (1)


## Circuit Schematics
The image below explains pin configuration of a simple push-button. Note that pin 1 and 2 are always connected and same is with pin 3 and 4.
- [button.jpg](button.jpg)

The image below provides a detailed schematic of the actual setup.
- [12_Circuit.png](12_Circuit.png)


## Information about the Code:
- The push-button is connected to GPIO pin 14 with a pull-up resistor.
- The LED is connected to GPIO pin 15.
- The program continuously checks the state of the button using `button.value()`.
- When the button is pressed and released, the LED toggles its state.
