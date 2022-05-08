import time
from sys import exit

import pygame
from pygame.locals import *

from floor import Floor
from floor import Floor2
from inimigo01 import Inimigo
from kirby import Kirby
from misc import Cherry
from misc import Coin

pygame.init()

# screen infoS

gravidade = 0.04  # VALOR INICIAL DA GRAVIDADE
width = 960
height = 720
F = 0  # VALOR INICIAL DA ACERELAÇÃO NO EIXO Y(ALTURA)


# CONFIGURAÇÕES GERAIS============================================================================================

screen = pygame.display.set_mode((width, height))
background = pygame.image.load('images/background.png')
background = pygame.transform.scale(background, (width, height))
background2 = pygame.image.load('images/background2.png')
background2 = pygame.transform.scale(background2, (width, height))
pygame.display.set_caption('Kirby')
font = pygame.font.SysFont('Akziden Ghost', 50, True, False)
clock = pygame.time.Clock()
tempo_inicial = time.time()
time_hit = time.time()
variacao_tempo = 0

# KIRBY INFORMAÇÕES============================================================================================

kirby_x = 80
kirby_y = 540
kirby = Kirby(screen, 80, 700, 100)


# FIM=================================================================================================

# INSTÂNCIAS DO CHÃO=======================================================================================
floor = Floor(screen, 0, 900)
floor2 = Floor(screen, 0, 900)
floor3 = Floor(screen, 0, 900)
floor4 = Floor(screen, 0, 900)
floor5 = Floor(screen, 0, 900)
floor6 = Floor(screen, 0, 900)

floor7 = Floor2(screen, 0, 900)
floor8 = Floor2(screen, 0, 900)
floor9 = Floor2(screen, 0, 900)
floor10 = Floor2(screen, 0, 900)
floor11 = Floor2(screen, 0, 900)
floor12 = Floor2(screen, 0, 900)
# FIM====================================================================================================================


# INIMIGOS====================================================================================================================

box_boxer = Inimigo(screen, 10, 10, 100)
box_boxer_x = 550
box_boxer_y = 900
moves = 0
box_boxer_colision = False
coeficiente_distancia = 1
coeficente_dano = 1
acel_x_1 = 1
acel_x_2 = 1

# OBJETOS===================================================================================

moeda1 = Coin(540, 500)
moeda2 = Coin(540, 850)
moeda3 = Coin(540, 700)
cereja1 = Cherry(540, 700)
cereja2 = Cherry(540, 400)

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
floor7_group = pygame.sprite.Group()
floor7_group.add(floor7)
floor8_group = pygame.sprite.Group()
floor8_group.add(floor8)
floor9_group = pygame.sprite.Group()
floor9_group.add(floor9)
floor10_group = pygame.sprite.Group()
floor10_group.add(floor10)
floor11_group = pygame.sprite.Group()
floor11_group.add(floor11)
floor12_group = pygame.sprite.Group()
floor12_group.add(floor12)

moedas_group = pygame.sprite.Group()
moedas_group.add(moeda1)
moedas_group.add(moeda2)
cerejas_group = pygame.sprite.Group()
cerejas_group.add(cereja1)

# SPRITES

# collectables info

draw_coin1 = True
draw_coin2 = True
draw_coin3 = True
draw_cherry1 = True
draw_cherry2 = True
points = 0
acel_y = 0
stage = 1

# game loop

