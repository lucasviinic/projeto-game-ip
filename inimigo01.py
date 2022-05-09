import pygame

pygame.init()


class Inimigo(pygame.sprite.Sprite):
    
    def __init__(self,tela,x,y,vida_inicial):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        for i in range(1,6):
            self.sprites.append(pygame.image.load(f"images/boxboxer/andando_{i}.png"))

        self.__index = 0
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect = 100,100
        self.tela = tela
        self.__pos_x = x
        self.__pos_y = y
        self.__vida = vida_inicial
        self.__direction = True

    def mover(self):
        self.rect = (self.__pos_x,self.__pos_y)

    def get_pos_x(self):
        return int(self.__pos_x)

    def get_pos_y(self):
        return int(self.__pos_y)

    def set_pos(self,x,y):
        self.__pos_x = x
        self.__pos_y = y
    
    def set_vida(self,dano):
        self.__vida -= dano

    def get_vida(self):
        return int(self.__vida)

    def update(self):
        if(self.__index <= 4):
            self.__index += 0.1

        else:
            self.__index = 1
        
        self.image = self.sprites[round(self.__index)]
        self.image = pygame.transform.scale(self.image,(80,80))

    def inverter(self):
        self.image = pygame.transform.flip(self.image, True, False)


    def get_pos(self):
        return self.rect

    def get_direction(self):
        return self.__direction

    def set_direction(self,boolean):
        self.__direction = boolean

    def get_pos_x(self):
        return int(self.__pos_x)

    def get_pos_y(self):
        return int(self.__pos_y)

    def set_pos_x(self, x):
        self.__pos_x = x


    def set_pos_y(self, y):
        self.__pos_y = y

    def set_index(self, index):
        self.__index = index
    
    
    

        