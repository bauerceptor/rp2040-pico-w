from machine import Pin
import utime as time			# micropython implementation of Time function
from dht import DHT11			# provides library to interact with the Humidity-&-Temprature sensor

data_pin = 16

pin = PIN(data_pin, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(pin)
print('My Sensor Data')

while True:
    sensor.measure()
    temp_c = sensor.temperature()
    humidity = sensor.humidity()
    print('\r','Temperature = ', temp_c, chr(176)+'C ','Humidity = ' humidity,'%', end='')
    time.sleep(1)
