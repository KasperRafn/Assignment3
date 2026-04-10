from machine import Pin, I2C
import time

print('-------------')
print('----Task4----')
print('-------------')

# --- I2C Setup ---
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

MCP9808_ADDR = 0x18

# --- RGB LED Pins ---
red = Pin(15, Pin.OUT)
green = Pin(13, Pin.OUT)
blue = Pin(12, Pin.OUT)

# --- Set this depending on your LED type ---
COMMON_ANODE = True  # Change to False if using common cathode

def set_color(r, g, b):
    if COMMON_ANODE:
        red.value(1 - r)
        green.value(1 - g)
        blue.value(1 - b)
    else:
        red.value(r)
        green.value(g)
        blue.value(b)

def read_temperature():
    data = i2c.readfrom_mem(MCP9808_ADDR, 0x05, 2)
    temp = ((data[0] << 8) | data[1]) & 0x0FFF
    temp /= 16.0
    if temp > 2047:
        temp -= 4096
    return temp

# --- Thresholds (adjust as needed) ---
LOW_TEMP = 24      # Room temperature
HIGH_TEMP = 28     # Touch temperature

while True:
    temp = read_temperature()
    print("Temperature:", temp)

    if temp < LOW_TEMP:
        # Green
        set_color(0, 1, 0)

    elif LOW_TEMP <= temp < HIGH_TEMP:
        # Yellow (Red + Green)
        set_color(1, 1, 0)

    else:
        # Red
        set_color(1, 0, 0)

    time.sleep(1)