import pygame
import re
import sys
import random

pygame.init()
#https://www.youtube.com/watch?v=mJ2hPj3kURg
# https://github.com/baraltech/Wordle-PyGame/blob/main/youtubemain.py 


screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("images/Starting Tiles.png")
background_rect = background.get_rect(center=(600, 300))

words = open("wordslist.txt").read()

pattern = r"^[a-z]{5}$"
word_options = re.findall(pattern,words,re.M)

GREEN = "#6aaa64"
YELLOW = "#c9b458"
GREY = "#787c7e"
OUTLINE = "#d3d6da"
FILLED_OUTLINE = "#878a8c"

alphabet = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

correct_word = random.choice(word_options)

guessedLetterFont = pygame.font.Font("FreeSansBold.otf", 50)
availableLetterFont = pygame.font.Font("FreeSansBold.otf", 25)

screen.fill("white")
screen.blit(background, background_rect)
pygame.display.update()

letter_x_spacing = 85
letter_y_spacing = 12
letter_size = 75

guesses_count = 0

guesses = [[]]*6

current_guess = []
current_guess_string = ""
current_letter_bg_x = 110

indicators = []

game_result = ""

class Letter:
    def __init__(self, text, bg_position):
        self.bg_color = "white"
        self.text_color = "black"
        self.bg_position = bg_position
        self.bg_x = bg_position[0]
        self.bg_y = bg_position[1]
        self.bg_rect =(self.bg_x+283, self.bg_y, letter_size, letter_size)
        self.text = text
        self.text_position = (self.bg_x+318, self.bg_position[1]+43)
        self.text_surface = guessedLetterFont.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.text_position)

    def draw(self):
        pygame.draw.rect(screen, self.bg_color, self.bg_rect)
        if self.bg_color == "white":
            pygame.draw.rect(screen, FILLED_OUTLINE, self.bg_rect, 3)
        self.text_surface = guessedLetterFont.render(self.text, True, self.text_color)
        screen.blit(self.text_surface, self.text_rect)
        pygame.display.update()
    
    def delete(self):
        pygame.draw.rect(screen, "white", self.bg_rect)
        pygame.draw.rect(screen, OUTLINE, self.bg_rect, 3)
        pygame.display.update()

class Indicator:
    def __init__(self, x, y, letter):
        self.x = x
        self.y = y
        self.text = letter
        self.rect = (self.x, self.y, 57, 57)
        self.bg_color = OUTLINE

    
    def draw(self):
        pygame.draw.rect(screen, self.bg_color, self.rect)
        self.text_surface = availableLetterFont.render(self.text, True, "white")
        self.text_rect = self.text_surface.get_rect(center=(self.x+27, self.y+30))
        screen.blit(self.text_surface, self.text_rect)
        pygame.display.update()

indicator_x, indicator_y = 300, 600

for i in range(3):
    for letter in alphabet[i]:
        new_indicator = Indicator(indicator_x, indicator_y, letter)
        indicators.append(new_indicator)
        new_indicator.draw()
        indicator_x += 60
    indicator_y += 65
    if i == 0:
        indicator_x = 330
    elif i == 1:
        indicator_x = 400

def play_again():
    pygame.draw.rect(screen, "white", (10, 600, 1000, 600))
    play_again_font = pygame.font.Font("FreeSansBold.otf", 40)
    play_again_text = play_again_font.render("Press ENTER to Play Again!", True, "black")
    play_again_rect = play_again_text.get_rect(center=(screen_width/2, 700))
    word_was_text = play_again_font.render(f"The word was {correct_word}!", True, "black")
    word_was_rect = word_was_text.get_rect(center=(screen_width/2, 650))
    screen.blit(word_was_text, word_was_rect)
    screen.blit(play_again_text, play_again_rect)
    pygame.display.update()

def check_guess(guess_to_check):
    global current_guess, current_guess_string, guesses_count, current_letter_bg_x, game_result
    game_decided = False
    for i in range(5):
        lowercase_letter = guess_to_check[i].text.lower()
        if lowercase_letter in correct_word:
            if lowercase_letter == correct_word[i]:
                guess_to_check[i].bg_color = GREEN
                for indicator in indicators:
                    if indicator.text == lowercase_letter.upper():
                        indicator.bg_color = GREEN
                        indicator.draw()
                guess_to_check[i].text_color = "white"
                if not game_decided:
                    game_result = "W"
                    import FinalProject_Part2
                    
            else:
                guess_to_check[i].bg_color = YELLOW
                for indicator in indicators:
                    if indicator.text == lowercase_letter.upper():
                        indicator.bg_color = YELLOW
                        indicator.draw()
                guess_to_check[i].text_color = "white"
                game_result = ""
                game_decided = True
        else:
            guess_to_check[i].bg_color = GREY
            for indicator in indicators:
                if indicator.text == lowercase_letter.upper():
                    indicator.bg_color = GREY
                    indicator.draw()
            guess_to_check[i].text_color = "white"
            game_result = ""
            game_decided = True
        guess_to_check[i].draw()
        pygame.display.update()
    
    guesses_count += 1
    current_guess = []
    current_guess_string = ""
    current_letter_bg_x = 110

    if guesses_count == 6 and game_result == "":
        game_result = "L"
        play_again()


def reset():
    global guesses_count, correct_word, guesses, current_guess, current_guess_string, game_result
    screen.fill("white")
    screen.blit(background, background_rect)
    guesses_count = 0
    correct_word = random.choice(word_options)
    guesses = [[]] * 6
    current_guess = []
    current_guess_string = ""
    game_result = ""
    pygame.display.update()
    for indicator in indicators:
        indicator.bg_color = OUTLINE
        indicator.draw()

def create_new_letter():
    global current_guess_string, current_letter_bg_x
    current_guess_string += key_pressed
    new_letter = Letter(key_pressed, (current_letter_bg_x, guesses_count*100+letter_y_spacing))
    current_letter_bg_x += letter_x_spacing
    guesses[guesses_count].append(new_letter)
    current_guess.append(new_letter)
    for guess in guesses:
        for letter in guess:
            letter.draw()

def delete_letter():
    global current_guess_string, current_letter_bg_x
    guesses[guesses_count][-1].delete()
    guesses[guesses_count].pop()
    current_guess_string = current_guess_string[:-1]
    current_guess.pop()
    current_letter_bg_x -= letter_x_spacing

running = True
while running:
    #if game_result == "L":
        #play_again()
    if game_result == "W":
       import FinalProject_Part2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if game_result != "":
                    reset()
                else:
                    if len(current_guess_string) == 5 and current_guess_string.lower() in word_options:
                        check_guess(current_guess)

            elif event.key == pygame.K_BACKSPACE:
                if len(current_guess_string) > 0:
                    delete_letter()
            else:
                key_pressed = event.unicode.upper()
                if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                    if len(current_guess_string) < 5:
                        create_new_letter()

        
    pygame.display.flip()
