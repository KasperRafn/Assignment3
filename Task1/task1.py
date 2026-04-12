# Task 1: Blink a red LED at 1 Hz (500 ms on/off) only while a button is pressed. Use a 330 Ω resistor and a button.

from machine import Pin
from utime import sleep

print('-------------')
print('----Task1----')
print('-------------')

# LED
led = Pin(13, Pin.OUT)

# Button
button = Pin(27, Pin.IN, Pin.PULL_DOWN)

# Main loop
while True:
    if button.value() == 1:
        led.on()
        sleep(0.5)
        led.off()
        sleep(0.5)
    else:
        led.off()