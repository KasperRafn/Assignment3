from machine import Pin

print('-------------')
print('----ready----')
print('-------------')

led = Pin(13, Pin.OUT)

led.on()

# Add button reading code
button = Pin(27, Pin.IN, Pin.PULL_DOWN)

while True:
    print(button.value())

# test abcd