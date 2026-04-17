import pygame
import sys

pygame.init()

screen_width = 1200
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menu")

background = pygame.image.load("images/blue_background_img.png").convert()   #https://pixabay.com/fr/illustrations/conception-courbes-bleu-contexte-2207760/
background = pygame.transform.scale(background, (1200, 800))

def get_font(size):
    return pygame.font.Font("FreeSansBold.otf", size)

class Buttons(): #https://github.com/baraltech/Menu-System-PyGame/blob/main/button.py
    def __init__(self, image, pos ,text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text_input = text_input

        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
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


def options():
    while True:
         options_mouse_pos = pygame.mouse.get_pos()
         screen.fill('white')
         
         options_text = get_font(45).render("This is the OPTIONS screen", True, 'black')
         options_rect = options_text.get_rect(center=(600, 200))
         screen.blit(options_text, options_rect)

         options_back = Buttons(image=None,pos=(600, 460), text_input="BACK", font=get_font(75), base_color="Black", hovering_color="red")
         options_back.changeColor(options_mouse_pos)
         options_back.update()
         
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if options_back.checkForInput(options_mouse_pos):
                    main_menu()

            pygame.display.update()
        

def main_menu():
    while True:
        screen.blit(background, (0,0))
        menu_mouse_pos = pygame.mouse.get_pos()
        menu_text = get_font(100).render("MAIN MENU", True, 'white')
        menu_rect = menu_text.get_rect(center=(640, 150))

        play_button = Buttons(image=None, pos=(600, 350), text_input="PLAY", font=get_font(75), base_color = 'white', hovering_color = "#ADD8E6")
        options_button = Buttons(image=None, pos=(600, 450), text_input="OPTIONS", font=get_font(75), base_color = 'white', hovering_color = "blue")
        quit_button = Buttons(image=None, pos=(600, 550), text_input="QUIT", font=get_font(50), base_color = 'white', hovering_color = "#ADD8E6")

        screen.blit(menu_text, menu_rect)

        for button in [play_button, options_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_mouse_pos):
                    import FinalProject
                if options_button.checkForInput(menu_mouse_pos):
                    options()
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()








