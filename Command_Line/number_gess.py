import random


def validate_number_in_range(user_number, number_min, number_max):
    return number_min >= user_number >= number_max


def convert_input_to_string(message):
    return int(input(message))


def gess_number():
    print("Please insert the range for the guess game, Insert the minimum value and then the maximum value.\n")
    range_min = convert_input_to_string("Minimun Value: ")
    range_max = convert_input_to_string("Maximum Value: ")

    number_to_gess = random.randint(range_min, (range_max + 1))
    # score = range_max - range_min
    score = 10
    msg = "Please insert a number between " + str(range_min) +" and " + str(range_max) +": "
    user_number = convert_input_to_string(msg)
    
    clue_number_higer = "Try a higger number. "
    clue_number_lower = "Try a lower number. "
    while score > 0 and user_number != number_to_gess:
        score -= 1
        if score == 0:
            print ("This time you do not win, maybe next time :D ")
        print("Your score is: ",str(score))
        if number_to_gess > user_number:
            user_number = convert_input_to_string(clue_number_higer)
        else:
            user_number = convert_input_to_string(clue_number_lower)
        
    print ("Congratulations You Win!")


def menu():
    menu = """
        [1] Gess the Number 
        You got only 10 (ten) opportunities for guess the number can you get the number with the minimum effort? Lets go a head!
    """
    print(menu)
    gess_number()


if __name__ == "__main__":
    menu()