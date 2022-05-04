import pygame

pygame.init()


class Inimigo(pygame.sprite.Sprite):
    
    def __init__(self,tela,x,y,vida_inicial):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        for i in range(1,6):
            self.sprites.append(pygame.image.load(f"images/boxboxer/andando_{i}.png"))

        self.index = 0
        self.image = self.sprites[0]
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
    
    def set_vida(self,dano):
        self.__vida -= dano

    def get_vida(self):
        return int(self.__vida)

    def update(self):
        if(self.index <= 4):
            self.index += 0.2

        else:
            self.index = 1
        
        self.image = self.sprites[round(self.index)]
        self.image = pygame.transform.scale(self.image,(80,80))

    def inverter(self,crescer):
        if(crescer == False):
            self.image = pygame.transform.flip(self.image,True,False)

    def get_pos(self):
        return self.rect

    
    
    

        