"""Example code for Tic-tac-toe

3x3 board was described as a list with 9 sequential items.
Each item in the list shows as follows.
 - 'e': empty
 - 'o': circle
 - 'x': cross

For example,
    board = ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']
shows that all cells have empty state.

The index of board[] begins from upper-left to lower-right.
For example,
    board = ['e', 'o', 'e', 'e', 'o', 'x', 'e', 'e', 'e']
describes the state of following.
    'e'|'o'|'e'
    ---+---+---
    'e'|'o'|'x'
    ---+---+---
    'e'|'e'|'e'


Example:
    This module has a test_play(), which executes
        1. prepare an empty board,
        2. play one hand with `o' randomly,
        2. play one hand with `c' randomly.

    case 1:
        % python
        > import tic_tac_toe
        > tic_tac_toe.test_play()

    case 2:
        % python
        > from tic_tac_toe import *
        > test_play()
    case 3:
        % python tic_tac_toe.py
"""

from __future__ import print_function
import random


def init_board():
    """Return the empty board.

    Args:
        None

    Returns:
        list: the empty board with 9 items.

    >>> board = init_board()
    >>> print(board)
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']
    """
    board = []
    index = 1
    while (index <= 9):
        board.append('e')
        index += 1

    return board


def print_board(board):
    """Print the board with 3x3.

    Args:
        board (list): the list with 9 items.

    Returns:
        None (only print the board to sys.stdout (standard output)

    >>> board = init_board()
    >>> print_board(board)
    eee
    eee
    eee
    ---
    """
    count = 0
    for state in board:
        count += 1
        if count % 3 == 0:
            print('{0}'.format(state))
        else:
            print('{0}'.format(state), end='')
    print('---')


def gather_empty_cells(board):
    """Gather empty cells on the board.

    Args:
        board (list): the list with 9 items.

    Returns:
        list: the index list of empty state on the board.

    >>> board = ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'e']
    >>> empty_list = gather_empty_cells(board)
    >>> len(empty_list) == 1
    True
    >>> empty_list[0] == 8
    True
    """
    empty_list = []
    index = 0
    for state in board:
        if state == 'e':
            empty_list.append(index)
        index += 1

    return empty_list


def point_random(board, player):
    """Play one step randomly.

    Args:
        board (list): the list with 9 items.
        player (str): 'o' for circle player, 'x' for cross player

    Returns:
        point (int): the pointed index on the board

    Note:
        This function DOESN'T check the validity of turn.
        You can play oneside-game.

    >>> board = init_board()
    >>> index = point_random(board, 'o')
    >>> board[index] == 'o'
    True
    """
    empty_list = gather_empty_cells(board)
    point = random.randint(0, len(empty_list)-1)
    board[empty_list[point]] = player
    return empty_list[point]

def is_finished(board, player):
    """Return True if the game is finished.

    Args:
        board (list): the list with 9 items.
        player (str): 'o' for circle player, 'x' for cross player

    Returns:
        bool: True if the game is finished, False otherwise.

    >>> board = ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']
    >>> is_finished(board, 'o')
    False
    >>> board = ['o', 'o', 'o', 'e', 'e', 'e', 'e', 'e', 'e']
    >>> is_finished(board, 'o')
    True
    """
    if 'e' in board:
        #行が揃った
        if board[0] == board[1] == board[2] == player:
            return True
        if board[3] == board[4] == board[5] == player:
            return True
        if board[6] == board[7] == board[8] == player:
            return True
        #列が揃った
        if board[0] == board[3] == board[6] == player:
            return True
        if board[1] == board[4] == board[7] == player:
            return True
        if board[2] == board[5] == board[8] == player:
            return True
        
        #斜めが揃った
        if board[0] == board[4] == board[8] == player:
            return True
        if board[2] == board[4] == board[6] == player:
            return True
        
        #条件以外は続行
        return False
    else:
        #セルが全て埋まると引き分け
        return True
    

def play():
    board = init_board()
    print_board(board)
    player = 'o'

    while not is_finished(board, player):
        player = 'o' if board.count('o') < board.count('x') else 'x'
        index = point_random(board, player)
        print("# user '{0}' pointed to board[{1}]".format(player, index))
        print_board(board)

    print("Game is finished")
    return 0


if __name__ == '__main__':
    play()