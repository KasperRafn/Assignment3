
# Task 5: Control the brightness of two NeoPixel LEDs using a potentiometer. Read the analog voltage from the pot and map it to a brightness level (0–full brightness).

from machine import Pin, PWM, ADC
from utime import sleep

print('-------------')
print('----Task5----')
print('-------------')

# PWM LED Setup
led = PWM(Pin(15), 1000)
dial_range = [0.128, 3.122]

def change_duty(val):
    normalized_val = (val - dial_range[0]) / (dial_range[1] - dial_range[0])

    if 0 <= normalized_val <= 1:
        led.duty(int(normalized_val * 1023))

# Dial Setup
dial = ADC(Pin(14))
dial.atten(ADC.ATTN_11DB)

# Main loop
while True:
    val = dial.read_uv() * 10**(-6)
    print('Dial value:', val)

    change_duty(val)

    sleep(0.1)