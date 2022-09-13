#!/usr/bin/env python3

from enum import Enum, auto


class Cell(Enum):
  white_queen = 6
  white_rook = 5
  white_knight = 4
  white_bishop = 3
  white_pawn = 2
  white_king = 1
  empty = 0
  black_king = -1
  black_pawn = -2
  black_bishop = -3
  black_knight = -4
  black_rook = -5
  black_queen = -6

  def is_same_player(self, other):
    return self.value != 0 and self.value < 0 == other.value > 0

def is_inside_board(target_index):
  return target_index >= 0 and target_index < 64


class Board:
    
  def __init__(self):
      self.cells = [
          Cell.black_rook,
          Cell.black_knight,
          Cell.black_bishop,
          Cell.black_queen,
          Cell.black_king,
          Cell.black_bishop,
          Cell.black_knight,
          Cell.black_rook,
          *[Cell.black_pawn] * 8,
          *[Cell.empty] * 4 * 8,
          *[Cell.white_pawn] * 8,
          Cell.white_rook,
          Cell.white_knight,
          Cell.white_bishop,
          Cell.white_queen,
          Cell.white_king,
          Cell.white_bishop,
          Cell.white_knight,
          Cell.white_rook,
      ]
      
      self.white_is_active = True
      self.white_can_castle = True
      self.black_can_castle = True
      self.en_passant = False
  
  
  def is_same_player(self, source_index, target_index):
    return self.cells[source_index].is_same_player(self.cells[target_index])
  
  
  def is_castling_move(self, source_index, target_index):
    return False
  
  
  def is_empty(self, target_index):
    return self.cells[target_index] is Cell.empty
  
  
  def is_my_piece(self, source_index):
    return (self.cells[source_index].value > 0) is self.white_is_active
  
  
  def is_possible_move(self, source_index, target_index):
    return True
  
  
  def is_valid_move(self, source_index, target_index):
      return (is_inside_board(target_index)
          and not self.is_same_player(source_index, target_index)
          and (self.is_empty(target_index) or self.is_castling_move(source_index, target_index))
          and self.is_my_piece(source_index)
          and self.is_possible_move(source_index, target_index)
      )
  

  def make_move(self, source_index, target_index):
      if self.is_valid_move(source_index, target_index):
          self.cells[target_index] = self.cells[source_index]
          self.cells[source_index] = Cell.empty
          return True
      
      return False

  def make_move_str(self, move_str):
      pass


  def __str__(self):
      result = ""

      for i, c in enumerate(self.cells):
          if c.value > 0:
            result += chr(ord('A') + c.value)
          elif c.value < 0:
            result += chr(ord('a') - c.value)
          else:
            result += ' '

          if i % 8 == 7 and i != len(self.cells) - 1:
              result += "\n"

      return result


def main():
    b = Board()
    
    print("Board:")
    print(b)
    
    b.make_move(48, 40)
    
    print("Board:")
    print(b)
    


if __name__ == "__main__":
    main()
