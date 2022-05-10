import time
from sys import exit
from services.manager import *

import pygame
from pygame.locals import *

from floor import Floor
from floor import Floor2
from enemy import Enemy
from kirby import Kirby
from misc import Cherry
from misc import Coin
from random import randint

pygame.init()

def show_message(msg, size, color):
    font1 = pygame.font.SysFont('Akziden Ghost', size, True, False)
    message = f'{msg}'
    formatted_text = font1.render(message, True, color)
    return formatted_text

# screen infoS
def play(nickname: str):
    gravity = 0.04  # VALOR INICIAL DA GRAVIDADE
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
    initial_time = time.time()
    time_hit = time.time()
    time_variation = 0
    music = pygame.mixer.music.load('sounds/musica.mp3')
    pygame.mixer.music.play(-1)
    nick = nickname

    game_over = show_message('GAME OVER', 80, (0, 0, 255))
    restart = show_message('Press T To Restart', 40, (0, 125, 125))
    nick = show_message(f'{nick}', 30, (0, 0, 0))

    # KIRBY INFORMAÇÕES============================================================================================

    kirby = Kirby(screen, 80, 700, 100)

    # FIM=================================================================================================

    # INSTÂNCIAS DO CHÃO=======================================================================================

    floor1 = Floor(screen, 0, 900)
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

    box_boxer = Enemy(screen, 10, 10, 100)
    moves = 0
    box_boxer_colision = False
    distance_coefficient = 1
    damage_coefficient = 1
    acel_x_1 = 1
    acel_x_2 = 1

    # OBJETOS===================================================================================

    coin1 = Coin(540, 500)
    coin2 = Coin(540, 850)
    cherry = Cherry(540, 700)

    # OBJETOS BARRA DE VIDA E PONTUAÇÃO=========================================================================

    coin_pontuation = Coin(20, 255)
    cherry_life = Cherry(20, 15)

    # FIM====================================================================================================================

    # SPRITES
    walk_kirby = pygame.sprite.Group()
    walk_kirby.add(kirby)

    walk_enemy = pygame.sprite.Group()
    walk_enemy.add(box_boxer)

    floor_group = pygame.sprite.Group()
    floor_group.add(floor1)
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

    coins_group = pygame.sprite.Group()
    coins_group.add(coin1)
    coins_group.add(coin2)
    cherrys_group = pygame.sprite.Group()
    cherrys_group.add(cherry)

    # SPRITES

    cherry_bar = pygame.sprite.Group()
    coins_points = pygame.sprite.Group()
    cherry_bar.add(cherry_life)
    coins_points.add(coin_pontuation)

    # collectables info

    draw_coin1 = True
    draw_coin2 = True
    draw_cherry1 = True
    points = 0
    acel_y = 0
    stage = 1
    acel_y2 = 0

    box_boxer.set_pos_x(600)
    box_boxer.set_pos_y(534.0000000000001)

    # game loop

    while True:
        # CONFIGAÇÕES========================================================================================
        clock.tick(60)  # FPS
        screen.fill('BLACK')

        if kirby.get_life() > 0:
            pygame.mixer.music.set_volume(0.2)

        if coin1 in coins_group:
            draw_coin1 = True
        if coin2 in coins_group:
            draw_coin2 = True
        if cherry in cherrys_group:
            draw_cherry1 = True

        if stage < 5:
            screen.blit(background, (0, 0))
        else:
            screen.blit(background2, (0, 0))

        score = f'{points}'
        life_points = 100 - kirby.get_life()
        bar_redution = 2 * life_points
        text1 = font.render(score, True, 'BLACK')
        pygame.draw.rect(screen, (0, 0, 0), (48, 47, 204, 15))
        pygame.draw.rect(screen, (255, 0, 0), (50, 50, 200 - bar_redution, 10))
        cherry_bar.draw(screen)
        coins_points.draw(screen)
        if acel_y == 0:
            kirby.set_stopped(True)

        else:
            kirby.set_fall(True)
        attacking = False

        time_game = clock.get_time()  # COLETA O TEMPO DECORRIDO
        F = gravity * time_game  # GERA ACERELAÇÃO DA GRAVIDADE
        acel_y += F
        acel_y2 += F
        final_time = time.time()
        time_variation = final_time - initial_time
        initial_time = final_time

        if (initial_time - time_hit) >= 0.1 and box_boxer_colision:
            box_boxer_colision = False

        kirby.set_pos_y(kirby.get_pos_y() + acel_y)
        box_boxer.set_pos_y(box_boxer.get_pos_y() + acel_y2)

        if kirby.get_pos_y() >= 526:  # DEFINE O CHÃO
            kirby.set_pos_y(526)
            kirby.set_fall(False)
            acel_y = 0
            time_game = pygame.time.Clock()

        if box_boxer.get_pos_y() <= 534.0000000000001:  # DEFINE O CHÃO
            acel_y = 0
            time_game = pygame.time.Clock()
        else:
            box_boxer.set_pos_y(534.0000000000001)

        # fim===============================================================================================
        if kirby.get_jump():
            acel_y -= 20
            kirby.set_fall(False)
            kirby.update_jump()
            if acel_y <= 0 and kirby.get_jump():
                kirby.set_jump(False)
                kirby.set_fall(True)
                kirby.set_pos_y(kirby.get_pos_y() + acel_y)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            # MOVIMENTA O PERSONAGEM==================================================================================

            if event.type == KEYDOWN and not box_boxer_colision:
                if event.key == K_r:
                    kirby.set_moving(False)
                    attacking = True
                    kirby.set_stopped(True)

                if event.key == K_w:
                    if not kirby.get_run():
                        kirby.set_run(True)
                    else:
                        kirby.set_run(False)

                if event.key == K_a and not pygame.key.get_pressed()[K_r] and not attacking:
                    kirby.set_pos_x(kirby.get_pos_x() - (220 * time_variation))

                    if kirby.get_jump():
                        kirby.update_jump()
                    else:
                        kirby.update_left()

                    kirby.set_direction(False)
                    kirby.set_stopped(False)

                if event.key == K_d and not box_boxer_colision and not pygame.key.get_pressed()[K_d] and not \
                        pygame.key.get_pressed()[K_r] and not attacking:

                    kirby.set_pos_x(kirby.get_pos_x() + (220 * time_variation))

                    if kirby.get_jump():
                        kirby.update_jump()
                    else:
                        kirby.update_right()

                    kirby.set_direction(True)
                    kirby.set_stopped(False)

                if event.key == K_SPACE:
                    if kirby.get_pos_y() == 526:
                        kirby.set_jump(True)

                if event.key == K_t and kirby.get_life() <= 0:
                    kirby.set_pos_x(80)
                    kirby.set_pos_y(526)
                    kirby.set_life(100)
                    points = 0
                    stage = 1
                    pygame.mixer.music.rewind()

                    coin1.rect.x, coin1.rect.y = 500, 540
                    coin2.rect.x, coin2.rect.y = 850, 540
                    cherry.rect.x, cherry.rect.y = 700, 540

                    if coin1 not in coins_group:
                        coins_group.add(coin1)
                    if coin2 not in coins_group:
                        coins_group.add(coin2)
                    if cherry not in cherrys_group:
                        cherrys_group.add(cherry)

        if kirby.get_pos_x() < 0:
            kirby.set_pos_x(10)

        if pygame.key.get_pressed()[K_r] and not box_boxer_colision and not pygame.key.get_pressed()[K_SPACE]:
            attacking = True
            kirby.set_stopped(True)
            kirby.set_moving(False)

        if pygame.key.get_pressed()[K_a] and not box_boxer_colision and not pygame.key.get_pressed()[K_d] and \
                not pygame.key.get_pressed()[K_r] and not attacking:
            kirby.set_stopped(False)
            kirby.set_direction(False)
            kirby.set_moving(True)

            if kirby.get_jump():
                kirby.update_jump()
                kirby.set_pos_x(kirby.get_pos_x() - (400 * time_variation))

            elif not kirby.get_jump():
                if not kirby.get_run():
                    kirby.update_left()
                    kirby.set_pos_x(kirby.get_pos_x() - (240 * time_variation))
                else:
                    kirby.update_run()
                    kirby.set_pos_x(kirby.get_pos_x() - (390 * time_variation))

            kirby.set_stopped(False)

        if pygame.key.get_pressed()[K_d] and not box_boxer_colision and not pygame.key.get_pressed()[K_a] and \
                not pygame.key.get_pressed()[K_r] and not attacking:
            kirby.set_direction(True)
            kirby.set_stopped(False)
            kirby.set_moving(True)

            if kirby.get_jump():
                kirby.update_jump()
                kirby.set_pos_x(kirby.get_pos_x() + (400 * time_variation))

            elif not kirby.get_jump():
                if not kirby.get_run():
                    kirby.update_right()
                    kirby.set_pos_x(kirby.get_pos_x() + (240 * time_variation))
                else:
                    kirby.set_pos_x(kirby.get_pos_x() + (390 * time_variation))
                    kirby.update_run()

            if kirby.get_pos_x() > 930:
                stage += 1
                kirby.set_pos_x(0)
                cherrys_group.add(cherry)
                coins_group.add(coin1)
                coins_group.add(coin2)
                draw_coin1 = True
                draw_coin2 = True
                draw_cherry1 = True
                coin1.rect.x, coin1.rect.y = randint(300, 900), randint(200, 540)
                coin2.rect.x, coin2.rect.y = randint(300, 900), 540
                cherry.rect.x, cherry.rect.y = randint(300, 900), randint(200, 540)
                if box_boxer.get_vida() <= 0:
                    box_boxer.set_vida(-100)

                box_boxer.set_pos_x(600)
                box_boxer.set_pos_y(534.0000000000001)
                box_boxer.set_direction(False)
                moves = 0
                acel_x2 = 1
                damage_coefficient = 1

            kirby.set_stopped(False)

        if kirby.get_stopped() and not kirby.get_jump() and not kirby.get_fall() and not attacking and not box_boxer_colision:
            kirby.stopped()

        elif kirby.get_jump() and not box_boxer_colision and not kirby.get_fall():
            kirby.update_jump()

        elif not kirby.get_jump() and kirby.get_fall() and not box_boxer_colision and not kirby.get_stopped():
            kirby.update_jump()

        elif kirby.get_jump() and not kirby.get_fall() and not box_boxer_colision:
            kirby.update_jump()

        elif not kirby.get_jump() and not kirby.get_fall() and attacking and not box_boxer_colision:

            kirby.update_basic_atk()

        # FIM===============================================================================================

        # POSICIONA O CHÃO==================================================================================

        floor1.set_pos(0, 605)
        floor1.posicionar()
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

        if kirby.colision(kirby.get_pos_x(), kirby.get_pos_y(), box_boxer.get_pos_x(),
                        box_boxer.get_pos_y()) <= 80 and not attacking and box_boxer.get_vida() > 0 and kirby.get_life() > 0:

            if kirby.get_pos_x() < box_boxer.get_pos_x():
                kirby.set_pos_x(kirby.get_pos_x() - 1200 * time_variation)
                box_boxer.set_pos_x(box_boxer.get_pos_x() + 1500 * time_variation)
            else:
                kirby.set_pos_x(kirby.get_pos_x() + 1200 * time_variation)
                box_boxer.set_pos_x(box_boxer.get_pos_x() - 1500 * time_variation)

            time_hit = time.time()

            box_boxer_colision = True
            kirby.update_hited()
            kirby.damage(int(1 * box_boxer.get_pos_x() * time_variation * damage_coefficient))

        if draw_coin1:
            if kirby.colision_coin(kirby.rect, coin1.rect):
                coins_group.remove(coin1)
                draw_coin1 = False
                points += 1

        if draw_coin2:
            if kirby.colision_coin(kirby.rect, coin2.rect):
                coins_group.remove(coin2)
                draw_coin2 = False
                points += 1

        if draw_cherry1:
            if kirby.colision_coin(kirby.rect, cherry.rect):
                cherrys_group.remove(cherry)
                draw_cherry1 = False
                kirby.set_life(10)

        if kirby.get_life() > 0:
            kirby.set_pos(kirby.get_pos_x(), kirby.get_pos_y())
            kirby.mover()
            walk_kirby.draw(screen)

            if kirby.colision(kirby.get_pos_x(), kirby.get_pos_y(), box_boxer.get_pos_x(),
                            box_boxer.get_pos_y()) <= 170 and 17 <= kirby.get_index() <= 21 and kirby.get_life() > 0 and\
                    box_boxer.get_vida() > 0 and kirby.get_stopped():

                if kirby.get_pos_x() < box_boxer.get_pos_x() and kirby.get_direction() == True:
                    box_boxer.set_pos_x(box_boxer.get_pos_x() - 10)

                    if kirby.colision(kirby.get_pos_x(), kirby.get_pos_y(), box_boxer.get_pos_x(),
                                    box_boxer.get_pos_y()) <= 80 and attacking and kirby.get_direction():
                        box_boxer.set_vida(box_boxer.get_vida())
                        kirby.set_life(5)

                elif kirby.get_pos_x() > box_boxer.get_pos_x() and not kirby.get_direction():
                    box_boxer.set_pos_x(box_boxer.get_pos_x() + 10)

                    if kirby.colision(kirby.get_pos_x(), kirby.get_pos_y(), box_boxer.get_pos_x(),
                                    box_boxer.get_pos_y()) <= 80 and attacking and not kirby.get_direction():
                        box_boxer.set_vida(box_boxer.get_vida())
                        kirby.set_life(5)

                elif kirby.get_pos_x() < box_boxer.get_pos_x() and not kirby.get_direction() and kirby.colision(
                        kirby.get_pos_x(), kirby.get_pos_y(), box_boxer.get_pos_x(), box_boxer.get_pos_y()) <= 80:
                    kirby.set_pos_x(kirby.get_pos_x() - 1200 * time_variation)
                    box_boxer.set_pos_x(box_boxer.get_pos_x() + 1500 * time_variation)
                    time_hit = time.time()
                    box_boxer_colision = True
                    kirby.update_hited()
                    kirby.damage(int(1 * box_boxer.get_pos_x() * time_variation * damage_coefficient))

                elif kirby.get_pos_x() > box_boxer.get_pos_x() and kirby.get_direction() and kirby.colision(
                        kirby.get_pos_x(), kirby.get_pos_y(), box_boxer.get_pos_x(), box_boxer.get_pos_y()) <= 80:
                    kirby.set_pos_x(kirby.get_pos_x() + 1200 * time_variation)
                    box_boxer.set_pos_x(box_boxer.get_pos_x() - 1500 * time_variation)
                    time_hit = time.time()
                    box_boxer_colision = True
                    kirby.update_hited()
                    kirby.damage(int(1 * box_boxer.get_pos_x() * time_variation * damage_coefficient))
        else:
            kirby.set_life(0)
            screen.blit(game_over, (280, 260))
            screen.blit(restart, (330, 340))
            box_boxer.set_pos_x(600)
            box_boxer.set_pos_y(534.0000000000001)
            pygame.mixer.music.set_volume(0)
            box_boxer.set_index(0)
            moves = 0
            distance_coefficient = 1
            damage_coefficient = 1
            
            #Registra no banco de dados
            print(f"{nickname} morreu :( e fez {score} pontos")
            insert_player(nick=nickname, score=score)

        coin1.update()
        coin2.update()

        if box_boxer.get_vida() > 0:

            box_boxer.set_pos(box_boxer.get_pos_x(), box_boxer.get_pos_y())
            box_boxer.mover()

            if not box_boxer_colision:
                box_boxer.update()

            if (kirby.get_direction() and not box_boxer.get_direction()) and kirby.colision(kirby.get_pos_x(),
                                                                                                        kirby.get_pos_y(),
                                                                                                        box_boxer.get_pos_x(),
                                                                                                        box_boxer.get_pos_y()) <= 200 and kirby.get_pos_x() < box_boxer.get_pos_x():
                acel_x_2 = 2 + (stage * 0.2)
                coeficiente_distancia = 1.2
                coeficente_dano = 2

            elif (not kirby.get_direction() and box_boxer.get_direction()) and kirby.colision(
                    kirby.get_pos_x(), kirby.get_pos_y(), box_boxer.get_pos_x(),
                    box_boxer.get_pos_y()) <= 200 and kirby.get_pos_x() > box_boxer.get_pos_x():
                acel_x_2 = 2 + (stage * 0.2)
                distance_coefficient = 1.2
                damage_coefficient = 2

            if box_boxer.get_pos_x() <= 0:
                moves = 0

            if box_boxer.get_pos_x() >= 920:
                moves = 140 * distance_coefficient

            if moves <= 0:
                right = True

            if moves >= 140 * distance_coefficient:
                right = False
                distance_coefficient = 1
                acel_x_1 = 1
                acel_x_2 = 1
                damage_coefficient = 1

            if right and not box_boxer_colision:
                moves += 1
                box_boxer.set_pos_x(box_boxer.get_pos_x() + 2 * acel_x_2)
                box_boxer.set_direction(True)

            elif not right and box_boxer_colision == False:
                moves -= 1
                box_boxer.inverter()
                box_boxer.set_pos_x(box_boxer.get_pos_x() - 2 * acel_x_2)
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

        if draw_coin1 or draw_coin2:
            coins_group.draw(screen)
        if draw_cherry1:
            cherrys_group.draw(screen)

        # FIM==================================================================================

        screen.blit(text1, (305, 36))
        screen.blit(nick, (60, 20))
        pygame.display.flip()
