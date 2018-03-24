# rps.py

import random

def is_valid_play(play):
    return play in ["rock","paper","scissors"]

def random_play():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_game_result(human, computer):
    # vrací řetezec s volbou
     if human == computer:
         return 'nerozhodne'
     elif human+computer in "rockpaperscissorsrock":
         return "Prohrals!"
     else:
         return "Vyhrals!"

def main(input=input):
    valid = False
    human = ''
    while not is_valid_play(human):
        human = input('rock, paper or scissors? ')


    computer = random_play()
    print(computer)

    result = determine_game_result(human, computer)

    if result == 'nerozhodne':
        print('nerozhodne')
    else:
        print(result, 'Vyhral!')


# když importujeme rps, __name__ je 'rsp'
# když spouštíme python rps.py, __name__ je '__main__'

if __name__ == '__main__':
    # __main__ -- jméno souboru ve kterém jsme
    main()





if False:
    human = input('rock, paper or scissors? ')

    while human not in ['rock', 'paper', 'scissors']:
        human = input('rock, paper or scissors? ')

    computer = random.choice(['rock', 'paper', 'scissors'])

    print(computer)

    if human == computer:
        print('nerozhodne')
    elif human == "rock" and computer == "paper":
      print("Vyhrals!")
    elif human == "rock" and computer == "scissors":
      print("Prohrals!")
    elif human == "paper" and computer == "scissors":
      print("Prohrals!")
    elif human == "paper" and computer == "rock":
      print("Vyhrals!")
    elif human == "scissors" and computer == "paper":
      print("Vyhrals!")
    elif human == "rock" and computer == "scissors":
      print("Vyhrals!")

# if human == computer:
#     print('nerozhodne')
# elif human+computer in "rockpaperscissorsrock":
#     print("computer wins")
# else:
#     print("human wins")
