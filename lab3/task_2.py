import pygame
from pygame.draw import *

pygame.init()
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
FPS = 30
len_space = 793
height_space = 1024
pi = 3.14
screen = pygame.display.set_mode((len_space, height_space))
# Function create background
def background():
    rect(screen, [33, 33, 120], [0, 0, len_space, 128])
    rect(screen, [141, 95, 211], [0, 128, len_space, 64])
    rect(screen, [205, 135, 222], [0, 192, len_space, 120])
    rect(screen, [222, 135, 170], [0, 290, len_space, 328])
    rect(screen, [255, 153, 85], [0, 448, len_space, 180])
    rect(screen, [0, 102, 128], [0, 612, len_space, 612])
background()
# Function create background in x,y coordinate with s scale
def fish(x, y, s):

    ellipse(screen, [71, 136, 147], [x, y-s, s*5, s*2])
    arc(screen, BLACK, [x, y-s, s*5, s*2], 0, 2*pi, 1)
    polygon(screen, [71, 136, 147], [(x, y), (x-s, y+s), (x-s, y-s)])
    circle(screen, BLACK, [x + 4*s, y], 3)


fish(250, 720, 50)
fish(80, 830, 30)
fish(600, 680, 20)
fish(600, 780, 20)




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()