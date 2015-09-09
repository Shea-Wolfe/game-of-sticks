# Getting Started
To run sticks.py, a pvp only game of sticks, on the terminal enter $ python sticks.py

To run ai_sticks.py (recommended), a game with learning ai capiblities, on the terminal enter $ python ai_sticks.py

To run sticks_test.py on the terminal enter $ python sticks_test.py

To run ai_sticks_test.py on the terminal enter $ python ai_sticks_test.py

## Description

Sticks.py is an old version of the code which allows for a game of sticks between two human players for any starting number of sticks from 10-100.  It has since been engulfed by ai_sticks.py and I recommend looking at ai_sticks.py

ai_sticks.py is a program that allows players to play sticks against another player (as above) or against an ai that learns from each game. some features of the game
* On start you can set difficulty, this runs a code where the ai plays itself 0 times (easy), 50 times (medium), or 250 times (hard).  For each game played the ai gets better at the game.  Note, this is the only way to access ai v ai in this game to prevent an endless loop since the ai games don't take any inputs.
* When playing the ai it adds the numbers it used at each count of sticks to it's pick list when it wins and it subtracts the same from its pick list when it loses.  The exception is that the ai will ALWAYS have 1, 2, and 3 in its options for each count of sticks, so if you get very very lucky it can make a bad move after it backs you into a corner (which it is very good at).
* The core game loop runs as thus.
  1. find out if there are 1 or 2 players
  2. find out how many sticks the player wants in the game and gets the player name
  3. Has the first player select a number of sticks to remove (1-3).  Checks to see if the removed sticks lowers the count to 0 or below.  If so declares the current player the loser.
  4. Has the second player select a number of sticks to remove.  If this is ai it selects a random number from its list.  The list is weighted based on past success.  The game then checks to see if player 2 loses
  5. Once the game ends (sticks go to or below 0) the AI updates its dictionary, adding if it won or subtracting if it lost.  The game then asks the player if they want to play again.  If they say yes they are returned to the number of players and name entry.

sticks_test.py is a testing file that examines two functions in sticks.py but since that file is out of date it is not used much.  Use ai_sticks_test instead.

ai_sticks_test.py runs a number of tests on the functions in ai_sticks.py to ensure they are returning expected values.

## Future updates

Code still needs refining.  Once everything was combined the functions got longer than preferred and mucked up readability.  sys.exit() was used because the game wasn't quitting properly, I would like to remove it.
