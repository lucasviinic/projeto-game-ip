from ast import walk
import pygame
from pygame.locals import *
from sys import exit
from kirby import Kirby
from floor import Floor
from inimigo01 import Inimigo

pygame.init()

# screen info

gravidade = 0.6 #VALOR INICIAL DA GRAVIDADE
width = 960 
height = 720
acel_y_kirby = 0 #VALOR INICIAL DA ACERELAÇÃO NO EIXO Y(ALTURA)

#CONFIGURAÇÕES GERAIS============================================================================================

screen = pygame.display.set_mode((width, height))
background = pygame.image.load('images/background.png')
background = pygame.transform.scale(background, (width, height))
pygame.display.set_caption('Kirby')
font = pygame.font.SysFont('Akziden Ghost', 50, True, False)
clock = pygame.time.Clock()

#KIRBY INFORMAÇÕES============================================================================================

kirby_x = 80
kirby_y = 0
parado = True

kirby = Kirby(screen,50,400,100)

#FIM=================================================================================================

#INSTÂNCIAS DO CHÃO=======================================================================================
floor = Floor(screen,0,900)
floor2 = Floor(screen,0,900)
floor3 = Floor(screen,0,900)
floor4 = Floor(screen,0,900)
floor5 = Floor(screen,0,900)
floor6 = Floor(screen,0,900)
#FIM====================================================================================================================



#INIMIGOS====================================================================================================================

box_boxer = Inimigo(screen,10,10,100)
box_boxer_x = 550
box_boxer_y = 0
moves = 0


#FIM====================================================================================================================


#SPRITES
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

#SPRITES

# collectables info

draw_coin = True
draw_potion = True

# game loop

while True:
#CONFIGAÇÕES========================================================================================

    clock.tick(120) #FPS
    screen.fill('BLACK') 
    screen.blit(background, (0, 0))
    parado = True #SETA O PERSONAGEM COMO PARADO

    t = clock.get_time() #COLETA O TEMPO DECORRIDO
    f = gravidade*t #GERA ACERELAÇÃO DA GRAVIDADE

    if(acel_y_kirby < 525): #DEFINE O CHÃO
        acel_y_kirby += f
    
    else:
        acel_y_kirby = 525

    
    if(box_boxer_y < 534.0000000000001): #DEFINE O CHÃO
        box_boxer_y += f
    else:
        box_boxer_y = 534.0000000000001

#fim===============================================================================================

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

#MOVIMENTA O PERSONAGEM==================================================================================

        if (event.type == KEYDOWN):    
            if(event.key == K_a):
                kirby_x -= 2
                kirby.update_left()
                parado = False
            
            if(event.key == K_d):
                kirby_x += 2
                kirby.update_right() 
                parado = False

            if(event.key == K_w):
                kirby_y -= 5

            if(event.key == K_s):
                kirby_y += 5

    if(pygame.key.get_pressed()[K_a]):
        kirby_x -= 3
        kirby.update_left()
        parado = False
    if(pygame.key.get_pressed()[K_d]):
        kirby_x += 3
        kirby.update_right()
        parado = False

    if(pygame.key.get_pressed()[K_w]):
        kirby_y -= 1

    if(pygame.key.get_pressed()[K_s]):
        kirby_y += 5

    if(parado == True):
        kirby.stopped()

#FIM===============================================================================================


#POSICIONA O CHÃO==================================================================================
    
    floor.set_pos(0,605)
    floor.posicionar()
    floor2.set_pos(200,605)
    floor2.posicionar()
    floor3.set_pos(400,605)
    floor3.posicionar()
    floor4.set_pos(600,605)
    floor4.posicionar()    
    floor5.set_pos(600,605)
    floor5.posicionar()     
    floor6.set_pos(800,605)
    floor6.posicionar()  

#FIM==================================================================================
    k_x = kirby.get_pos_x()
    k_y = kirby.get_pos_y()
    i_x = box_boxer.get_pos_x()
    i_y = int(box_boxer.get_pos_y())

    
    if(kirby.colision(k_x,k_y,i_x,i_y) <= 80):
       kirby.damage(100)

       
    if(kirby.get_life() >= 0):
        kirby.set_pos(kirby_x,acel_y_kirby)
        kirby.mover()
        walk_kirby.draw(screen)

    box_boxer.set_pos(box_boxer_x,box_boxer_y)
    box_boxer.mover()
    box_boxer.update()

    if(moves <= 0):
        direita = True

    if(moves >= 140):
        direita = False

    if(direita == True):
        moves +=1
        box_boxer_x += 2
        
    else:
        moves -=1
        box_boxer.inverter(direita)
        box_boxer_x -= 2
    
#DESENHA chão====================================================================================

    floor_group.draw(screen)
    floor2_group.draw(screen)
    floor3_group.draw(screen)
    floor4_group.draw(screen)
    floor5_group.draw(screen)
    floor6_group.draw(screen)
    walk_enemy.draw(screen)

#FIM==================================================================================
        
    pygame.display.flip()