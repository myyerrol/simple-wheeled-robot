import Tkinter as tk
import RPi.GPIO as gpio
from simple_wheeled_robot_lib import SimpleWheeledRobot

simple_wheeled_robot = SimpleWheeledRobot()
simple_wheeled_robot.initialize_lcd()

def input_key(event):
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
        simple_wheeled_robot.move_servo_left()
    elif key_press.lower() == 'p':
        simple_wheeled_robot.move_servo_right()
    else:
        pass

    distance = simple_wheeled_robot.get_distance()
    simple_wheeled_robot.print_lcd(1, 0, 'UltrasonicWare')
    simple_wheeled_robot.print_lcd(1, 1, 'Distance:%.lf CM' % distance)
    print "Distance: %.1f CM" % distance

    if distance < 10:
        simple_wheeled_robot.__init__()
        simple_wheeled_robot.go_reverse(2)

try:
    command = tk.Tk()
    command.bind('<KeyPress>', input_key)
    command.mainloop()
except KeyboardInterrupt:
    gpio.cleanup()
