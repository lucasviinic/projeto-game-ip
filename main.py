from ast import walk
import pygame
from pygame.locals import *
from sys import exit
from kirby import Kirby
from floor import Floor
from inimigo01 import Inimigo
from misc import Coin
from misc import Cherry

pygame.init()

# screen info

gravidade = 0.25  # VALOR INICIAL DA GRAVIDADE
gravidade_reversa = -0.25
width = 960
height = 720
acel_y = 0  # VALOR INICIAL DA ACERELAÇÃO NO EIXO Y(ALTURA)

# CONFIGURAÇÕES GERAIS============================================================================================

screen = pygame.display.set_mode((width, height))
background = pygame.image.load('images/background.png')
background = pygame.transform.scale(background, (width, height))
pygame.display.set_caption('Kirby')
font = pygame.font.SysFont('Akziden Ghost', 50, True, False)
clock = pygame.time.Clock()

# KIRBY INFORMAÇÕES============================================================================================

kirby_x = 80
kirby_y = 540
parado = True

kirby = Kirby(screen, 50, 400, 100)

# FIM=================================================================================================

# INSTÂNCIAS DO CHÃO=======================================================================================
floor = Floor(screen, 0, 900)
floor2 = Floor(screen, 0, 900)
floor3 = Floor(screen, 0, 900)
floor4 = Floor(screen, 0, 900)
floor5 = Floor(screen, 0, 900)
floor6 = Floor(screen, 0, 900)
# FIM====================================================================================================================


# INIMIGOS====================================================================================================================

box_boxer = Inimigo(screen, 10, 10, 100)
box_boxer_x = 550
box_boxer_y = 900
moves = 0

# OBJETOS===================================================================================

moeda1 = Coin(540, 500)
moeda2 = Coin(540, 850)
cereja1 = Cherry(540, 700)

# FIM====================================================================================================================


# SPRITES
walk_kirby = pygame.sprite.Group()
walk_kirby.add(kirby)

walk_enemy = pygame.sprite.Group()
walk_enemy.add(box_boxer)

floor_group = pygame.sprite.Group()
floor_group.add(floor)
floor2_group = pygame.sprite.Group()
floor2_group.add(floor2)
floor3_group = pygame.sprite.Group()
floor3_group.add(floor3)
floor4_group = pygame.sprite.Group()
floor4_group.add(floor5)
floor5_group = pygame.sprite.Group()
floor5_group.add(floor5)
floor6_group = pygame.sprite.Group()
floor6_group.add(floor6)

moedas_group = pygame.sprite.Group()
moedas_group.add(moeda1)
moedas_group.add(moeda2)
cerejas_group = pygame.sprite.Group()
cerejas_group.add(cereja1)

# SPRITES

# collectables info

draw_coin1 = True
draw_coin2 = True
draw_cherry1 = True
jumping = False
points = 0

# game loop

while True:
    # CONFIGAÇÕES========================================================================================
    clock.tick(120)  # FPS
    screen.fill('BLACK')
    screen.blit(background, (0, 0))
    score = f'Points: {points}'
    life_points = f'Life: {kirby.get_life()}/100'
    text1 = font.render(score, True, 'BLACK')
    text2 = font.render(life_points, True, 'RED')
    parado = True  # SETA O PERSONAGEM COMO PARADO

    t = clock.get_time()  # COLETA O TEMPO DECORRIDO
    acel_y = gravidade * t  # GERA ACERELAÇÃO DA GRAVIDADE
    acel_pulo = gravidade_reversa * t

    if not jumping:
        kirby_y += acel_y

    if kirby_y > 526:  # DEFINE O CHÃO
        kirby_y = 526
        acel_y = 0

    if box_boxer_y < 534.0000000000001:  # DEFINE O CHÃO
        box_boxer_y += acel_y
    else:
        box_boxer_y = 534.0000000000001

    # fim===============================================================================================
    if jumping:
        if 526 >= kirby_y >= 300:
            acel_y = 0
            kirby_y -= 10
            if kirby_y <= 300:
                jumping = False

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        # MOVIMENTA O PERSONAGEM==================================================================================

        if event.type == KEYDOWN:
            if event.key == K_a:
                kirby_x -= 3
                if kirby_x < 0:
                    kirby_x += 3
                kirby.update_left()
                parado = False

            if event.key == K_d:
                kirby_x += 3
                if kirby_x > 930:
                    kirby_x = 0
                kirby.update_right()
                parado = False

            if event.key == K_SPACE:
                jumping = True

    if pygame.key.get_pressed()[K_a]:
        kirby_x -= 4
        if kirby_x < 0:
            kirby_x += 4
        kirby.update_left()
        parado = False
    if pygame.key.get_pressed()[K_d]:
        kirby_x += 4
        if kirby_x > 930:
            kirby_x = 0
            cerejas_group.add(cereja1)
            moedas_group.add(moeda1)
            moedas_group.add(moeda2)
            draw_coin1 = True
            draw_coin2 = True
            draw_cherry1 = True
        kirby.update_right()
        parado = False

    if parado:
        kirby.stopped()

    # FIM===============================================================================================

    # POSICIONA O CHÃO==================================================================================

    floor.set_pos(0, 605)
    floor.posicionar()
    floor2.set_pos(200, 605)
    floor2.posicionar()
    floor3.set_pos(400, 605)
    floor3.posicionar()
    floor4.set_pos(600, 605)
    floor4.posicionar()
    floor5.set_pos(600, 605)
    floor5.posicionar()
    floor6.set_pos(800, 605)
    floor6.posicionar()

    # FIM==================================================================================
    k_x = kirby.get_pos_x()
    k_y = kirby.get_pos_y()
    i_x = box_boxer.get_pos_x()
    i_y = int(box_boxer.get_pos_y())

    if kirby.colision(k_x, k_y, i_x, i_y) <= 80:
        if k_x < i_x:
            kirby_x = k_x - 20
        else:
            kirby_x = k_x + 20
        kirby.damage(10)

    if draw_coin1:
        if kirby.colision_coin(kirby.rect, moeda1.rect):
            moedas_group.remove(moeda1)
            draw_coin1 = False
            points += 1

    if draw_coin2:
        if kirby.colision_coin(kirby.rect, moeda2.rect):
            moedas_group.remove(moeda2)
            draw_coin2 = False
            points += 1

    if draw_cherry1:
        if kirby.colision_coin(kirby.rect, cereja1.rect):
            draw_cherry1 = False
            kirby.set_life(10)

    if kirby.get_life() > 0:
        kirby.set_pos(kirby_x, kirby_y)
        kirby.mover()
        walk_kirby.draw(screen)
    else:
        kirby.set_life(0)

    box_boxer.set_pos(box_boxer_x, box_boxer_y)
    box_boxer.mover()
    box_boxer.update()
    moeda1.update()
    moeda2.update()

    if moves <= 0:
        direita = True

    if moves >= 140:
        direita = False

    if direita:
        moves += 1
        box_boxer_x += 2

    else:
        moves -= 1
        box_boxer.inverter(direita)
        box_boxer_x -= 2

    # DESENHA chão====================================================================================

    floor_group.draw(screen)
    floor2_group.draw(screen)
    floor3_group.draw(screen)
    floor4_group.draw(screen)
    floor5_group.draw(screen)
    floor6_group.draw(screen)
    walk_enemy.draw(screen)
    if draw_coin1 or draw_coin2:
        moedas_group.draw(screen)
    if draw_cherry1:
        cerejas_group.draw(screen)

    # FIM==================================================================================

    screen.blit(text1, (750, 40))
    screen.blit(text2, (475, 40))
    pygame.display.flip()
