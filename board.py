import numpy as np

class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.cols = columns
        self.board = np.zeros((rows, columns))

    def place_disk(self, row, col, disk):
        if(self.is_valid_location(row, col)):
            self.board[self.rows - row -1][col] = disk

    def is_valid_location(self, row, col):
        return self.board[self.rows - row -1][col] == 0

    def print_board(self):
        print(self.board)

    def get_next_open_row(self, col):
        for row in range(self.rows):
            if self.board[self.rows-1-row][col] == 0:
                return row

    def check_winner(self, player, row, col):
        if self.check_horizontal(row, col,  player) or self.check_vertical(row, col, player):
            return True
        return False

    def check_horizontal(self, row, col, player):
        pos = self.rows - row - 1
        total = 0
        #check left
        while pos > 0:
            if (self.board[pos][col] == player):
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



