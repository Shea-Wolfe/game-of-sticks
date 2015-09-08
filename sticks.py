'''Game setup:
X pick number of sticks
X take player names

Game loop:
X inform player turn and ask for removal
check to see if player removed the last sticks
if True, inform player he loses
else continue'''

def game_setup():
    sticks = int(input('Welcome to the game how many sticks are on the table?\nEnter a number between 10-100? > '))
    player1 = input('Great! player 1 please enter your name > ')
    player2 = input('Awesome! Player 2 please enter your name > ')
    return (sticks, player1, player2)

def game_loop(sticks, current_player):
    player_move = int(input('Hi {}! Please select a number of sticks, 1-3'.format(current_player)))
    if player_move < 1 or player_move > 3:
        print('That\'s not a valid move!')
        return game_loop(sticks, current_player)
    return sticks -= player_move

def main():
    pass


if __name__ == '__main__':
    main()
