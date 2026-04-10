from machine import Pin
import time

# LED pins
green = Pin(14, Pin.OUT)
yellow = Pin(27, Pin.OUT)
red = Pin(26, Pin.OUT)

# Button pin
button = Pin(33, Pin.IN)

# LED states list
leds = [green, yellow, red]
current_index = 0

# Turn on initial LED (green)
def update_leds(index):
    for i in range(3):
        leds[i].value(1 if i == index else 0)

update_leds(current_index)

# For edge detection
last_button_state = 0

while True:
    current_button_state = button.value()

    # Detect rising edge (button pressed)
    if current_button_state == 1 and last_button_state == 0:
        current_index = (current_index + 1) % 3
        update_leds(current_index)

        # debounce delay
        time.sleep(0.2)

    last_button_state = current_button_state
    time.sleep(0.01)