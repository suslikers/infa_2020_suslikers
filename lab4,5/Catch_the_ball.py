import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 0.5
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    global x, y, r
    '''рисует новый шарик '''
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

# Функция сравнивает координаты шарика м мышки
def click(event):
    print(f"Координаты шара {x} {y} {r}")
    coordinate_x = event.pos[0]
    coordinate_y = event.pos[1]
    print(f'{coordinate_x} x мыши,  {x} x шара, {coordinate_y} y мыши, {y} y шара, r')
    if (coordinate_x - x)**2 + (coordinate_y - y)**2 <= r**2:
        print('Попал!')
    elif (coordinate_x - x)**2 + (coordinate_y - y)**2 > r**2:
        print('Мимо!')
    else:
        print('Ошибка в функции click')



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

pygame.quit()