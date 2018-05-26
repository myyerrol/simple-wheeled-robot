import sys
import pygame
from pygame.locals import *
import RPi.GPIO as gpio
from raspberry_pi_simple_car_lib import RaspberryPiSimpleCar

raspberry_pi_simple_car = RaspberryPiSimpleCar()

pygame.init()
screen = pygame.display.set_mode((800, 800))
font = pygame.font.SysFont("arial", 64)
pygame.display.set_caption('RaspberryPiSimpleCar')
pygame.mouse.set_visible(0)

while True:
    gpio.cleanup()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            time = 0.03
        if event.key == K_UP or event.key == ord('w'):
            raspberry_pi_simple_car.go_forward(time)
        elif event.key == K_DOWN or event.key == ord('s'):
            raspberry_pi_simple_car.go_reverse(time)
        elif event.key == K_LEFT or event.key == ord('a'):
            raspberry_pi_simple_car.go_left(time)
        elif event.key == K_RIGHT or event.key == ord('d'):
            raspberry_pi_simple_car.go_right(time)
        elif event.key == ord('q'):
            raspberry_pi_simple_car.go_pivot_left(time)
        elif event.key == ord('e'):
            raspberry_pi_simple_car.go_pivot_right(time)
