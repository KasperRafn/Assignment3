from machine import Pin, ADC, PWM
from utime import ticks_ms, ticks_diff

import lib.non_blocking as nb

# Task 5: Control the brightness of two NeoPixel LEDs using a potentiometer. Read the analog voltage from the pot and map it to a brightness level (0–full brightness).

print('-------------')
print('----Task5----')
print('-------------')

pwm_led_pin = 15
dimmable_led = nb.pwm_led(50, pwm_led_pin)

dial_pin = 12
dial_callbacks = [dimmable_led.change_duty]
dial = nb.adc(50, dial_pin, dial_callbacks)

while True:
    dial.tick()
    dimmable_led.tick()