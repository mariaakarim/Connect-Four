import numpy as k

Row_Count = 6
Col_count = 7

def create_board():
  board = k.zeros((6,7))
  return board


def drop_piece(board, row, col, piece):
  board[row][col] = piece
  
  
def is_valid_location():
  pass
  
def print_board(board):
  pass
