# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pygame
from pygame.draw import *

pygame.init()
clock = pygame.time.Clock()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (0, 255, 255), (0, 0, 400, 400))

circle(screen, (255, 255, 0), (200, 175), 150)
circle(screen, (0, 0, 0), (200, 175), 150, 5)

rect(screen, (0, 0, 0), (100, 230, 200, 40))
circle(screen, (255, 0, 0), (130, 120), 40)
circle(screen, (0, 0, 0), (130, 120), 40, 5)
circle(screen, (0, 0, 0), (130, 120), 20)
circle(screen, (255, 0, 0), (280, 120), 30)
circle(screen, (0, 0, 0), (280, 120), 30, 5)
circle(screen, (0, 0, 0), (280, 120), 15)
#rect(screen, (0, 0, 0), (40, 50, 100, 100))
polygon(screen, (0, 0, 0), [(30,30), (20,60),
                               (200,80), (200,60)])
polygon(screen, (0, 0, 0), [(400,50), (400,70),
                            (230,100), (220,80)])
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

