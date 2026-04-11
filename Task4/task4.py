from machine import Pin, I2C
from machine import Pin, ADC, PWM, I2C
from utime import sleep, ticks_ms, ticks_diff, time

#Task 4: Replace the three separate LEDs with a single RGB LED. Use it to show the same color changes (green → yellow → red) based on the temperature, using the RGB LED’s three channels.

print('-------------')
print('----Task4----')
print('-------------')

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

# Color changing

red   = PWM(Pin(33), freq=500)
green = PWM(Pin(15), freq=500)
blue  = PWM(Pin(12), freq=500)

def set_color(r, g, b):
    red.duty(int(r / 255 * 1023))
    green.duty(int(g / 255 * 1023))
    blue.duty(int(b / 255 * 1023))

# Thresholds
LOW_TEMP = 28
HIGH_TEMP = 30

while True:
    data = i2c.readfrom_mem(address, temp_reg, 2)
    temperature = temp_c(data)
    print("Temp:", temperature)
    
    if temperature < LOW_TEMP:
        # Green
        set_color(255,0,255)

    elif LOW_TEMP <= temperature < HIGH_TEMP:
        # Yellow
        set_color(0, 0, 255)

    else:
        # Red
        set_color(0, 255, 255)

    sleep(1)