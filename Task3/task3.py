from time import time

from machine import Pin, ADC, PWM
from utime import ticks_ms, ticks_diff

import lib.non_blocking as nb

import busio
import adafruit_mcp9808

# Task 3: Read temperature from the MCP9808 sensor. Light the green LED for normal/room temperature, yellow when it reaches a warmer threshold, and red when it gets hot. The thresholds should be set so you can trigger them by touching the sensor.

print('-------------')
print('----Task3----')
print('-------------')

# LEDS
green_led = Pin(15, Pin.OUT)
yellow_led = Pin(12, Pin.OUT)
red_led = Pin(33, Pin.OUT)

# SDA Pin = 21

# Sensor
def change_led_color(new_sensor_value):
    if new_sensor_value < 25:
        green_led.on()
        yellow_led.off()
        red_led.off()
    elif 25 <= new_sensor_value < 30:
        green_led.off()
        yellow_led.on()
        red_led.off()
    else:
        green_led.off()
        yellow_led.off()
        red_led.on()

sensor_pin = 32
temp_sensor_ = nb.adc(20, sensor_pin, [change_led_color])

####################

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_mcp9808.MCP9808(i2c)

while True:
    # Read temperature in Celsius
    c = sensor.temperature
    
    # Convert to Fahrenheit
    f = c * 9.0 / 5.0 + 32

    # Print values
    print(f"Temp: {c:.2f} C\t{f:.2f} F")

    # Wait 250 ms
    time.sleep(0.25)

    # Put sensor to sleep
    sensor.shutdown = True
    time.sleep(2)

    # Wake sensor back up
    sensor.shutdown = False