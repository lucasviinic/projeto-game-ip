import pygame, sys
from services.manager import *
import time

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

pygame.init()

SCREEN = pygame.display.set_mode((960, 720))
pygame.display.set_caption("Kirby - Menu")
clock = pygame.time.Clock()

BG = pygame.image.load("./images/background_menu.jpg")

def get_font(size):
    return pygame.font.Font("./assets/font.ttf", size)

def main_menu(nome_jogador: str):

    from main import play

    create_table()
    nickname = nome_jogador

    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        LOGO = pygame.image.load("./images/logo.png")
        LOGO_RECT = LOGO.get_rect(center=(480, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("./assets/play_rect.png"), pos=(480, 400), 
                            text_input="PLAY", font=get_font(45), base_color="#d7fcd4", hovering_color="White")

        ranking_list = get_players_sorted_by_score()[:3]
        if len(ranking_list) < 3:
            while len(ranking_list) < 3:
                ranking_list.append((int, "---", "---"))

        FIRST_PLACE_TEXT = get_font(26).render(f"{ranking_list[0][1]}", True, "#b68f40")
        SCREEN.blit(FIRST_PLACE_TEXT, (400, 536))

        SECOND_PLACE_TEXT = get_font(26).render(f"{ranking_list[1][1]}", True, "#b68f40")
        SCREEN.blit(SECOND_PLACE_TEXT, (400, 596))

        THIRD_PLACE_TEXT = get_font(26).render(f"{ranking_list[2][1]}", True, "#b68f40")
        SCREEN.blit(THIRD_PLACE_TEXT, (400, 656))

        SCREEN.blit(LOGO, LOGO_RECT)

        #Icone de trofeu de ouro
        TROFEU_ICON_FIRST = pygame.image.load("./images/trofeu_ouro_test.png")
        TROFEU_ICON_FIRST = pygame.transform.scale(TROFEU_ICON_FIRST, (48, 44))
        TROFEU_ICON_FIRST_RECT = TROFEU_ICON_FIRST.get_rect(center=(350, 550))
        SCREEN.blit(TROFEU_ICON_FIRST, TROFEU_ICON_FIRST_RECT)

        #Icone de trofeu de prata
        TROFEU_ICON_FIRST = pygame.image.load("./images/trofeu_prata_test.png")
        TROFEU_ICON_FIRST = pygame.transform.scale(TROFEU_ICON_FIRST, (48, 44))
        TROFEU_ICON_FIRST_RECT = TROFEU_ICON_FIRST.get_rect(center=(350, 610))
        SCREEN.blit(TROFEU_ICON_FIRST, TROFEU_ICON_FIRST_RECT)

        #Icone de trofeu de bronze
        TROFEU_ICON_FIRST = pygame.image.load("./images/trofeu_bronze_test.png")
        TROFEU_ICON_FIRST = pygame.transform.scale(TROFEU_ICON_FIRST, (48, 44))
        TROFEU_ICON_FIRST_RECT = TROFEU_ICON_FIRST.get_rect(center=(350, 670))
        SCREEN.blit(TROFEU_ICON_FIRST, TROFEU_ICON_FIRST_RECT)

        for button in [PLAY_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.Sound.play(pygame.mixer.Sound("./sounds/click_button_sound.mp3"))
                    time.sleep(0.4)
                    play(nickname=nickname)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    nickname = nickname[:-1]
                else:
                    if len(nickname) < 10:
                        nickname += event.unicode

        NICKNAME_TITLE = get_font(16).render("Nickname:", True, "#b68f40")
        NICKNAME_RECT = NICKNAME_TITLE.get_rect(center=(310, 245))
        SCREEN.blit(NICKNAME_TITLE, NICKNAME_RECT)

        if len(nickname) == 0:
            if pygame.time.get_ticks() % 1000 < 500:
                pygame.draw.line(SCREEN, "white", (250, 320), (250, 280), 2)

        pygame.draw.rect(SCREEN, "white", (236, 265, 480, 68), 2)
        text_surface = get_font(30).render(nickname, True, "black")
        SCREEN.blit(text_surface, (255, 285))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main_menu('')