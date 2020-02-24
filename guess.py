import random


def play_game():
    num = random.randrange(1, 10)
    print('Please guess from 1 to 10')
    guess = input('Make your guess: ')
    guess = int(guess)
    if guess == num:
        print('YOU WINN!!')
    else:
        print('Better luck next time')

    play_game()
