from machine import Pin, PWM, ADC
from utime import sleep, ticks_ms, ticks_diff, time

print('-------------')
print('----ready----')
print('-------------')

class tick_element():
    def __init__(self, freq):
        self.freq = freq
        self.last_time = 0
        
    def on_tick(self):
        pass
    
    def tick(self):
        if ticks_diff(ticks_ms(), self.last_time) > self.freq:
            self.last_time = ticks_ms()

            self.on_tick()

class blinking_led(tick_element):
    def __init__(self, freq, pin):
        super().__init__(freq)

        self.led = Pin(pin, Pin.OUT)
        self.led_on = False
        self.should_blink = True

    def on_tick(self):
        if self.should_blink:
            if self.led_on:
                self.led.off()
            else:
                self.led.on()

            self.led_on = not self.led_on

    def togle_blink(self):
        self.should_blink = not self.should_blink

class pwm_led(tick_element):
    def __init__(self, freq, pin):
        super().__init__(freq)

        self.led = PWM(Pin(pin), 1)
        self.duty = 0 # range 0 - 1023

        # Min max values for dial
        self.min_val = 0.128
        self.max_val = 3.152

    def change_duty(self, val):
        normalized_val = (val - self.min_val) / (self.max_val - self.min_val)

        if 0 <= normalized_val <= 1:
            self.duty = int(normalized_val * 1023) # val in range 0 - 1, duty in range 0 - 1023

        self.led.duty(self.duty)

class button(tick_element):
    def __init__(self, freq, pin, callbacks):
        super().__init__(freq)

        self.pin = pin

        self.button = Pin(pin, Pin.IN, Pin.PULL_DOWN)
        self.callbacks = callbacks # an array of callback function, called on button press
        self.last_val = 0
        self.press_count = 0

    def on_tick(self):
        if self.button.value() == 0 and self.last_val == 1:
            print('button pressed')

            for callback in self.callbacks:
                callback()

            self.press_count += 1
            self.last_val = 0

        elif self.button.value() == 1:
            self.last_val = 1

class adc(tick_element):
    def __init__(self, freq, pin, callbacks):
        super().__init__(freq)

        self.callbacks = callbacks # an array of callback function, called on value changed

        self.adc = ADC(Pin(pin))
        self.adc.atten(ADC.ATTN_11DB)

        self.val = 0

    def on_tick(self):
        new_val = self.adc.read_uv() * 10**(-6)
        if new_val != self.val:
            #print(new_val, 'V')

            for callback in self.callbacks:
                callback(new_val)

        self.val = new_val

class data_gatherer():
    def __init__(self, file_name):

        self.file_name = file_name
        self.is_active = True

        self.data = ''
        self.gather_start_time = 0

    def write_to_file(self, text):
        f_out = open('data.txt', 'w')

        f_out.write(text)

        f_out.close()

    def add_data_point(self, data):
        self.data += data + '\n'

    def add_adc_data(self, val):
        data_point = str((time() - self.gather_start_time)) + ' - ' + str(val)
        self.add_data_point(data_point)

    def toggle_capture_data(self):
        self.is_active = not self.is_active

        if self.is_active:
            print('stopping to gather data')

            self.write_to_file(self.data)

            print('data gathered:')
            with open(self.file_name) as f:
                data_text = f.read()
                print(data_text)

        else:
            print('starting to gather data')

            self.gather_start_time = time()