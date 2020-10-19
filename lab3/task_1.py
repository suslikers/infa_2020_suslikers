import pygame
from pygame.draw import *

pygame.init()

FPS = 30

screen = pygame.display.set_mode((400, 400))
rect(screen, [255, 255, 250], [0, 0, 400, 400])


circle(screen, [255, 255, 0], [200, 200], 100)
circle(screen, [255, 0, 0], [160, 160], 20)
circle(screen, [255, 0, 0], [240, 160], 17)
circle(screen, [0, 0, 0], [160, 160], 10)
circle(screen, [0, 0, 0], [240, 160], 8)


rect(screen, [0, 0, 0], [140, 240, 120, 21])

polygon(screen, (0, 0, 0), [(120, 120), (125, 105),
                               (209, 163), (200, 170)])
polygon(screen, (0, 0, 0), [(280, 120), (275, 105),
                               (191, 163), (200, 170)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()