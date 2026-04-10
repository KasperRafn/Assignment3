from machine import Pin, ADC, PWM
from utime import ticks_ms, ticks_diff

import lib.non_blocking as nb

# Task 3: Read temperature from the MCP9808 sensor. Light the green LED for normal/room temperature, yellow when it reaches a warmer threshold, and red when it gets hot. The thresholds should be set so you can trigger them by touching the sensor.

print('-------------')
print('----Task3----')
print('-------------')

# LEDS
green_led = Pin(15, Pin.OUT)
yellow_led = Pin(14, Pin.OUT)
red_led = Pin(12, Pin.OUT)

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

sensor_pin = 13
temp_sensor = nb.adc(20, sensor_pin, [change_led_color])

while True:
    temp_sensor.tick()