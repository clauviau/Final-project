import pygame


pygame.init()

screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()

# desk and library images from https://opengameart.org/content/wooden-cupboard-shelf-pcdesk
# wall image from https://opengameart.org/content/medieval-wall
    #used GIMP to make wall_img.png bigger, by creating a canvas the size of the screen and ctr+c/ctr+v the initial image
    #windows :  https://fr.freepik.com/photos-vecteurs-libre/fenetre-arche 

 #Level class understood from this video : https://www.youtube.com/watch?v=QZ6f9i_GE4s&list=PL117jAcXfXy5lV5A6gi1FEfjxSeBXD3Sz&index=2

class Level:
    def __init__(self, screen):
        self.screen = screen
        self.sky = pygame.image.load('sky1.png').convert_alpha()
        self.sky = pygame.transform.scale(self.sky, (1200, 800))
        self.wall = pygame.image.load('bigwall.png').convert_alpha() 
        self.wall = pygame.transform.scale(self.wall, (1200, 800))
        
        self.desk = pygame.image.load('woodDesk_img.png').convert_alpha()
        self.desk = pygame.transform.scale(self.desk, (180, 215))
        self.library = pygame.image.load('library_img.png').convert_alpha()
        self.library = pygame.transform.scale(self.library, (180, 250))
        
    
    def update(self):
        pass
    
    def draw(self):
        self.screen.blit(self.sky, (0, 0))
        self.screen.blit(self.wall, (0, 0))
        
        self.floor = pygame.draw.rect(self.screen,(75, 30, 0), (0, 680, 1200, 120))

        self.screen.blit(self.desk, (800, 500))
        self.screen.blit(self.library, (550, 440))
        
        

    def run(self):
        self.update()
        self.draw()

   

#def room(screen):

level = Level(screen)

running = True
while running:
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    level.run()
    pygame.display.flip()
    clock.tick(60)   

pygame.quit()


#screen.fill("black") allow to cover previous windows