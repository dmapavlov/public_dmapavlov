import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

x1 = 100
y1 = 100
x2 = 300
y2 = 200
N = 10
color_yellow = (255, 211, 0)
color_red = (255, 0, 0)
color_black = (0, 0, 0)
color_white = (255, 255, 255)
circle(screen, color_yellow, (200, 200), 100)
circle(screen, color_red, (150, 170), 25)
circle(screen, color_red, (250, 170), 20)
circle(screen, color_black, (150, 170), 10)
circle(screen, color_black, (250, 170), 10)
rect(screen, color_black, (150, 240, 100, 20))  # left, top, width, height
polygon(screen, color_white, [(110, 90), (90, 110), (150, 140), (140, 150)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
