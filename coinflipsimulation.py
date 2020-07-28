#Coin Flip Simulation - Write some code that simulates flipping a single
# coin however many times the user decides. The code
# should record the outcomes and count the number of tails and heads.
from random import randint
keeprunning = True
nu_heads = 0
nu_tails = 0
outcome = []
while keeprunning:

    #tell user the game and ask him to flip or stop the game
    #try for yes or no anything else raise error
    user_input = input('yes to flip and anything else you type will quit the game')
    if user_input == 'yes' or user_input == 'y':
        # random a number from 1 to two
        #show to user if he got a head or tails
        if randint(1,2) == 1:
            print(' you mother fucker got a HEADS')
            nu_heads += 1
            outcome.append('heads')
        else:
            print('you motherfucker got a Tails')
            nu_tails += 1
            outcome.append('tails')
    else:
        print('quitting game you just wasted your time')
        print(f'you mother fucker got {nu_heads} times Heads and {nu_tails} times tails')
        print(outcome)
        keeprunning = False


