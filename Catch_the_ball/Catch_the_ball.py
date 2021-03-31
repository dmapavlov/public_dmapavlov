import pygame
from pygame.draw import *
from random import randint
from math import sqrt

pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
points = 0


def new_ball():
    '''рисует новый шарик'''
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle1 = circle(screen, color, (x, y), r)
    #circle1.move([2, 2])


def click(event):
    """проверяет, попали мы в круг или нет, если попали, то +1 очко"""
    global points
    pos = pygame.mouse.get_pos()
    if (pos[0] - x) ** 2 + (pos[1] - y) ** 2 <= r ** 2:
        points += 1


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)
print('Вы набрали', points, 'очков')

pygame.quit()
