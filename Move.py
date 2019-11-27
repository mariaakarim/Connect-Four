class Move:

    def __init__(self, row, col):
        """ Initializes a new move with given row and column.
        """
        # === Representation Invariants ===
        # - row >= 1 and row <= 6
        # - col >= 1 and col <= 7

        self.row = row
        self.col = col

    def getRowNum(self):
        """ Returns the row number.
        """
        return self.row

    def getColNum(self):
        """ Returns the column number.
        """
        return self.col

    def is_empty(self, row, col):
        """ Return True iff the position at row and col is an empty slot."
        """

        if self.chessBoard[row][col] == "EMPTY":
            return True
        else:
            return False

    def checkValidMove(self, row, col):
        """ Return True iff the given move at row and col is valid.
        """

        if self.is_empty(row,col):

            return True

        return False



