#how to create background
import pygame
import sys
import math


pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Background Example")

clock = pygame.time.Clock()

beige = (245, 245, 220)
sky_blue = (135, 206, 235)
grey = (128, 128, 128)
brown = (150, 75, 0)

desk_img = pygame.image.load('desk_img.png').convert()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(beige)
    
    #window = pygame.draw.circle(screen, (135, 206, 235), (250,200), 50)
    window = pygame.draw.rect(screen, sky_blue, (250, 200, 100, 125))
    window_top = pygame.draw.ellipse(screen, sky_blue,(250,120,100,135))
    # window_top = pygame.draw.arc(screen, (135, 206, 235), (250, 200, 20, 35), ((math.pi)/4),((3*(math.pi))/4))
    window2 = pygame.draw.rect(screen, sky_blue, (450, 200, 100, 125))
    window2_top = pygame.draw.ellipse(screen, sky_blue,(450,120,100,135))

    screen.blit(desk_img, (250, 350))
    #pygame.draw.rect(screen, brown, (300, 400, 200, 20))

    floor = pygame.draw.rect(screen, grey, (0, 500, 800, 100))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()