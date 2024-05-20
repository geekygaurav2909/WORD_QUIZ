from turtle import Screen
from matrix import Matrix
from score_tracker import Score_Track
from word_base import word_dict
import time
import random


screen = Screen()
screen.title("!!Word Guessing Game!!")
screen.screensize(700,700)
screen.bgcolor('black')
screen.tracer(0)

is_game_on = True

score =Score_Track()


box = Matrix(no_of_rows=3,no_of_cols=3)
words_to_guess = int(screen.textinput(title="Input Required", prompt="How many words would you like to guess?: "))

# Generating the random list of words to guess
word_list = [(random.choice(word_dict)).upper() for _ in range(words_to_guess)]

# Concatenating string into a list

alpha_string = [char for string in word_list for char in string]
upper_case = ''.join(alpha_string)

print(f"The alpha is: {upper_case}")

box.fill_values(upper_case)


while is_game_on:
    screen.update()
    time.sleep(0.1)

    user_input = screen.textinput(title="User Guess", prompt="Guess the word: ").lower()
    score.word_tracker(word=user_input)

    print(f"The count is {score.guess.count(user_input)}")
    print(f"The guess list is {score.guess}")

    #converting list into a lowercase.
    final_dict = [word.lower() for word in word_dict]


    # Char check from matrix
    available = all(char in upper_case.lower() for char in user_input)


    if user_input in final_dict and available:
        score.word_check(user_input)
    else:
        is_game_on = False
        score.game_over()


screen.exitonclick()