from ast import walk
import pygame
from pygame.locals import *
from sys import exit
from kirby import Kirby
from floor import Floor
from inimigo01 import Inimigo
from misc import Coin
from misc import Cherry
import time

pygame.init()

# screen infoS

gravidade = 0.5  # VALOR INICIAL DA GRAVIDADE
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
tempo_inicial = time.time()
time_hit = time.time()
variacao_tempo = 0

# KIRBY INFORMAÇÕES============================================================================================

kirby_x = 80
kirby_y = 540
stopped = True
jumping = False
kirby = Kirby(screen, 50, 400, 100)
fall = True
double_press_right = 0
double_press_left = 0


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
box_boxer_colision = False
coeficiente_distancia = 1
coeficente_dano = 1
acel_x_1 = 1
acel_x_2 = 1

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
    stopped = True  # SETA O PERSONAGEM COMO PARADO
    atacando = False

    time_game = clock.get_time()  # COLETA O TEMPO DECORRIDO
    acel_y = gravidade * time_game  # GERA ACERELAÇÃO DA GRAVIDADE
    tempo_final = time.time()
    variacao_tempo = tempo_final - tempo_inicial
    tempo_inicial = tempo_final

    if (tempo_inicial - time_hit) >= 0.1 and box_boxer_colision == True:
        box_boxer_colision = False

    if not jumping:
        kirby_y += acel_y

    if kirby_y > 526:  # DEFINE O CHÃO
        kirby_y = 526
        fall = False
        time_game = pygame.time.Clock()
 
    if box_boxer_y < 534.0000000000001:  # DEFINE O CHÃO
        box_boxer_y += acel_y
    else:
        box_boxer_y = 534.0000000000001


    # fim===============================================================================================
    if jumping:
        time_game = pygame.time.Clock()
        kirby_y -= acel_y
        fall = False

        if kirby.get_pos_y() <= 320:
            jumping = False
            fall = True
            kirby_y += acel_y

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            

        # MOVIMENTA O PERSONAGEM==================================================================================

        if event.type == KEYDOWN:
            if event.key == K_a:
                kirby_x -= 220*variacao_tempo
                if kirby_x < 0:
                    kirby_x += 3

                if(jumping == True):
                    kirby.update_jump()
                else:
                    kirby.update_left()

                kirby.set_direction(False)
                stopped = False

            if event.type == K_r:
                atacando = True

            if event.key == K_d:
                double_press_left = 0

                if(double_press_right < 2):
                    double_press_right += 1

                if(double_press_right < 2):
                    kirby_x += 220*variacao_tempo
                    if kirby_x > 930:
                        kirby_x = 0

                    if(jumping == True):
                        kirby.update_jump()
                    else:
                        kirby.update_right()

                kirby.set_direction(True)
                stopped = False

            if event.key == K_SPACE:
                if kirby_y == 526:
                    jumping = True

    if pygame.key.get_pressed()[K_r]:
        atacando = True

    if pygame.key.get_pressed()[K_a]:
        if kirby_x < 0:
            kirby_x += 4
        
        if(jumping == True):
            kirby.update_jump()
            kirby_x -= 350* variacao_tempo

        else:
            kirby.update_left()
            kirby_x -= 220* variacao_tempo

        stopped = False
        
    if pygame.key.get_pressed()[K_d]:
        if(double_press_right <2):

            if(jumping == True):
                kirby.update_jump()
                kirby_x += 350* variacao_tempo

            else:
                kirby.update_right()
                kirby_x += 220* variacao_tempo

        else:
            if(jumping == True):
                kirby.update_jump()
                kirby_x += 350* variacao_tempo

            else:
                kirby.update_right()
                kirby_x += 220* variacao_tempo


        if kirby_x > 930:
            kirby_x = 0
            cerejas_group.add(cereja1)
            moedas_group.add(moeda1)
            moedas_group.add(moeda2)
            draw_coin1 = True
            draw_coin2 = True
            draw_cherry1 = True

        stopped = False

    if stopped == True and jumping == False and fall == False and atacando == False and box_boxer_colision == False:
        kirby.stopped()

    elif stopped == False and jumping == True and box_boxer_colision == False:
        kirby.update_jump()

    elif jumping == False and fall == True and box_boxer_colision == False:
        kirby.update_fall()

    elif stopped == True and jumping == True and fall == False and box_boxer_colision == False:
        kirby.update_jump()

    elif stopped == True and jumping == False and fall == False and atacando == True:
        
        kirby.update_basic_atk()

        k_x = kirby.get_pos_x()
        k_y = kirby.get_pos_y()
        i_x = box_boxer.get_pos_x()
        i_y = int(box_boxer.get_pos_y())

        if kirby.colision (kirby.get_pos_x(), kirby.get_pos_y(), box_boxer.get_pos_x(), box_boxer.get_pos_y()) <= 170 and kirby.get_index() >= 17:

            if kirby.get_pos_x() < box_boxer.get_pos_x() and kirby.get_direction() == True:
                box_boxer_x -= 10

                if kirby.colision (kirby.get_pos_x(), kirby.get_pos_y(), box_boxer.get_pos_x(), box_boxer.get_pos_y()) <= 80 and atacando == True:
                    box_boxer.set_vida(box_boxer.get_vida())

            elif kirby.get_pos_x() > box_boxer.get_pos_x() and kirby.get_direction() == False:
                box_boxer_x += 10

                if kirby.colision (kirby.get_pos_x(), kirby.get_pos_y(), box_boxer.get_pos_x(), box_boxer.get_pos_y()) <= 80 and atacando == True:
                    box_boxer.set_vida(box_boxer.get_vida())

            elif kirby.get_pos_x() < box_boxer.get_pos_x() and kirby.get_direction() == False and kirby.colision (kirby.get_pos_x(), kirby.get_pos_y(), box_boxer.get_pos_x(), box_boxer.get_pos_y()) <= 80:
                kirby_x = kirby.get_pos_x() - 1000*variacao_tempo
                box_boxer_x += 1500*variacao_tempo
                time_hit = time.time()
                box_boxer_colision = True
                kirby.update_hited()
                kirby.damage(int(1*box_boxer_x*variacao_tempo*coeficente_dano))

            elif k_x > box_boxer.get_pos_x() and kirby.get_direction() == True and kirby.colision (kirby.get_pos_x(), kirby.get_pos_y(), box_boxer.get_pos_x(), box_boxer.get_pos_y()) <= 80:
                kirby_x = kirby.get_pos_x() + 1000*variacao_tempo
                box_boxer_x -= 1500*variacao_tempo
                time_hit = time.time()
                box_boxer_colision = True
                kirby.update_hited()
                kirby.damage(int(1*box_boxer_x*variacao_tempo*coeficente_dano))
            
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

    # FIM========================================================================================

    if kirby.colision (kirby.get_pos_x(), kirby.get_pos_y(), box_boxer.get_pos_x(), box_boxer.get_pos_y()) <= 80 and atacando == False and box_boxer.get_vida() > 0:

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

    moeda1.update()
    moeda2.update()

    if(box_boxer.get_vida() > 0):

        box_boxer.set_pos(box_boxer_x, box_boxer_y)
        box_boxer.mover()

        if box_boxer_colision == False:
            box_boxer.update()

        if (kirby.get_direction() == True and box_boxer.get_direction()== False) and kirby.colision (kirby.get_pos_x(), kirby.get_pos_y(), box_boxer.get_pos_x(), box_boxer.get_pos_y()) <= 200 and kirby.get_pos_x() < box_boxer.get_pos_x():
            acel_x_1 = 1.7
            coeficiente_distancia = 1.2
            coeficente_dano = 3

        elif (kirby.get_direction() == False and box_boxer.get_direction()== True) and kirby.colision (kirby.get_pos_x(), kirby.get_pos_y(), box_boxer.get_pos_x(), box_boxer.get_pos_y()) <= 200 and kirby.get_pos_x() > box_boxer.get_pos_x():
            acel_x_2 = 1.7
            coeficiente_distancia = 1.2
            coeficente_dano = 3

        if moves <= 0 :
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

    floor_group.draw(screen)
    floor2_group.draw(screen)
    floor3_group.draw(screen)
    floor4_group.draw(screen)
    floor5_group.draw(screen)
    floor6_group.draw(screen)

    if draw_coin1 or draw_coin2:
        moedas_group.draw(screen)
    if draw_cherry1:
        cerejas_group.draw(screen)

    # FIM==================================================================================

    screen.blit(text1, (750, 40))
    screen.blit(text2, (475, 40))
    pygame.display.flip()
