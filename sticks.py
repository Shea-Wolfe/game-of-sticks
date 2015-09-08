'''Game setup:
X pick number of sticks
X take player names

Game loop:
inform player turn and ask for removal
check to see if player removed the last sticks
if True, inform player he loses
else continue'''

def game_setup():
    '''Takes no arguements.
    Gets the player names and how many sticks the game will be played with'''
    sticks = int(input('Welcome to the game how many sticks are on the table?\nEnter a number between 10-100? > '))
    player1 = input('Great! player 1 please enter your name > ')
    player2 = input('Awesome! Player 2 please enter your name > ')
    return (sticks, player1, player2)

def player_move(sticks, player_move):
    '''Takes the sticks remaining in the pile and number of sticks removed as arguements
    returns the pile of sticks minus the sticks removed'''
    if player_move < 1 or player_move > 3:
        print('That\'s not a valid move!')
        return player_move(sticks)
    sticks -= player_move
    return sticks

def end_game(current_player):
    '''Takes the losing player as an arguements
    checks to see if the player wants to play again, if yes it runs the main loop
    if no it breaks the main loop which exits the program.'''
    credit = input('You lose {}!  Would you like to play again? enter [y]es or [n]o >'.format(current_player)).lower()
    if credit == 'y' or credit == 'yes':
        return main()
    return True

def main():
    '''inform player turn and ask for # sticks to remove
    check to see if player removed the last stick
    if True, inform player he loses
    else continue'''
    sticks,player1,player2 = game_setup()
    while sticks > 0:
        sticks_out = int(input('Hi {}!  There are {} sticks remaining \nPlease select a number of sticks, 1-3 > '.format(player1,sticks)))
        while sticks_out not in range(1,4):
            print('That\'s not a valid move!')
            sticks_out = int(input('As a reminder {} there are {} sticks remaing. \nPlease select a number of sticks, 1-3 > '.format(player1, sticks)))
        sticks = player_move(sticks, sticks_out)
        if sticks < 1:
            if end_game(player1):
                break
        sticks_out = int(input('Hi {}!  There are {} sticks remaining \nPlease select a number of sticks, 1-3 > '.format(player2, sticks)))
        while sticks_out not in range(1,4):
            print('That\'s not a valid move!')
            sticks_out = int(input('As a reminder {} there are {} sticks remaing. \nPlease select a number of sticks, 1-3 > '.format(player2, sticks)))
        sticks = player_move(sticks, sticks_out)
        if sticks <1:
            if end_game(player2):
                break




if __name__ == '__main__':
    main()
