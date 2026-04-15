import pygame
import random


pygame.init()


screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))



background = pygame.image.load("images/paper.png")
background = pygame.transform.scale(background, (1190, 800)).convert_alpha()
background_rect = background.get_rect(topleft=(-5, 0))


font_title = pygame.font.Font("FreeSansBold.otf", 50)
font_equation = pygame.font.Font("FreeSansBold.otf", 80)
font_input = pygame.font.Font("FreeSansBold.otf", 55)
font_message = pygame.font.Font("FreeSansBold.otf", 40)


class Title:
    def __init__(self, text):
          self.text = text

    def draw_title(self, surface):
        title_surface = font_title.render(self.text, True, "black")
        title_rect = title_surface.get_rect(center=(screen_width / 2, 120))
        surface.blit(title_surface, title_rect)
        

class Equation:
    def __init__(self):
        self.new_equation()

    def new_equation(self):
        nums = []
        for _ in range(4):
            nums.append(random.randint(1,9))  
        self.question = f"(3*{nums[0]}+{nums[1]}^2)//{nums[2]}+{nums[3]}*2"
        self.answer = (3*nums[0] + nums[1]**2)//nums[2] + nums[3]*2
    
    def draw(self, surface):
        equation_surface = font_equation.render(self.question, True, "black")
        equation_rect = equation_surface.get_rect(center=(screen_width / 2, screen_height / 2 - 80))
        surface.blit(equation_surface, equation_rect)

#class Input:
    #def __init__(self, text):
       # self.text = text

    #def draw_input(self, surface):
        #input_surface = font_input.render(self.text, True, "black")
        #input_rect_text = input_surface.get_rect(center=input_rect.center)
        #screen.blit(input_surface, input_rect_text)

       
title = Title("REMEMBER YOUR PRIORITY OF OPERATIONS?")
equation = Equation()

current_input = ""

message = "Type the answer and press Enter"
message_color = "black"
correct = False
input_rect = pygame.Rect(200, 520, 800, 90)

print(equation.answer)
print(equation.question)
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_RETURN:
                if current_input.strip() =="":
                    message = "Please type a number first"
                    message_color = "red"

                elif int(current_input) == equation.answer:
                    message = "Correct! The key to the door is 1884"
                    message_color = 'green'
                else:
                    message = "Wrong answer, try again"
    
            elif event.key == pygame.K_BACKSPACE:
                current_input = current_input[:-1]
            else:
                current_input += event.unicode

    screen.fill("white")
    screen.blit(background, background_rect)

    title.draw_title(screen)
    equation.draw(screen)

    pygame.draw.rect(screen, "black", input_rect, 2)

    input_surface = font_input.render(current_input, True, "black")
    input_rect_text = input_surface.get_rect(center=input_rect.center)
    screen.blit(input_surface, input_rect_text)

    message_surface = font_message.render(message, True, message_color)
    message_rect = message_surface.get_rect(center=(screen_width / 2, 650))
    screen.blit(message_surface, message_rect)

    pygame.draw.rect(screen, "black", input_rect, 2)

   

    pygame.display.flip()
        

            



pygame.quit()