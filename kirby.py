from webbrowser import get
import pygame
from pygame.locals import *
import math
from floor import Floor
from inimigo01 import Inimigo


class Kirby(pygame.sprite.Sprite):

    def __init__(self,tela,x,y,vida_inicial):
        pygame.sprite.Sprite.__init__(self)

        self.sprites = []

        self.sprites.append(pygame.image.load(f"images/kirby/stopped.png"))
        for i in range(2,9):
            self.sprites.append(pygame.image.load(f"images/kirby/walk{i}.png"))
        
        self.index = 0
        self.image = self.sprites[self.index]
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(x, y, 80, 80)
        self.tela = tela
        self.__pos_x = x
        self.__pos_y = y
        self.__vida = vida_inicial
        self.jumping = False

    def mover(self):
        self.rect[0] = self.__pos_x
        self.rect[1] = self.__pos_y

    def get_pos_x(self):
        return int(self.__pos_x)

    def get_pos_y(self):
        return int(self.__pos_y)

    def set_pos(self,x,y):
        self.__pos_x = x
        self.__pos_y = y

    def stopped(self):
        self.index = 0
        self.image = self.sprites[int(self.index)]
        self.image = pygame.transform.scale(self.image, (80, 80))

    def update_right(self):

        if self.index <= 6:
            self.index += 0.4

        else:
            self.index = 1
        
        self.image = self.sprites[round(self.index)]
        self.image = pygame.transform.scale(self.image,(80,80))

    def update_left(self):
        if self.index <= 6:
            self.index += 0.4

        else:
            self.index = 1
        
        self.image = self.sprites[round(self.index)]
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.image = pygame.transform.flip(self.image, True, False)

    def on_floor(self, kirby_x, kirby_y, floor_x, floor_y):
        return floor_y - kirby_y 

    def get_pos(self):
        return self.rect

    def get_life(self):
        return self.__vida

    def set_life(self, life):
        self.__vida += life
        if self.__vida >= 100:
            self.__vida = 100
        if self.__vida <= 0:
            self.__vida = 0

    def damage(self,damage):
        self.__vida -= damage
        return self.__vida

    def colision(self,player_x, player_y,inimigo_x,inimigo_y):
        valor = int(math.sqrt(((inimigo_x-player_x)**2)+(inimigo_y-player_y)**2))
        return valor

    def colision_coin(self, k_rect, c_rect):
        return k_rect.colliderect(c_rect)

    def colision_cherry(self, k_rect, c_rect):
        return k_rect.colliderect(c_rect)



