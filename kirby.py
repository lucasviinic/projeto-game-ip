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
        self.rect = 100,100
        self.tela = tela
        self.__pos_x = x
        self.__pos_y = y
        self.__vida = vida_inicial

    def mover(self):
        self.rect = (self.__pos_x,self.__pos_y)

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
        self.image = pygame.transform.scale(self.image,(80,80))

    def update_right(self):

        if(self.index <= 6):
            self.index += 0.4

        else:
            self.index = 1
        
        self.image = self.sprites[round(self.index)]
        self.image = pygame.transform.scale(self.image,(80,80))

    def update_left(self):
        if(self.index <= 6):
            self.index += 0.4

        else:
            self.index = 1
        
        self.image = self.sprites[round(self.index)]
        self.image = pygame.transform.scale(self.image,(80,80))
        self.image = pygame.transform.flip(self.image,True,False)

    def on_floor(self,kirby_x,kirby_y,floor_x,floor_y):
        return floor_y - kirby_y 

    def get_pos(self):
        return self.rect

    def get_life(self):
        return self.__vida

    def damage(self,damage):
        self.__vida -= damage
        return self.__vida

    def colision(self,player_x, player_y,inimigo_x,inimigo_y):
        valor = int(math.sqrt(((inimigo_x-player_x)**2)+(inimigo_y-player_y)**2))
        return valor

    def teste(self,box_boxer):
        self.rect.colliderect(box_boxer)

