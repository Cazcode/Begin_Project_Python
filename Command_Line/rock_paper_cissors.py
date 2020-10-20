import random

GAME_WORDS = ['ROCK','PAPER','CISSORS']
def rock_papaer_cissors():
    idx_words = random.randint(0, len(GAME_WORDS) - 1)
    computer_choice = GAME_WORDS[idx_words]
    while True:
        user_choices = input('Do you Already Select your choice!! Then Lets go!!...\n ROCK, PAPER, CISSORS!!!')
        print('Computer: ' + computer_choice + " Vs Your: "+ user_choices)
        if user_choices == computer_choice:
            a = "HOla"
            

def run():
    rock_papaer_cissors()


if __name__ == "__main__":
    run()