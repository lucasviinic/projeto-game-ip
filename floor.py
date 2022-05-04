import pygame

pygame.init()

class Floor(pygame.sprite.Sprite):
    
    def __init__(self,tela,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load(f"images/floor.png"))
        self.index = 0
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect = (100,100)
        self.tela = tela
        self.__pos_x = x
        self.__pos_y = y
        self.image = pygame.transform.scale(self.image,(200,100))

    def posicionar(self):
        self.rect = (self.__pos_x,self.__pos_y)
        self.image = self.sprites[int(self.index)]
        self.image = pygame.transform.scale(self.image,(200,100))

    def set_pos(self,x,y):
        self.__pos_x = x
        self.__pos_y = y
        