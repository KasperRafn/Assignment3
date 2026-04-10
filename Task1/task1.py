from machine import Pin, PWM, ADC
from utime import sleep, ticks_ms, ticks_diff, time

# Task 1: Blink a red LED at 1 Hz (500 ms on/off) only while a button is pressed. Use a 330 Ω resistor and a button.

print('-------------')
print('----Task1----')
print('-------------')

led = Pin(13, Pin.OUT)
button = Pin(27, Pin.IN, Pin.PULL_DOWN)

while True:
    print(button.value())
    if button.value() == 1: # Button is pressed
        led.on()
        sleep(0.5) # Keep the LED on for 0.5 seconds
        led.off()
        sleep(0.5) # Wait for 0.5 seconds before checking the button
    else: # Button is not pressed
        led.off()