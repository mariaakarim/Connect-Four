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
        return None
