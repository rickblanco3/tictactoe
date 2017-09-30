''' tictactoe.py
    ------------
    play tic-tac-toe in the command-line
    against the CPU

                                    '''

import re

class TicTacToe:
    '''
        creates and runs a game of tic-tac-toe.
        -player X is the user
        -player O is the CPU
                                    '''
    def __init__(self):
        '''
        Create the empty game board
                                    '''
        self._board = ['-']*9

    def __str__(self):
        board_str = []
        vals = tuple(self._board[0:3])
        board_str.append("%s|%s|%s" % (vals))
        vals = tuple(self._board[3:6])
        board_str.append("%s|%s|%s" % (vals))
        vals = tuple(self._board[6:])
        board_str.append("%s|%s|%s" % (vals))
        return "\n".join(board_str)

    def add_token(self, token, row, col):
        '''
            adds  token X or O to board at row, col
                                                '''
        if token not in ('X', 'O'):
            raise ValueError("Invalid token. Valid tokens: X, O")
        if row not in range(1, 4) or col not in range(1, 4):
            raise ValueError("Invalid row & column combination. Valid values: 1 through 3")

        board_idx = None
        if row == 1:
            board_idx = col - 1
        elif row == 2:
            board_idx = col + 2
        elif row == 3:
            board_idx = col + 5

        if self._board[board_idx] == '-': # empty
            self._board[board_idx] = token
        else:
            raise ValueError("There's already a token at %d,%d!" % (row, col))

    def is_board_full(self):
        return '-' not in self._board

    def ai_move(self):
        ''' place an 'O' token at first empty spot on board '''
        if self.is_board_full():
            raise ValueError("Board is full!")
        idx = 0
        while self._board[idx] != '-':
            idx += 1
        self._board[idx] = 'O'

    def get_winner(self):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
            ]
        for a_val, b_val, c_val in win_conditions:
            if self._board[a_val] in ('X', 'O') and \
                self._board[a_val] == self._board[b_val] and \
                self._board[b_val] == self._board[c_val]:
                return self._board[a_val]
        return None


def main():
    game = TicTacToe()
    while not game.is_board_full():
        player_move = raw_input("Player move row/column (example: 1,1): ")
        if  re.match(r'\d,\d', player_move):
            game.add_token('X', int(player_move[0]), int(player_move[2]))
            print(str(game)+"\n")
            winner = game.get_winner()
            if winner:
                print("Player %s wins!" % winner)
                break
            game.ai_move()
            print(str(game)+"\n")
            winner = game.get_winner()
            if winner:
                print("Player %s wins!" % winner)
                break

        else:
            print("Invalid input! Please try again...")

if __name__ == "__main__":
    main()
