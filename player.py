from board import Board

class Player():
    """
    Represents the player

    Instance attributes:
        board: [Board] board object that game is on
        symbol: [str] symbol that the player so chooses
        start: [bool] whether the player starts first
    """
    def __init__(self, board):

        self.symbol = self.add_symbol()
        self.start = self.add_start()
        self.board = board
        self.pos = board.xs if self.symbol == 'x' else board.os

    def input_move(self):
        """
        ask for user input for next position
        """
        try:
            player_pos = int(input('Position to take [0-8]:'))
            if player_pos not in range(9):
                raise ValueError
            if player_pos in self.board.xs + self.board.os:
                raise IndexError
            return player_pos
        except ValueError:
            print(f'Ensure valid integer between 0 and 8 inclusive')
            return self.input_move()
        except IndexError:
            print(f'Ensure position is not occupied, you typed {player_pos}')
            return self.input_move()

    def make_move(self):
        """
        Ask user for move and adds to self position
        """
        users_move = self.input_move()
        self.pos.append(users_move)

    def add_symbol(self):
        """
        Ask for user input for symbol and return symbol
        """
        try:
            player_symbol_choice = input('Choice of symbol [x,o]: ').strip().lower()
            if player_symbol_choice not in ['x','o']:
                raise ValueError
            return player_symbol_choice

        except ValueError:
            print(f'Choice of symbol should be either \'x\' or \'o\', you typed {player_symbol_choice}')
            return self.add_start()

    def add_start(self):
        """
        Ask whether player wants to start first and return bool
        """
        try:
            player_start = input('Do you want to start [Y/N]?: ').upper().strip()
            if player_start not in ['Y','N']:
                raise ValueError
            return player_start == 'Y'

        except:
            print(f'Requires \'Y\' or \'N\', you typed {player_start}')
            return self.add_start()

    def __repr__(self):
        return f'Player [{self.symbol}]'

