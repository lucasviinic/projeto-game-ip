import pygame
from pygame.locals import *
from sys import exit


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()

        self.images = []
        walk01 = pygame.image.load('images/walk01.png')
        walk01 = pygame.transform.scale(walk01, (50, 60))
        walk02 = pygame.image.load('images/walk02.png')
        walk02 = pygame.transform.scale(walk02, (50, 60))
        walk03 = pygame.image.load('images/walk03.png')
        walk03 = pygame.transform.scale(walk03, (50, 60))
        walk04 = pygame.image.load('images/walk04.png')
        walk04 = pygame.transform.scale(walk04, (50, 60))

        self.images.append(walk01)
        self.images.append(walk02)
        self.images.append(walk03)
        self.images.append(walk04)

        self.index = 0

        self.image = self.images[self.index]

        self.index = 0

        self.image = self.images[self.index]

        self.rect = pygame.Rect(50, 565, 50, 60)

    def move(self, direction):
        if direction == 'right':
            self.index += 1

            if self.index > 1:
                self.index = 0

            self.image = self.images[self.index]
            self.rect[0] += 3
            if self.rect[0] > 930:
                self.rect[0] -= 3

        if direction == 'left':
            self.index += 1

            if self.index > 3:
                self.index = 2

            self.image = self.images[self.index]
            self.rect[0] -= 3
            if self.rect[0] < 0:
                self.rect[0] += 3

    def collision(self):
        return self.rect


pygame.init()

# screen info


width = 960
height = 720
screen = pygame.display.set_mode((width, height))
background = pygame.image.load('images/background.png')
background = pygame.transform.scale(background, (width, height))
pygame.display.set_caption('Kirby')
font = pygame.font.SysFont('Akziden Ghost', 50, True, False)
clock = pygame.time.Clock()

# player info

kirby = Player()
kirby_group = pygame.sprite.Group()
kirby_group.add(kirby)
points = 0
life = 50

# collectables info

draw_coin = True
draw_potion = True

# game loop

while True:
    clock.tick(200)
    screen.fill('BLACK')
    screen.blit(background, (0, 0))
    kirby_group.update()
    kb = kirby_group.draw(screen)
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
        kirby.move('left')

    if pygame.key.get_pressed()[K_d]:
        kirby.move('right')

    # objects

    if draw_coin:
        coin = pygame.draw.rect(screen, 'GOLD', (450, 590, 15, 15))
        print(kirby.collision())
        if kirby.collision().colliderect(coin):
            draw_coin = False
            points += 1
    if draw_potion:
        potion = pygame.draw.rect(screen, 'RED', (550, 590, 15, 15))
        if kirby.collision().colliderect(potion):
            draw_potion = False
            life += 10

    # text

    screen.blit(text1, (750, 40))
    screen.blit(text2, (500, 40))
    pygame.display.update()

