import time
import serial
import random
import Tkinter as tk
import RPi.gpio as gpio
from simple_wheeled_robot_lib import SimpleWheeledRobot

simple_wheeled_robot = SimpleWheeledRobot()
simple_wheeled_robot.initialize_lcd()
port = "/dev/ttyUSB0"
serial_to_arduino = serial.Serial(port, 9600)
serial_from_arduino = serial.Serial(port, 9600)
serial_from_arduino.flushInput()
serial_to_arduino.write('n')

def detecte_distance():
    distance = simple_wheeled_robot.get_distance()

    if distance >= 20:
        # Light up the green led.
        serial_to_arduino.write('g')
    elif distance >= 10:
        # Light up the yellow led.
        serial_to_arduino.write('y')
    elif distance < 10:
        # Light up the red led.
        serial_to_arduino.write('r')
        simple_wheeled_robot.buzzing()
        simple_wheeled_robot.__init__()
        simple_wheeled_robot.go_reverse(2)
        simple_wheeled_robot.__init__()
        simple_wheeled_robot.go_pivot_right(2)

    # Check the distance between wall and car's both sides.
    serial_to_arduino.write('k')
    data_from_arduino = serial_from_arduino.readline()
    data_from_arduino_int = int(data_from_arduino)

    # Car is too close to the left wall.
    if data_from_arduino_int == 01:
        simple_wheeled_robot.buzzing()
        simple_wheeled_robot.__init__()
        simple_wheeled_robot.go_right(2)
    # Car is too close to the right wall.
    elif data_from_arduino_int == 10:
        simple_wheeled_robot.buzzing()
        simple_wheeled_robot.__init__()
        simple_wheeled_robot.go_left(2)

def input_key(event):
    simple_wheeled_robot.__init__()
    print 'Key', event.char
    key_press = event.char
    seconds = 0.05

    if key_press.lower() == 'w':
        simple_wheeled_robot.go_forward(seconds)
    elif key_press.lower() == 's':
        simple_wheeled_robot.go_reverse(seconds)
    elif key_press.lower() == 'a':
        simple_wheeled_robot.go_left(seconds)
    elif key_press.lower() == 'd':
        simple_wheeled_robot.go_right(seconds)
    elif key_press.lower() == 'q':
        simple_wheeled_robot.go_pivot_left(seconds)
    elif key_press.lower() == 'e':
        simple_wheeled_robot.go_pivot_right(seconds)
    elif key_press.lower() == 'o':
        gpio.cleanup()
        # Move the servo in forward directory.
        serial_to_arduino.write('o')
        time.sleep(0.05)
    elif key_press.lower() == 'h':
        gpio.cleanup()
        # Light up the logo.
        serial_to_arduino.write('h')
    elif key_press.lower() == 'j':
        gpio.cleanup()
        # Turn off the logo.
        serial_to_arduino.write('j')
    elif key_press.lower() == 'p':
        gpio.cleanup()
        # Move the servo in reverse directory.
        serial_to_arduino.write('p')
        time.sleep(0.05)
    elif key_press.lower() == 'i':
        gpio.cleanup()
        serial_to_arduino.write('m')
        # Enter the random run mode.
        serial_to_arduino.write('i')
        for z in range(20):
            x = random.randrange(0, 5)
            if x == 0:
                for y in range(30):
                    detecte_distance()
                    simple_wheeled_robot.__init__()
                    simple_wheeled_robot.go_forward(0.05)
            elif x == 1:
                for y in range(30):
                    detecte_distance()
                    simple_wheeled_robot.__init__()
                    simple_wheeled_robot.go_left(0.05)
            elif x == 2:
                for y in range(30):
                    detecte_distance()
                    simple_wheeled_robot.__init__()
                    simple_wheeled_robot.go_right(0.05)
            elif x == 3:
                for y in range(30):
                    detecte_distance()
                    simple_wheeled_robot.__init__()
                    simple_wheeled_robot.go_pivot_left(0.05)
            elif x == 4:
                for y in range(30):
                    detecte_distance()
                    simple_wheeled_robot.__init__()
                    simple_wheeled_robot.go_pivot_right(0.05)

            data_from_arduino = serial_from_arduino.readline()
            data_from_arduino_int = int(data_from_arduino)

            if data_from_arduino_int == 1111:
                simple_wheeled_robot.__init__()
                simple_wheeled_robot.go_forward(0.05)
                if data_from_arduino_int == 1111:
                    simple_wheeled_robot.__init__()
                    simple_wheeled_robot.stop()
                elif data_from_arduino_int == 0000:
                    simple_wheeled_robot.__init__()
                    simple_wheeled_robot.go_forward(0.05)
                elif data_from_arduino_int == 0100:
                    simple_wheeled_robot.__init__()
                    simple_wheeled_robot.go_left(0.05)
                elif data_from_arduino_int == 1000 or \
                     data_from_arduino_int == 1100:
                    simple_wheeled_robot.__init__()
                    simple_wheeled_robot.go_left(0.08)
                elif data_from_arduino_int == 0010:
                    simple_wheeled_robot.__init__()
                    simple_wheeled_robot.go_right(0.05)
                elif data_from_arduino_int == 0001 or \
                     data_from_arduino_int == 0011:
                    simple_wheeled_robot.__init__()
                    simple_wheeled_robot.go_right(0.08)

        serial_to_arduino.write('l')

    elif key_press.lower() == 'u':
        gpio.cleanup()
        simple_wheeled_robot.print_lcd(1, 0, 'UltrasonicWare')
        simple_wheeled_robot.print_lcd(1, 1, 'Distance:%.lf CM' %
                                              simple_wheeled_robot.get_distance())
    else:
        pass

    distance = simple_wheeled_robot.get_distance()

    if distance >= 20:
        serial_to_arduino.write('g')
    elif distance >= 10:
        serial_to_arduino.write('y')
    elif distance < 10:
        serial_to_arduino.write('r')
        simple_wheeled_robot.buzzing()
        simple_wheeled_robot.__init__()
        simple_wheeled_robot.go_reverse(2)

    serial_to_arduino.write('k')
    data_from_arduino = serial_from_arduino.readline()
    data_from_arduino_int = int(data_from_arduino)

    if data_from_arduino_int == 1:
        simple_wheeled_robot.buzzing()
        simple_wheeled_robot.__init__()
        simple_wheeled_robot.go_right(2)
    elif data_from_arduino_int == 10:
        simple_wheeled_robot.buzzing()
        simple_wheeled_robot.__init__()
        simple_wheeled_robot.go_left(2)

try:
    command = tk.Tk()
    command.bind('<KeyPress>', input_key)
    command.mainloop()
except KeyboardInterrupt:
    gpio.cleanup()
