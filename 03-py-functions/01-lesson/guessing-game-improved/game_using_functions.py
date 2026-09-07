import random
from game_helpers import *

# play_guessing_game() - en funksjon
#   read_guess() - input fra spilleren
#   check_guess() - sjekke gjettet
#   show_feedback() - gi status til spilleren, hurra eller for høyt/lavt

def play_guessing_game():
    secret_number = random.randint(1,30)
    result= ""


    while result != "correct":
        guess = read_guess()
        result = check_guess(guess, secret_number)
        show_feedback(result)


play_guessing_game()