# Task 2: Cycle through three LEDs (green, yellow, red) each time a button is pressed. Start with green; each press advances to the next color (green→yellow→red→green…). A single press is counted only once, even if held.

from machine import Pin
from utime import sleep

print('-------------')
print('----Task2----')
print('-------------')

# LEDs
green_led = Pin(15, Pin.OUT)
yellow_led = Pin(12, Pin.OUT)
red_led = Pin(33, Pin.OUT)

leds = [green_led, yellow_led, red_led]
current_led_index = 0

def update_leds(index):
    for i in range(3):
        leds[i].value(1 if i == index else 0)

update_leds(current_led_index)

# Button
button = Pin(27, Pin.IN, Pin.PULL_DOWN)

last_button_state = 0

# Main loop
while True:
    current_button_state = button.value()

    # Detect if the button was pressed e.g. if button state changed
    if current_button_state == 1 and last_button_state == 0:
        current_led_index = (current_led_index + 1) % 3
        update_leds(current_led_index)

        print('button pressed')

        # debounce delay
        sleep(0.2)

    last_button_state = current_button_state
    sleep(0.01)