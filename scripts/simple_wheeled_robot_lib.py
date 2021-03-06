import time
import smbus
import RPi.GPIO as gpio

motor_run_left        = 17
motor_run_right       = 10
motor_direction_left  = 4
motor_direction_right = 25
led_left              = 7
led_right             = 8
ultrasonic_trig       = 23
ultrasonic_echo       = 24
servo                 = 11
buzzer                = 18
lcd_address           = 0x27
data_bus = smbus.SMBus(1)

class SimpleWheeledRobot:
    def __init__(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(motor_run_left, gpio.OUT)
        gpio.setup(motor_run_right, gpio.OUT)
        gpio.setup(motor_direction_left, gpio.OUT)
        gpio.setup(motor_direction_right, gpio.OUT)
        gpio.setup(led_left, gpio.OUT)
        gpio.setup(led_right, gpio.OUT)

    def set_motors(self, run_left, direction_left, run_right, direction_right):
        gpio.output(motor_run_left, run_left)
        gpio.output(motor_run_right, run_right)
        gpio.output(motor_direction_left, direction_left)
        gpio.output(motor_direction_right, direction_right)

    def set_led_left(self, state):
        gpio.output(led_left, state)

    def set_led_right(self, state):
        gpio.output(led_right, state)

    def go_forward(self, seconds):
        if seconds == 0:
            self.set_motors(1, 1, 1, 1)
            self.set_led_left(1)
            self.set_led_right(1)
        else:
            self.set_motors(1, 1, 1, 1)
            time.sleep(seconds)
            gpio.cleanup()

    def go_reverse(self, seconds):
        if seconds == 0:
            self.set_motors(1, 0, 1, 0)
            self.set_led_left(0)
            self.set_led_right(0)
        else:
            self.set_motors(1, 0, 1, 0)
            time.sleep(seconds)
            gpio.cleanup()

    def go_left(self, seconds):
        if seconds == 0:
            self.set_motors(0, 0, 1, 1)
            self.set_led_left(1)
            self.set_led_right(0)
        else:
            self.set_motors(0, 0, 1, 1)
            time.sleep(seconds)
            gpio.cleanup()

    def go_right(self, seconds):
        if seconds == 0:
            self.set_motors(1, 1, 0, 0)
            self.set_led_left(0)
            self.set_led_right(1)
        else:
            self.set_motors(1, 1, 0, 0)
            time.sleep(seconds)
            gpio.cleanup()

    def go_pivot_left(self, seconds):
        if seconds == 0:
            self.set_motors(1, 0, 1, 1)
            self.set_led_left(1)
            self.set_led_right(0)
        else:
            self.set_motors(1, 0, 1, 1)
            time.sleep(seconds)
            gpio.cleanup()

    def go_pivot_right(self, seconds):
        if seconds == 0:
            self.set_motors(1, 1, 1, 0)
            self.set_led_left(0)
            self.set_led_right(1)
        else:
            self.set_motors(1, 1, 1, 0)
            time.sleep(seconds)
            gpio.cleanup()

    def stop(self):
        self.set_motors(0, 0, 0, 0)
        self.set_led_left(0)
        self.set_led_right(0)

    def buzzing(self):
        gpio.setup(buzzer, gpio.OUT)
        gpio.output(buzzer, True)
        for x in range(5):
            gpio.output(buzzer, False)
            time.sleep(0.1)
            gpio.output(buzzer, True)
            time.sleep(0.1)

    def get_distance(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(ultrasonic_trig, gpio.OUT)
        gpio.setup(ultrasonic_echo, gpio.IN)
        gpio.output(ultrasonic_trig, False)
        while gpio.input(ultrasonic_echo) == 0:
            start_time = time.time()
        while gpio.input(ultrasonic_echo) == 1:
            stop_time = time.time()
        duration = stop_time - start_time
        distance = (duration * 34300) / 2
        gpio.cleanup()
        return distance

    def send_command(self, command):
        buf = command & 0xF0
        buf |= 0x04
        data_bus.write_byte(lcd_address, buf)
        time.sleep(0.002)
        buf &= 0xFB
        data_bus.write_byte(lcd_address, buf)
        buf = (command & 0x0F) << 4
        buf |= 0x04
        data_bus.write_byte(lcd_address, buf)
        time.sleep(0.002)
        buf &= 0xFB
        data_bus.write_byte(lcd_address, buf)

    def send_data(self, data):
        buf = data & 0xF0
        buf |= 0x05
        data_bus.write_byte(lcd_address, buf)
        time.sleep(0.002)
        buf &= 0xFB
        data_bus.write_byte(lcd_address, buf)
        buf = (data & 0x0F) << 4
        buf |= 0x05
        data_bus.write_byte(lcd_address, buf)
        time.sleep(0.002)
        buf &= 0xFB
        data_bus.write_byte(lcd_address, buf)

    def initialize_lcd(self):
        try:
            self.send_command(0x33)
            time.sleep(0.005)
            self.send_command(0x32)
            time.sleep(0.005)
            self.send_command(0x28)
            time.sleep(0.005)
            self.send_command(0x0C)
            time.sleep(0.005)
            self.send_command(0x01)
        except:
            return False
        else:
            return True

    def clear_lcd(self):
        self.send_command(0x01)

    def print_lcd(self, x, y, lcd_string):
        if x < 0:
            x = 0
        if x > 15:
            x = 15
        if y < 0:
            y = 0
        if y > 1:
            y = 1
        address = 0x80 + 0x40 * y + x
        self.send_command(address)
        for lcd_char in lcd_string:
            self.send_data(ord(lcd_char))

    def move_servo_left(self):
        servo_range = 13
        gpio.setmode(gpio.BCM)
        gpio.setup(servo, gpio.OUT)
        pwm = gpio.PWM(servo, 100)
        pwm.start(0)
        while servo_range <= 23:
            pwm.ChangeDutyCycle(servo_range)
            servo_range += 1
            time.sleep(0.5)
        pwm.stop()

    def move_servo_right(self):
        servo_range = 13
        gpio.setmode(gpio.BCM)
        gpio.setup(servo, gpio.OUT)
        pwm = gpio.PWM(servo, 100)
        pwm.start(0)
        while servo_range >= 0:
            pwm.ChangeDutyCycle(servo_range)
            servo_range -= 1
            time.sleep(0.5)
        pwm.stop()
