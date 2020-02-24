def play_game():
    num = 3
    guess = input('Make your guess')
    guess = int(guess)
    if guess == num:
        print('YOU WINN!!')
    else:
        print('Better luck next time')

    play_game()
