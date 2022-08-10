from board import Board
from utils import check_win, minimax

class bot():
    """
    Parent class bot

    instance attributes:
        board: [board.Board] initially empty at the start of the game
        symbol: [str] either 'x' or 'o', the opposite of the player
        starting: [bool] whethe rthe bot start first, defaut False
    """

    def __init__(self,symbol:str,board:Board):
        """
        Instantiates attributes into object
        """
        self.board = board
        self.symbol = symbol
        self.pos = board.xs if self.symbol == 'x' else board.os


    def add_pos(self,pos:int):
        """
        Modifies the bot's postion to include the new position
        :param pos: [int] valid position on board
        """
        assert type(pos) == int and 0<=pos<=8
        assert pos not in self.board.xs + self.board.os

        self.pos.append(pos)


class smart_bot(bot):
    """
    Bot that uses the minimax algorithm
    """

    def make_move(self):
        """
        Appends next move of the bot based on the current state
        of the board using the minimax algorithm to the bot's pos
        """
        bot_pos = self.board.xs if self.symbol == 'x' else self.board.os
        player_pos = self.board.os if self.symbol == 'x' else self.board.xs

        _, best_next_pos = minimax(bot_pos, player_pos, True, 0)
        self.add_pos(best_next_pos)



    def __repr__(self):
        return f'Smart Bot {self.symbol}'



