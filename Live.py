def welcome(name):
    print('-----------------------------------------------------------------------')
    print("Hello " + name + " and welcome to the World of Games (WoG).")
    print("Here you can find many cool games to play.")
    print('-----------------------------------------------------------------------')
    return name




def load_game():
    print('Please choose a game to play:')
    print('1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back')
    print('2. Guess Game - guess a number and see if you chose like the computer')
    c= int(input('choose number "1" or "2" '))
    print('-----------------------------------------------------------------------')
    difficulty=int(input('Please choose game difficulty from 1 to 5'))
    if c == 1:
        print('Lets play Memory Game')
        from MemoryGame import play
        play(difficulty)

    elif c == 2:
        print('Lets play Guess Game')
        from GuessGame import play
        play(difficulty)

    else:
        print("Something went wrong..")
    print('-----------------------------------------------------------------------')










