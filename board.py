import numpy as np


class Board:

    def __init__(self, rows, columns):
        """ Initialize a the board with the given rows and columns

        """
        self.rows = rows
        self.cols = columns
        self.board = np.zeros((rows, columns))

    def place_disk(self, row, col, disk):
        """  Place a disk on the board at the given row and col.
        """

        if self.is_valid_location(row, col):
            self.board[self.rows - row -1][col] = disk

    def is_valid_location(self, row, col):
        """ Return True iff the position at the given row and col
        the board is 0.
        """

        return self.board[self.rows - row -1][col] == 0

    def print_board(self):
        """Print the Connect Four Board
        """

        print(self.board)

    def get_next_open_row(self, col):
        """ Return the next open row in the given column
        """

        for row in range(self.rows):
            if self.board[self.rows-1-row][col] == 0:
                return row

    def check_winner(self, player, row, col):
        """ Return True iff the player is a winner at the given
        row and column and has 4 consecutive disks.
        """

        if self.check_horizontal(row, col,  player) or \
                self.check_vertical(row, col, player) or self.check_diagonal(row, col, player):
            return True
        return False

    def check_horizontal(self, row, col, player):
        """ Return True iff the player has 4 consecutive disks
        in the horizontal direction.
        """

        pos = self.rows - row - 1
        total = 0
        #check left
        while pos > 0:
            if self.board[pos][col] == player:
                total += 1
            else:
                break
            pos -= 1

        pos = self.rows - row

        while pos < self.rows:
            if self.board[pos][col] == player:
                total += 1
            else:
                break
            pos += 1

        if total == 4:
            return True
        return False

    def check_vertical(self, row, col, player):
        """ Return True iff the player has 4 consecutive disks
        in the vertical direction.
        """

        c = col
        r = self.rows - row - 1
        total = 0
        while c > 0:
            if self.board[r][c] == player:
                total += 1
            else:
                break
            c -= 1
        c = col + 1

        while c < self.cols:
            if self.board[r][c] == player:
                total += 1
            else:
                break
            c += 1
        if total == 4:
            return True
        return False

    def check_diagonal(self, row, col, player):
        """ Return True iff the player has 4 consecutive disks
        in the diagonal direction.
        """

        curr_row = self.rows - row - 1
        curr_col = col
        disk_total = 0

        while curr_row > 0:
            while curr_col > 0:
                if self.board[curr_row][curr_col]==player:
                    disk_total+=1
                curr_col -= 1
            curr_row -= 1

        curr_col = col + 1
        curr_row = self.rows - row

        while curr_row < self.rows:
            while curr_col < self.cols:
                if self.board[curr_row][curr_col] == player:
                    disk_total += 1
                curr_col += 1
            curr_row += 1
        if disk_total == 4:
            return True
        return False





