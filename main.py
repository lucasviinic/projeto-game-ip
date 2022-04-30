import pygame
from pygame.locals import *
from sys import exit


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, stage):
        super(Player, self).__init__()

        self.x = x
        self.y = y
        self.vel_x = 5
        self.vel_y = 5
        self.jumping = False
        self.scale = scale
        self.stage = stage
        self.images = []
        walk01 = pygame.image.load('images/walk01.png')
        walk01 = pygame.transform.scale(walk01, scale)
        walk02 = pygame.image.load('images/walk02.png')
        walk02 = pygame.transform.scale(walk02, scale)
        walk03 = pygame.image.load('images/walk03.png')
        walk03 = pygame.transform.scale(walk03, scale)
        walk04 = pygame.image.load('images/walk04.png')
        walk04 = pygame.transform.scale(walk04, scale)
        jump01 = pygame.image.load('images/jump01.png')
        jump01 = pygame.transform.scale(jump01, scale)
        jump02 = pygame.image.load('images/jump02.png')
        jump02 = pygame.transform.scale(jump02, scale)
        jump03 = pygame.image.load('images/jump03.png')
        jump03 = pygame.transform.scale(jump03, scale)
        jump04 = pygame.image.load('images/jump04.png')
        jump04 = pygame.transform.scale(jump04, scale)

        self.images.append(walk01)
        self.images.append(walk02)
        self.images.append(walk03)
        self.images.append(walk04)
        self.images.append(jump01)
        self.images.append(jump02)
        self.images.append(jump03)
        self.images.append(jump04)

        self.index = 0

        self.image = self.images[self.index]

        self.index = 0

        self.image = self.images[self.index]

        self.rect = pygame.Rect(x, y, scale[0], scale[1])

    def move(self, direction):
        if direction == 'right':
            self.index += 1

            if self.index > 1:
                self.index = 0

            self.image = self.images[self.index]
            self.rect[0] += self.vel_x
            if self.rect[0] > 930:
                self.rect[0] = 0
        if direction == 'left':
            self.index += 1

            if self.index > 3:
                self.index = 2

            self.image = self.images[self.index]
            self.rect[0] -= self.vel_x
            if self.rect[0] < 0:
                self.rect[0] += self.vel_x

    def jump(self):
        self.jumping = True

    def collision(self):
        return self.rect

    def update(self, side):
        if self.jumping:
            if side == 'left':
                self.image = self.images[6]
            else:
                self.image = self.images[4]
            if self.rect[1] <= 370:
                self.jumping = False
                if side == 'left':
                    self.image = self.images[7]
                else:
                    self.image = self.images[5]
            self.rect[1] -= 10
        else:
            if self.rect[1] < self.y:
                self.rect[1] += self.vel_y
            else:
                self.rect[1] = self.y


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

kirby = Player(50, 555, (50, 60), 0)
kirby_group = pygame.sprite.Group()
looking = 'right'
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
    kirby.update(looking)
    kirby_group.draw(screen)
    score = f'Points: {points}'
    life_points = f'Life: {life}/100'
    text1 = font.render(score, True, 'BLACK')
    text2 = font.render(life_points, True, 'RED')
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # player movement

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                kirby.jump()

    if pygame.key.get_pressed()[K_a]:
        kirby.move('left')
        looking = 'left'

    if pygame.key.get_pressed()[K_d]:
        kirby.move('right')
        looking = 'right'

    # objects

    if draw_coin:
        coin = pygame.draw.rect(screen, 'GOLD', (450, 590, 15, 15))
        if kirby.collision().colliderect(coin):
            draw_coin = False
            points += 1
    if draw_potion:
        potion = pygame.draw.rect(screen, 'RED', (550, 590, 15, 15))
        if kirby.collision().colliderect(potion):
            draw_potion = False
            life += 10
            if life > 100:
                life = 100

    if kirby.collision()[0] > 925:
        draw_coin = True
        draw_potion = True

    # text

    screen.blit(text1, (750, 40))
    screen.blit(text2, (475, 40))
    pygame.display.update()