from machine import Pin, ADC, PWM
from utime import ticks_ms, ticks_diff

# Task 2: Cycle through three LEDs (green, yellow, red) each time a button is pressed. Start with green; each press advances to the next color (green→yellow→red→green…). A single press is counted only once, even if held.

print('-------------')
print('----Task2----')
print('-------------')