from machine import ADC, Pin
import time

# Create ADC object on pin 13
ldr = ADC(Pin(13))

# Configure ADC
ldr.atten(ADC.ATTN_11DB) 
#ldr.width(ADC.WIDTH_12BIT)

while True:
    value = ldr.read()
    print("LDR value:", value)
    time.sleep(0.5)