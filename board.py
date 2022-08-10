
class Board():
    """
    Represents a board object with 3x3 squares

    Instance attributes:
        xs: list of ints (0-8) which represents player x's positions,
            need not be ordered
        os: list of ints (0-8) which represents player o's positions,
            need not be ordered
    """

    def __init__(self):
        """
        Writes the attributes xs and os as empty to start the game
        """
        self.xs = []
        self.os = []

    def __repr__(self):
        """
        Returns the current pictorial state of the game
        """
        rows = ["   |   |   "]*3
        for player,symbol in zip([self.xs, self.os],['x','o']):
            for pos in player:
                r_num = pos // 3
                c_num = pos % 3
                rows[r_num] = rows[r_num][:1+4*c_num]+symbol+rows[r_num][2+4*c_num:]

        return "\n".join(rows)

    def add_x(self, pos):
        """
        Modifies self.xs to include the new position

        precondition: pos is an int (0-8) whih represents
                    a position on the board, and is not occupied
        """
        assert type(pos) in [int, bool] and pos>=0 and pos<=8
        assert pos not in self.xs+self.os

        self.xs.append(pos)

    def add_o(self, pos):
        """
        Modifies self.xs to include the new position

        precondition: pos is an int (0-8) whih represents
                    a position on the board, and is not occupied
        """
        assert type(pos) in [int, bool] and 0 <= pos <= 8
        assert pos not in self.xs + self.os

        self.os.append(pos)

