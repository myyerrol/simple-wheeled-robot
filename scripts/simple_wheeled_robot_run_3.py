import sys
import pygame
from pygame.locals import *
import RPi.GPIO as gpio
from simple_wheeled_robot_lib import SimpleWheeledRobot

simple_wheeled_robot = SimpleWheeledRobot()

pygame.init()
screen = pygame.display.set_mode((800, 800))
font = pygame.font.SysFont("arial", 64)
pygame.display.set_caption('SimpleWheeledRobot')
pygame.mouse.set_visible(0)

while True:
    gpio.cleanup()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            time = 0.03
        if event.key == K_UP or event.key == ord('w'):
            simple_wheeled_robot.go_forward(time)
        elif event.key == K_DOWN or event.key == ord('s'):
            simple_wheeled_robot.go_reverse(time)
        elif event.key == K_LEFT or event.key == ord('a'):
            simple_wheeled_robot.go_left(time)
        elif event.key == K_RIGHT or event.key == ord('d'):
            simple_wheeled_robot.go_right(time)
        elif event.key == ord('q'):
            simple_wheeled_robot.go_pivot_left(time)
        elif event.key == ord('e'):
            simple_wheeled_robot.go_pivot_right(time)
