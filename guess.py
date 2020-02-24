def play_game():
    num = 3
    guess = input('Make your guess')
    if not guess.isdigit():
        print('Please enter an integer')
        exit()
    guess = int(guess)
    if guess == num:
        print('YOU WINN!!')
    else:
        print('Better luck next time')

    play_game()
