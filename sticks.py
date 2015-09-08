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

def player_move(sticks, player_move):
    if player_move < 1 or player_move > 3:
        print('That\'s not a valid move!')
        return player_move(sticks)
    sticks -= player_move
    return sticks

def end_game(current_player):
    pass

def main():
    sticks,player1,player2 = game_setup()
    while sticks > 0:
        sticks_out = int(input('Hi {}! Please select a number of sticks, 1-3'.format(player1)))
        while player_move  not in range(1,4):
            print('That\'s not a valid move!')
            player_move = int(input('Hi {}! Please select a number of sticks, 1-3'.format(player1)))
        player_move(sticks, sticks_out)
        if sticks < 1:
            end_game(player1)
        sticks_out = int(input('Hi {}! Please select a number of sticks, 1-3'.format(player1)))
        while player_move  not in range(1,4):
            print('That\'s not a valid move!')
            player_move = int(input('Hi {}! Please select a number of sticks, 1-3'.format(player1)))
        player_move(sticks, sticks_out)
    end_game(player2)




if __name__ == '__main__':
    main()
