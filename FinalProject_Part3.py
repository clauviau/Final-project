import pygame
import random


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

        self.library = pygame.image.load('images/library_img.png').convert_alpha()
        self.library = pygame.transform.scale(self.library, (180, 250))

        self.desk = pygame.image.load('images/woodDesk_img.png').convert_alpha()
        self.desk = pygame.transform.scale(self.desk, (180, 215))
        
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
        self.screen.blit(self.library, (550, 440))
        self.screen.blit(self.desk, (800, 500))
        
    def run(self):
        self.update_cloud()
        self.draw()

def get_font(size):
    return pygame.font.Font("FreeSansBold.otf", size)

class Door():
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load("images/door_code.png").convert()
        self.background = pygame.transform.scale(self.background, (1200, 800))
        self.circle = pygame.image.load("images/Door code images/green_circle.png").convert_alpha()
        self.wrong_start_time = 0
        self.show_wrong = False

        self.code_entered = ""
        self.correct_code = "1884"
        self.unlocked = False

        self.numbers = {"1": pygame.Rect(460, 155, 100, 100),
        "2": pygame.Rect(595, 155, 100, 100),
        "3": pygame.Rect(730, 155, 100, 100),

        "4": pygame.Rect(460, 290, 100, 100),
        "5": pygame.Rect(595, 290, 100, 100),
        "6": pygame.Rect(730, 290, 100, 100),

        "7": pygame.Rect(460, 425, 100, 100),
        "8": pygame.Rect(595, 425, 100, 100),
        "9": pygame.Rect(730, 425, 100, 100),

        "X": pygame.Rect(460, 555, 100, 100),
        "0": pygame.Rect(595, 555, 100, 100),
        "key": pygame.Rect(730, 555, 100, 100)}
        
        self.clicked_numbers = []

    def run(self):
        self.screen.blit(self.background, (0, 0))

        current_time = pygame.time.get_ticks()

        new_clicked = []

        for item in self.clicked_numbers:
            if current_time - item["time"] < 500:
                self.screen.blit(self.circle, item["pos"])
                new_clicked.append(item)
        

        if self.show_wrong:
            current_time = pygame.time.get_ticks()
            if current_time - self.wrong_start_time < 2000:
                wrong = get_font(100).render("Wrong key", True, 'red')
                wrong_rect = wrong.get_rect(center=(625, 150))
                self.screen.blit(wrong, wrong_rect)
            else:
                self.show_wrong = False
            
              
    def check_code_click(self, position):
            for key, rect in self.numbers.items():
                if rect.collidepoint(position):

                    if key.isdigit():
                        if len(self.code_entered) < 4:
                            self.code_entered += key
                            self.clicked_numbers.append({"pos" : rect.topleft, "time" : pygame.time.get_ticks()})

                    elif key == "X":
                        self.code_entered = ""
                        self.clicked_numbers = []

                    elif key == "key":
                        wrong_start_time = pygame.time.get_ticks()
                        if self.code_entered == self.correct_code:
                            self.unlocked = True
                            
                        else:
                            self.show_wrong = True
                            self.wrong_start_time = pygame.time.get_ticks()
                            self.code_entered = ""
                            self.clicked_numbers = []

            return
        

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
        
    def checkForInput_door(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True

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

button_door = pygame.image.load('images/closeddoor_img.png').convert_alpha()
button_door = pygame.transform.scale(button_door, (180, 300))

openDoor = pygame.image.load('images/opendoor_img.png').convert()
openDoor = pygame.transform.scale(openDoor, (180, 300))
buttons_openDoor = Buttons(openDoor,100, 390, (190, 315), (95, 380))

background = Background(screen)
buttons_door = Buttons(button_door, 100, 390, (190, 315), (95, 380))

door_open = False

door_unlocked = False 

door_code = Door(screen)

def win():
    while True:
        screen.fill("black")
        won_text = get_font(100).render("You WON!", True, 'white')
        won_rect = won_text.get_rect(center=(625, 150))
        screen.blit(won_text, won_rect)
        Menu_text = get_font(50).render("Click Enter to Return to the Game Menu", True, 'white')
        Menu_rect = Menu_text.get_rect(center=(625, 300))
        screen.blit(Menu_text, Menu_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    import GameMenu
                

            pygame.display.update()

running = True
while running:
    won = False
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if door_open: 
                door_code.check_code_click(mouse_pos)
            elif door_unlocked and buttons_openDoor.checkForInput_door(mouse_pos):
                won = True
            elif buttons_door.checkForInput_door(mouse_pos):
                door_open = True
                         
    if door_open:
        door_code.run()

        if door_code.unlocked:
            door_open = False
            door_unlocked = True

    elif door_unlocked:
        background.run()
        buttons_openDoor.run()
        buttons_openDoor.change_color(mouse_pos)
        if won:
            win()
            


    else:
        background.run()
        buttons_door.run()
        buttons_door.change_color(mouse_pos)

        
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)   

pygame.quit()
