import re
import random
import colorama #https://www.youtube.com/watch?v=u51Zjlnui4Y 
from colorama import Fore, Back, Style #https://pypi.org/project/colorama/ 
colorama.init(autoreset = True)

words = open("wordslist.txt").read()

pattern = r"^[a-z]{5}$"
word_options = re.findall(pattern,words,re.M)

def word_to_guess():
    word_to_guess = random.choice(word_options)
    return word_to_guess

def validate():
    valid_word = False
    while not valid_word:
        player_input = input("What is your guess?")
        player_input = player_input.lower()
        if player_input in word_options:
            valid_word = True
            return player_input
        else:
            print("The word is not valid")

def compare_answer():
    answer = word_to_guess()

    for _ in range(6):
        player_input = validate()

        correct = []
        intheword = []
        wrong = []
        
        for i in range(5):
            if player_input[i] == answer[i]:
                print(Back.GREEN + player_input[i], end="")
                correct.append(player_input[i])
            
            elif player_input[i] in answer:
                print(Back.YELLOW + player_input[i], end="")
                intheword.append(player_input[i])
        
            elif player_input[i] not in answer:
                print(player_input[i], end="")
                wrong.append(player_input[i])
                
            elif player_input == answer:
                print("You win!")
                return

        if correct != []:
            print("these letters are in the right place",correct)
        if intheword != []:
            print("these letters are in the word, but in the wrong place", intheword)
        if wrong != []:
            print("these letters are not in the word", wrong)
            
    return print("the word was:", answer)


#Que faire si la lettre y est deux fois?
#Maniere plus claire de l'afficher?
    
compare_answer()




