import random
def game_setup(players):
    '''Takes one arguement, the players (one or two).
    Gets the player names and how many sticks the game will be played with'''

    if players == 1:
        sticks = int(input('Welcome to the game how many sticks are on the table?\nEnter a number between 10-100? > '))
        player1 = input('Great! player 1 please enter your name > ')
        player2 = 'Skynet'
    else:
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

def end_game(current_player, ai_dict):
    '''Takes the losing player as an arguements
    checks to see if the player wants to play again, if yes it runs the main loop
    if no it breaks the main loop which exits the program.'''
    print(ai_dict)
    credit = input('You lose {}!  Would you like to play again? enter [y]es or [n]o >'.format(current_player)).lower()
    if credit == 'y' or credit == 'yes':
        return main(ai_dict)
    return True

def ai_dict_changes(ai_dict, ai_choices, ai_win):
    '''This function takes the set dictionary, the choices it's made in the game and if it won.
    It returns a dictionary that has been changed based on the guesses and if it won
    or didn't win'''
    if ai_win:
        for key in ai_choices:
            ai_dict[key].append(ai_choices[key])
    else:
        for key in ai_choices:
            if ai_dict[key].count(ai_choices[key]) == 1:
                pass
            else:
                ai_dict[key].remove(ai_choices[key])
    return ai_dict

def ai_turn(ai_dict, sticks, ai_choices):
    '''Takes two arguements, the AI dictionary and the number of sticks in the pile
    returns a random selection from remaining values at that key in the ai dict'''
    current_guess = random.choice(ai_dict[sticks])
    ai_choices[sticks] = current_guess
    return (current_guess, ai_choices)

def get_ai_dict():
    '''Takes no input.  Returns a dictionary with keys from 1-100.
    Value for each key is the same, a list of ints one two and three.'''
    return {key: [1,2,3] for key in range(1,101)}


def main(ai_dict):
    '''inform player turn and ask for # sticks to remove
    check to see if player removed the last stick
    if True, inform player he loses
    else continue'''
    ai_choices = {}
    sticks,player1,player2 = game_setup(1)
    while sticks > 0:
        sticks_out = int(input('Hi {}!  There are {} sticks remaining \nPlease select a number of sticks, 1-3 > '.format(player1,sticks)))
        while sticks_out not in range(1,4):
            print('That\'s not a valid move!')
            sticks_out = int(input('As a reminder {} there are {} sticks remaing. \nPlease select a number of sticks, 1-3 > '.format(player1, sticks)))
        sticks = player_move(sticks, sticks_out)
        if sticks < 1:
            ai_dict = ai_dict_changes(ai_dict, ai_choices, True)
            if end_game(player1, ai_dict):
                break
        sticks_out, ai_choices = ai_turn(ai_dict, sticks, ai_choices)
        sticks = player_move(sticks, sticks_out)
        if sticks <1:
            ai_dict = ai_dict_changes(ai_dict, ai_choices, False)
            if end_game(player2, ai_dict):
                break




if __name__ == '__main__':
    ai_dict = get_ai_dict()
    main(ai_dict)
