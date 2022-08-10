from Bot import *
from player import *
from board import *

# board
board = Board()
print(board)

# player
player = Player(board)

# bot
bot_symbol = 'x' if player.symbol == 'o' else 'o'
bot = smart_bot(bot_symbol, board)

first_player = player if player.start else bot
second_player = bot if player.start else player

while len(first_player.pos)+len(second_player.pos)<9:
    print('='*50)
    first_player.make_move()
    print(board)
    print('-'*50)
    if check_win(first_player.pos):
        print(f'{first_player} won!')
        break
    elif len(first_player.pos)+len(second_player.pos) == 9:
        print('Tie')
        break
    second_player.make_move()
    print(board)
    if check_win(second_player.pos):
        print(f'{second_player} won!')
        break
    elif len(first_player.pos) + len(second_player.pos) == 9:
        print('Tie')
        break

print('End of Game')


