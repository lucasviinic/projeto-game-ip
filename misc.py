import pygame


class Cherry(pygame.sprite.Sprite):
    def __init__(self, altura, largura):
        pygame.sprite.Sprite.__init__(self)  # Pra usar o Sprite
        self.altura = altura
        self.largura = largura
        cereja1 = pygame.image.load('images/miscellanous/Cereja.png')
        cereja1 = pygame.transform.scale(cereja1, (50, 60))
        self.rect = pygame.Rect(largura, altura, 50, 60)
        self.image = cereja1


class Coin(pygame.sprite.Sprite):
    def __init__(self, altura, largura):
        pygame.sprite.Sprite.__init__(self)  # Pra usar o Sprite
        self.altura = altura
        self.largura = largura
        self.sprites = []
        for i in range(1, 12):
            img = pygame.image.load(f"images/miscellanous/img{i}.png")
            img = pygame.transform.scale(img, (50, 60))
            self.sprites.append(img)

        self.rect = pygame.Rect(largura, altura, 50, 60)
        self.index = 0
        self.image = self.sprites[0]
        self.contador = 0

    def update(self):
        self.contador += 1
        if self.contador == 5:
            self.index += 1
            self.image = self.sprites[self.index]
            if self.index >= 10:
                self.index = 0
            self.contador = 0
