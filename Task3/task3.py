from machine import Pin, ADC, PWM, I2C
from utime import sleep, ticks_ms, ticks_diff, time

import lib.non_blocking as nb

# Task 3: Read temperature from the MCP9808 sensor. Light the green LED for normal/room temperature, yellow when it reaches a warmer threshold, and red when it gets hot. The thresholds should be set so you can trigger them by touching the sensor.

print('-------------')
print('----Task3----')
print('-------------')

# LEDS
green_led = Pin(15, Pin.OUT)
yellow_led = Pin(12, Pin.OUT)
red_led = Pin(33, Pin.OUT)

# I2C Setup

i2c = I2C(0, scl=Pin(22), sda=Pin(21))

address = 0x18  # 24 in hex
temp_reg = 0x05

def temp_c(data):
    value = data[0] << 8 | data[1]
    temp = (value & 0x0FFF) / 16.0
    if value & 0x1000:
        temp -= 256.0
    return temp

# Sensor

def change_led_color(new_sensor_value):
    if new_sensor_value < 29:
        green_led.on()
        yellow_led.off()
        red_led.off()
    elif 29 <= new_sensor_value < 30:
        green_led.off()
        yellow_led.on()
        red_led.off()
    else:
        green_led.off()
        yellow_led.off()
        red_led.on()

while True:
    data = i2c.readfrom_mem(address, temp_reg, 2)
    temperature = temp_c(data)
    print("Temp:", temperature)

    change_led_color(temperature)

    sleep(0.5)