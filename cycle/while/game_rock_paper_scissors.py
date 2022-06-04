import random

player_wins = 0
comp_wins = 0
for_choice = ['r', 'p', 's']

while player_wins < 3 and comp_wins < 3:
    player = input('Input r or p or s: ')
    comp = random.choice(for_choice)
    if player == comp:
        print('draw')
    elif (player == 'r' and comp == 's') or (player == 's' and comp == 'p') or (player == 'p' and comp == 'r'):
        print('player wins')
        player_wins += 1
    elif (comp == 'r' and player == 's') or (comp == 's' and player == 'p') or (comp == 'p' and player == 'r'):
        print('comp wins')
        comp_wins += 1
    else:
        print('wrong input, try one more time')

if player_wins == 3:
    print('Player WINS!!!!!')
if comp_wins == 3:
    print('Comp WINS!!!!!')

