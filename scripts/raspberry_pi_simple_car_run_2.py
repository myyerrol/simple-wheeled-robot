import Tkinter as tk
import RPi.GPIO as gpio
from raspberry_pi_simple_car_lib import RaspberryPiSimpleCar

raspberry_pi_simple_car = RaspberryPiSimpleCar()
raspberry_pi_simple_car.initialize_lcd()

def input_key(event):
    print 'Key', event.char
    key_press = event.char
    seconds = 0.05

    if key_press.lower() == 'w':
        raspberry_pi_simple_car.go_forward(seconds)
    elif key_press.lower() == 's':
        raspberry_pi_simple_car.go_reverse(seconds)
    elif key_press.lower() == 'a':
        raspberry_pi_simple_car.go_left(seconds)
    elif key_press.lower() == 'd':
        raspberry_pi_simple_car.go_right(seconds)
    elif key_press.lower() == 'q':
        raspberry_pi_simple_car.go_pivot_left(seconds)
    elif key_press.lower() == 'e':
        raspberry_pi_simple_car.go_pivot_right(seconds)
    elif key_press.lower() == 'o':
        raspberry_pi_simple_car.move_servo_left()
    elif key_press.lower() == 'p':
        raspberry_pi_simple_car.move_servo_right()
    else:
        pass

    distance = raspberry_pi_simple_car.get_distance()
    raspberry_pi_simple_car.print_lcd(1, 0, 'UltrasonicWare')
    raspberry_pi_simple_car.print_lcd(1, 1, 'Distance:%.lf CM' % distance)
    print "Distance: %.1f CM" % distance

    if distance < 10:
        raspberry_pi_simple_car.__init__()
        raspberry_pi_simple_car.go_reverse(2)

try:
    command = tk.Tk()
    command.bind('<KeyPress>', input_key)
    command.mainloop()
except KeyboardInterrupt:
    gpio.cleanup()
