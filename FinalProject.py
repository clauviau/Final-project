import pygame
import random
import time


pygame.init()


screen_width = 1200
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


# desk and library images from https://opengameart.org/content/wooden-cupboard-shelf-pcdesk
# wall image from https://opengameart.org/content/medieval-wall
    #used GIMP to make wall_img.png bigger, by creating a canvas the size of the screen and ctr+c/ctr+v the initial image
    #windows :  https://fr.freepik.com/photos-vecteurs-libre/fenetre-arche 

 #Level class understood from this video : https://www.youtube.com/watch?v=QZ6f9i_GE4s&list=PL117jAcXfXy5lV5A6gi1FEfjxSeBXD3Sz&index=2
 #structure of the cloud generation : https://www.youtube.com/watch?v=QZ6f9i_GE4s&list=PL117jAcXfXy5lV5A6gi1FEfjxSeBXD3Sz&index=4 

class Background():
    def __init__(self, screen):
        self.screen = screen
        self.sky = pygame.image.load('images/sky1.png').convert_alpha()
        self.sky = pygame.transform.scale(self.sky, (screen_width, screen_height))
        
        self.wall = pygame.image.load('images/bigwall.png').convert_alpha() 
        self.wall = pygame.transform.scale(self.wall, (screen_width, screen_height))

        #self.desk = pygame.image.load('images/woodDesk_img.png').convert_alpha()
        #self.desk = pygame.transform.scale(self.desk, (180, 215))

        self.door = pygame.image.load('images/closeddoor_img.png').convert_alpha()
        self.door = pygame.transform.scale(self.door, (180, 300))

        self.cloud = pygame.image.load('images/clouds_img.png').convert_alpha()
        self.cloud = pygame.transform.scale(self.cloud, (110, 90))
        self.clouds = []

        for i in range(4):
            x = random.randint(0, screen_width)
            y = random.randint(100,200)
            speed = random.randint(2,4)
            self.clouds.append({"x": x, "y":y, "speed":speed})
     

    def update_cloud(self):
        for cloud in self.clouds:
            cloud["x"] += cloud["speed"]

            if cloud["x"] > screen_width:
                cloud["x"] = -100
                cloud["y"] = random.randint(0,250)
                cloud["speed"] = random.randint(1,3)
    
    def draw(self):
        self.screen.blit(self.sky, (0, 0))
        for cloud in self.clouds:
            self.screen.blit(self.cloud, (cloud["x"], cloud["y"]))

        self.screen.blit(self.wall, (0, 0))
        self.floor = pygame.draw.rect(self.screen,(75, 30, 0), (0, 680, 1200, 120))
        #self.screen.blit(self.desk, (800, 500))
        self.screen.blit(self.door, (100, 390))
 
    def run(self):
        self.update_cloud()
        self.draw()

def get_font(size):
    return pygame.font.Font("FreeSansBold.otf", size)

class Buttons():
    def __init__(self, image, x_pos, y_pos, size_hover, hover_pos):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))

        self.hover_image = pygame.image.load("images/white.png").convert_alpha()
        self.hover_image = pygame.transform.scale(self.hover_image, size_hover)
        self.hover_pos_x = hover_pos[0]
        self.hover_pos_y = hover_pos[1]
        
        self.hover_image_rect = self.hover_image.get_rect(topleft=(self.hover_pos_x, self.hover_pos_y))

    def update(self):
        screen.blit(self.image, self.rect)

    def checkForInput_library(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            import Guidedwordle

    def checkForInput_desk(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
            #self.text = get_font(50).render(self.text, True, 'black')
            #self.text_rect = self.text.get_rect(center=(600, 400))
            #screen.blit(self.text, self.text_rect)
            
            
    def change_color(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            screen.blit(self.hover_image, self.hover_image_rect)
            screen.blit(self.image, self.rect)
            
    def run(self):
        self.update()



button_library = pygame.image.load('images/library_img.png').convert_alpha()
button_library = pygame.transform.scale(button_library, (180, 250))

button_desk = pygame.image.load('images/woodDesk_img.png').convert_alpha()
button_desk = pygame.transform.scale(button_desk, (180, 215))


background = Background(screen)
buttons_library = Buttons(button_library, 550, 440, (195, 260),(542, 435))
buttons_desk = Buttons(button_desk,800, 500, (190, 225), (795, 495))

#self.blit(self.desk, (800, 500))
#self.screen.blit(self.library, (550, 440))

message = ""
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            buttons_library.checkForInput_library(mouse_pos)
            if buttons_desk.checkForInput_desk(mouse_pos):
                message = "Not available at this time!"
            
    background.run()
    buttons_library.run()
    buttons_desk.run()
    buttons_library.change_color(mouse_pos)
    buttons_desk.change_color(mouse_pos)

    if message != "":
        message_time = pygame.time.get_ticks()
        if message_time < 4000:
            text_surface = get_font(50).render(message, True, "red")
            text_rect = text_surface.get_rect(center=(600, 400))
            screen.blit(text_surface, text_rect)
        else:
            message = ""


    pygame.display.flip()
    clock.tick(60)   

pygame.quit()
