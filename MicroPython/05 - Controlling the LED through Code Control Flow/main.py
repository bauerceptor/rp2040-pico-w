from machine import Pin

led = Pin(15, Pin.OUT)

while True:
    command = input("Enter 1 to ON, 2 to OFF or 3 to TOGGLE the LED: ")
    command = int(command)
    
    if (command == 1):
        led.value(True)
    elif (command == 2):
        led.value(False)
    elif (command == 3):
        led.toggle()
    elif (command == 4):
        break
    else:
        print("Invalid command.")