while True:
    # CONFIGAÇÕES========================================================================================
    clock.tick(60)  # FPS
    screen.fill('BLACK')
    if stage < 5:
        screen.blit(background, (0, 0))
    else:
        screen.blit(background2, (0, 0))
    score = f'Points: {points}'
    life_points = f'Life: {kirby.get_life()}/100'
    text1 = font.render(score, True, 'BLACK')
    text2 = font.render(life_points, True, 'RED')
    if(acel_y == 0):
        kirby.set_stopped(True)

    else:
        kirby.set_fall(True)
    atacando = False

    time_game = clock.get_time()  # COLETA O TEMPO DECORRIDO
    F = gravidade * time_game  # GERA ACERELAÇÃO DA GRAVIDADE
    acel_y += F 
    tempo_final = time.time()
    variacao_tempo = tempo_final - tempo_inicial
    tempo_inicial = tempo_final

    if (tempo_inicial - time_hit) >= 0.1 and box_boxer_colision == True:
        box_boxer_colision = False
 
    kirby.set_pos_y(kirby.get_pos_y() + acel_y) 

    if kirby.get_pos_y() >= 526:  # DEFINE O CHÃO
        kirby.set_pos_y(526) 
        kirby.set_fall(False)
        acel_y = 0
        time_game = pygame.time.Clock()
 
    if box_boxer_y < 534.0000000000001:  # DEFINE O CHÃO
        box_boxer_y += F
    else:
        box_boxer_y = 534.0000000000001


    # fim===============================================================================================
    if kirby.get_jump() == True:
        acel_y -= 20
        kirby.set_fall(False)
        kirby.update_jump()
        if acel_y <= 0 and kirby.get_jump() == True:
            kirby.set_jump(False)
            kirby.set_fall(True)
            kirby.set_pos_y(kirby.get_pos_y() + acel_y)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            

        # MOVIMENTA O PERSONAGEM==================================================================================

        if event.type == KEYDOWN and box_boxer_colision == False:
            if(event.key == K_w):
                if(kirby.get_run() == False):
                    kirby.set_run(True)

                else:
                    kirby.set_run(False)

            if event.key == K_a:
                kirby.set_pos_x(kirby.get_pos_x()-(220* variacao_tempo))

                if(kirby.get_jump() == True):
                    kirby.update_jump()
                else:
                    kirby.update_left()

                kirby.set_direction(False)
                kirby.set_stopped(False)

            if event.key == K_d and box_boxer_colision == False:
                    
                kirby.set_pos_x(kirby.get_pos_x()+(220* variacao_tempo))

                if(kirby.get_jump() == True):
                    kirby.update_jump()
                else:
                    kirby.update_right()

                kirby.set_direction(True)
                kirby.set_stopped(False)

            if event.key == K_SPACE:
                if kirby.get_pos_y() == 526:
                    kirby.set_jump(True)
                    print(kirby.get_jump())

    if kirby.get_pos_x() < 0:
        kirby.set_pos_x(10)

    if pygame.key.get_pressed()[K_r] and box_boxer_colision == False and pygame.key.get_pressed()[K_a] == False and pygame.key.get_pressed()[K_d] == False and pygame.key.get_pressed()[K_SPACE] == False:
        atacando = True
        kirby.set_stopped(True)


    if pygame.key.get_pressed()[K_a] and box_boxer_colision == False and pygame.key.get_pressed()[K_d] == False and pygame.key.get_pressed()[K_r] == False:
        kirby.set_stopped(False)
        kirby.set_direction(False)
        
        if(kirby.get_jump() == True):
            kirby.update_jump()
            kirby.set_pos_x(kirby.get_pos_x()-(400* variacao_tempo))

        elif(kirby.get_jump() == False):
            if(kirby.get_run()== False):
                kirby.update_left()
                kirby.set_pos_x(kirby.get_pos_x()-(240* variacao_tempo))
            else:
                kirby.set_pos_x(kirby.get_pos_x()-(390* variacao_tempo))
                kirby.update_run()

        kirby.set_stopped(False)
        
    if pygame.key.get_pressed()[K_d] and box_boxer_colision == False and pygame.key.get_pressed()[K_a] == False and pygame.key.get_pressed()[K_r] == False:
        kirby.set_direction(True)
        kirby.set_stopped(False)
        
        if(kirby.get_jump() == True):
            kirby.update_jump()
            kirby.set_pos_x(kirby.get_pos_x()+(400* variacao_tempo))

        elif(kirby.get_jump() == False):
            if(kirby.get_run()== False):
                kirby.update_right()
                kirby.set_pos_x(kirby.get_pos_x()+(240* variacao_tempo))
            else:
                kirby.set_pos_x(kirby.get_pos_x()+(390* variacao_tempo))
                kirby.update_run()

        if kirby.get_pos_x() > 930:
            stage += 1
            kirby.set_pos_x(0)
            cerejas_group.add(cereja1)
            moedas_group.add(moeda1)
            moedas_group.add(moeda2)
            draw_coin1 = True
            draw_coin2 = True
            draw_cherry1 = True
            if stage == 4 or stage == 6:
                draw_coin3 = True
                moedas_group.add(moeda3)
                draw_cherry1 = False
            if stage == 5 or stage == 7:
                draw_cherry2 = True
                cerejas_group.add(cereja2)
                draw_coin1, draw_coin2, draw_coin3 = False, False, False
            if box_boxer.get_vida() <= 0:
                box_boxer.set_vida(-100)

        kirby.set_stopped(False)

    if kirby.get_stopped() == True and kirby.get_jump() == False and kirby.get_fall() == False and atacando == False and box_boxer_colision == False:
        kirby.stopped()

    elif kirby.get_jump() == True and box_boxer_colision == False and kirby.get_fall() == False:
        kirby.update_jump()

    elif kirby.get_jump() == False and kirby.get_fall() == True and box_boxer_colision == False and kirby.get_stopped() == False:
        kirby.update_jump()

    elif kirby.get_stopped() == True and kirby.get_jump() == True and kirby.get_fall() == False and box_boxer_colision == False:
        kirby.update_jump()

    elif kirby.get_stopped() and kirby.get_jump() == False and kirby.get_fall() == False and atacando == True and box_boxer_colision == False:
        
        kirby.update_basic_atk()
            
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
    floor7.set_pos(0, 605)
    floor7.posicionar()
    floor8.set_pos(200, 605)
    floor8.posicionar()
    floor9.set_pos(400, 605)
    floor9.posicionar()
    floor10.set_pos(600, 605)
    floor10.posicionar()
    floor11.set_pos(600, 605)
    floor11.posicionar()
    floor12.set_pos(800, 605)
    floor12.posicionar()

    # FIM========================================================================================

    if kirby.colision (kirby.get_pos_x(), kirby.get_pos_y(), box_boxer.get_pos_x(), box_boxer.get_pos_y()) <= 80 and atacando == False and box_boxer.get_vida() > 0 and kirby.get_life() > 0:

        if kirby.get_pos_x() < box_boxer.get_pos_x():
            kirby_x = kirby.get_pos_x() - 1000*variacao_tempo
            box_boxer_x += 1500*variacao_tempo
        else:
            kirby_x = kirby.get_pos_x() + 1000*variacao_tempo
            box_boxer_x -= 1500*variacao_tempo

        time_hit = time.time()
        
        box_boxer_colision = True
        kirby.update_hited()
        kirby.damage(int(1*box_boxer_x*variacao_tempo*coeficente_dano))
        
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

    if draw_coin3:
        if kirby.colision_coin(kirby.rect, moeda3.rect):
            moedas_group.remove(moeda3)
            draw_coin3 = False
            points += 1

    if draw_cherry1:
        if kirby.colision_coin(kirby.rect, cereja1.rect):
            cerejas_group.remove(cereja1)
            draw_cherry1 = False
            kirby.set_life(10)

    if draw_cherry2:
        if kirby.colision_coin(kirby.rect, cereja2.rect):
            cerejas_group.remove(cereja2)
            draw_cherry2 = False
            kirby.set_life(10)

    if kirby.get_life() > 0:
        kirby.set_pos(kirby.get_pos_x(), kirby.get_pos_y())
        kirby.mover()
        walk_kirby.draw(screen)

        if kirby.colision (kirby.get_pos_x(), kirby.get_pos_y(), box_boxer.get_pos_x(), box_boxer.get_pos_y()) <= 170 and kirby.get_index() >= 17 and kirby.get_index() <= 21 and  kirby.get_life() > 0 and box_boxer.get_vida() > 0 and kirby.get_stopped() == True:

            if kirby.get_pos_x() < box_boxer.get_pos_x() and kirby.get_direction() == True:
                box_boxer_x -= 10

                if kirby.colision (kirby.get_pos_x(), kirby.get_pos_y(), box_boxer.get_pos_x(), box_boxer.get_pos_y()) <= 80 and atacando == True and kirby.get_direction() == True:
                    box_boxer.set_vida(box_boxer.get_vida())

            elif kirby.get_pos_x() > box_boxer.get_pos_x() and kirby.get_direction() == False:
                box_boxer_x += 10

                if kirby.colision (kirby.get_pos_x(), kirby.get_pos_y(), box_boxer.get_pos_x(), box_boxer.get_pos_y()) <= 80 and atacando == True and kirby.get_direction() == False:
                    box_boxer.set_vida(box_boxer.get_vida())

            elif kirby.get_pos_x() < box_boxer.get_pos_x() and kirby.get_direction() == False and kirby.colision (kirby.get_pos_x(), kirby.get_pos_y(), box_boxer.get_pos_x(), box_boxer.get_pos_y()) <= 80:
                kirby_x = kirby.get_pos_x() - 1000*variacao_tempo
                box_boxer_x += 1500*variacao_tempo
                time_hit = time.time()
                box_boxer_colision = True
                kirby.update_hited()
                kirby.damage(int(1*box_boxer_x*variacao_tempo*coeficente_dano))

            elif kirby.get_pos_x() > box_boxer.get_pos_x() and kirby.get_direction() == True and kirby.colision (kirby.get_pos_x(), kirby.get_pos_y(), box_boxer.get_pos_x(), box_boxer.get_pos_y()) <= 80:
                kirby_x = kirby.get_pos_x() + 1000*variacao_tempo
                box_boxer_x -= 1500*variacao_tempo
                time_hit = time.time()
                box_boxer_colision = True
                kirby.update_hited()
                kirby.damage(int(1*box_boxer_x*variacao_tempo*coeficente_dano))
    else:
        kirby.set_life(0)

    moeda1.update()
    moeda2.update()
    moeda3.update()

    if(box_boxer.get_vida() > 0):

        box_boxer.set_pos(box_boxer_x, box_boxer_y)
        box_boxer.mover()

        if box_boxer_colision == False:
            box_boxer.update()

        if (kirby.get_direction() == True and box_boxer.get_direction()== False) and kirby.colision (kirby.get_pos_x(), kirby.get_pos_y(), box_boxer.get_pos_x(), box_boxer.get_pos_y()) <= 200 and kirby.get_pos_x() < box_boxer.get_pos_x():
            acel_x_1 = 1.7 + (stage * 0.2)
            coeficiente_distancia = 1.2
            coeficente_dano = 3

        elif (kirby.get_direction() == False and box_boxer.get_direction()== True) and kirby.colision (kirby.get_pos_x(), kirby.get_pos_y(), box_boxer.get_pos_x(), box_boxer.get_pos_y()) <= 200 and kirby.get_pos_x() > box_boxer.get_pos_x():
            acel_x_2 = 1.7 + (stage * 0.2)
            coeficiente_distancia = 1.2
            coeficente_dano = 3

        if box_boxer_x <= 0:
            moves = 0

        if box_boxer_x >= 920:
            moves = 140*coeficiente_distancia

        if moves <= 0:
            direita = True

        if moves >= 140*coeficiente_distancia:
            direita = False
            coeficiente_distancia = 1
            acel_x_1 = 1
            acel_x_2 = 1
            coeficente_dano = 1

        if direita == True and box_boxer_colision == False:
            moves += 1
            box_boxer_x += 2*acel_x_2
            box_boxer.set_direction(True)

        elif direita == False and box_boxer_colision == False:
            moves -= 1
            box_boxer.inverter()
            box_boxer_x -= 2*acel_x_1
            box_boxer.set_direction(False)
        
        walk_enemy.draw(screen)
    

    # DESENHA O CHÃO=========================================================================================

    if stage < 5:
        floor_group.draw(screen)
        floor2_group.draw(screen)
        floor3_group.draw(screen)
        floor4_group.draw(screen)
        floor5_group.draw(screen)
        floor6_group.draw(screen)
    else:
        floor7_group.draw(screen)
        floor8_group.draw(screen)
        floor9_group.draw(screen)
        floor10_group.draw(screen)
        floor11_group.draw(screen)
        floor12_group.draw(screen)

    if stage == 2 or stage == 9:
        moeda1.rect.x, moeda1.rect.y = 500, 350
        moeda2.rect.x = 400
        cereja1.rect.y = 300
    if stage == 3 or stage == 8:
        cereja1.rect.y = 500
        moeda1.rect.x = 200
        moeda1.rect.y = 500

    if draw_coin1 or draw_coin2 or draw_coin3:
        moedas_group.draw(screen)
    if draw_cherry1 or draw_cherry2:
        cerejas_group.draw(screen)

    # FIM==================================================================================

    screen.blit(text1, (750, 40))
    screen.blit(text2, (475, 40))
    pygame.display.flip()
