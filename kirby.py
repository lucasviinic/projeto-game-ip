from webbrowser import get
import pygame
from pygame.locals import *
import math
from floor import Floor
from inimigo01 import Inimigo

#DESCRIÇÃO SOBRE AS FUNÇÕES

#MOVE(): altera a posição do kirby
#qualquer função "set()": altera alguma caracterisca do kirby
#qualquer função "get()": coleca o valor de alguma informação do kirby
#inverse(): inverte o lado do sprite
#updates(): alteram os sprites para determinada situação
#funções do tipo "colision()": detecta alguma colisão entre o kirby e algum objeto




class Kirby(pygame.sprite.Sprite):

    def __init__(self,tela,x,y,vida_inicial):
        pygame.sprite.Sprite.__init__(self)

        self.sprites = []

        self.sprites.append(pygame.image.load(f"images/kirby/stopped.png"))
        for i in range(2,9):
            self.sprites.append(pygame.image.load(f"images/kirby/walk{i}.png"))

        self.sprites.append(pygame.image.load(f"images/kirby/jump.png"))

        for i in range(1,3):
            self.sprites.append(pygame.image.load(f"images/kirby/fall{i}.png"))

        self.sprites.append(pygame.image.load(f"images/kirby/hited.png"))

        for i in range(1,10):
            self.sprites.append(pygame.image.load(f"images/kirby/atk{i}.png"))

        for i in range(1,8):
            self.sprites.append(pygame.image.load(f"images/kirby/run{i}.png"))
            
        self.__index = 0
        self.image = self.sprites[self.__index]
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(x, y, 80, 80)
        self.__tela = tela
        self.__pos_x = x
        self.__pos_y = y
        self.__vida = vida_inicial
        self.__direction = True
        self.__run = False

    def mover(self):
        self.rect[0] = self.__pos_x
        self.rect[1] = self.__pos_y

    def get_pos_x(self):
        return int(self.__pos_x)

    def get_pos_y(self):
        return int(self.__pos_y)

    def set_pos(self, x, y):
        self.__pos_x = x
        self.__pos_y = y

    def stopped(self):
        self.__index = 0
        self.image = self.sprites[int(self.__index)]
        self.image = pygame.transform.scale(self.image, (80, 80))
        if(self.get_direction() == False):
            self.inverse()
            

    def update_right(self):

        if self.__index <= 6:
            self.__index += 0.4

        else:
            self.__index = 1
        
        self.image = self.sprites[round(self.__index)]
        self.image = pygame.transform.scale(self.image,(80,80))

    def update_left(self):
        if self.__index <= 6:
            self.__index += 0.4

        else:
            self.__index = 1
        
        self.image = self.sprites[round(self.__index)]
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.inverse()

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

    def update_jump(self):
        self.__index = 8
        self.image = self.sprites[round(self.__index)]
        self.image = pygame.transform.scale(self.image, (80, 80))

        if(self.get_direction() == False):
            self.inverse()

    def update_fall(self):
        if(self.__index <=8):
            self.__index = 9
        elif(self.__index >= 10):
            self.__index = 9 
        self.image = self.sprites[round(self.__index)]
        self.image = pygame.transform.scale(self.image, (80, 80))
        if(self.get_direction() == False):
            self.inverse()

    def inverse(self):
        self.image = pygame.transform.flip(self.image, True, False)

    def get_direction(self):
        return self.__direction

    def set_direction(self,boolean):
        self.__direction = boolean

    def update_hited(self):
        self.__index = 11
        self.image = self.sprites[round(self.__index)]
        self.image = pygame.transform.scale(self.image, (80, 80))
        if(self.get_direction() == False):
            self.inverse()

    def update_basic_atk(self):
        if int(self.__index )== 19:
            self.__index = 17

        elif self.__index < 21 and self.__index >= 13 and self.__index < 17:
            self.__index += 0.3


        elif self.__index < 21 and self.__index >= 17:
            self.__index += 0.065


        elif(self.__index <13):
            self.__index = 13

        self.image = self.sprites[int(self.__index)]
        self.image = pygame.transform.scale(self.image, (80, 80))          
        if(self.get_direction() == False):
            self.inverse()


    def set_index(self, index):
        self.__index = index

    def get_index(self):
        return self.__index

    def update_run(self):
        if int(self.__index )== 26:
            self.__index = 21

        elif self.__index < 26 and self.__index >= 21:
            self.__index += 0.3


        elif(self.__index <21):
            self.__index = 21


        self.image = self.sprites[round(self.__index)]
        self.image = pygame.transform.scale(self.image, (80, 80))
        if(self.get_direction() == False):
            self.inverse()

    def get_run(self):
        return self.__run

    def set_run(self,status):
        self.__run = status