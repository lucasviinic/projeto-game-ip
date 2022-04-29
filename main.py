import pygame
from pygame.locals import *
from sys import exit

pygame.init()

# screen info

width = 960
height = 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Kirby')
font = pygame.font.SysFont('Akziden Ghost', 50, True, False)
clock = pygame.time.Clock()

# player info

kirbyx, kirbyy = 50, 475
points = 0
life = 50

# collectables info

draw_coin = True
draw_potion = True

# game loop

while True:
    clock.tick(200)
    screen.fill('BLACK')
    score = f'Points: {points}'
    life_points = f'Life: {life}/100'
    text1 = font.render(score, True, 'GOLD')
    text2 = font.render(life_points, True, 'RED')
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # player walking

    if pygame.key.get_pressed()[K_a]:
        kirbyx -= 1
        if kirbyx < 0:
            kirbyx += 1

    if pygame.key.get_pressed()[K_d]:
        kirbyx += 1
        if kirbyx > 960:
            kirbyx -= 1

    # objects

    kirby = pygame.draw.circle(screen, 'PINK2', (kirbyx, kirbyy), 20)
    floor = pygame.draw.line(screen, 'WHITE', (0, 500), (960, 500), 5)
    if draw_coin:
        coin = pygame.draw.rect(screen, 'GOLD', (450, 480, 15, 15))
        if kirby.colliderect(coin):
            draw_coin = False
            points += 1
    if draw_potion:
        potion = pygame.draw.rect(screen, 'RED', (550, 480, 15, 15))
        if kirby.colliderect(potion):
            draw_potion = False
            life += 10

    # text

    screen.blit(text1, (750, 40))
    screen.blit(text2, (500, 40))
    pygame.display.update()
