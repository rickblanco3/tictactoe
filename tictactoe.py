import re

class TicTacToe:
    def __init__(self):
        self._board = []
        for i in range(9):
            self._board.append('-')

    def print_board(self):
        board_str = []

        vals = tuple(self._board[0:3])
        board_str.append("%s|%s|%s" % (vals))
        
        vals = tuple(self._board[3:6])
        board_str.append("%s|%s|%s" % (vals))


        vals = tuple(self._board[6:])
        board_str.append("%s|%s|%s" % (vals))

        print '\n'.join(board_str)

    def add_token(self, token, row, col):
        ''' adds  token X or O to board at row, col
        
        '''
        if token not in ('X','O'):
            raise ValueError("Invalid token. Valid tokens: X, O")
        if row not in range(1,4) or col not in range(1,4):
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
            raise ValueError("There's already a token at %d,%d!" % (row,col))
        

    def is_full(self):
        return '-' not in self._board

    def ai_move(self):
        ''' place an 'O' token at first empty spot on board '''
        if self.is_full():
            raise Error("Board is full!")
        idx = 0
        while self._board[idx] != '-':
            idx += 1
        self._board[idx] = 'O'

    def is_winner(self):
        win_cond = [
                (0,1,2), (3,4,5),(6,7,8),
                (0,3,6), (1,4,7),(2,5,8),
                (0,4,8), (2,4,6)
            ]
        for a,b,c in win_cond:
            if self._board[a] in ('X','O') and \
                self._board[a] == self._board[b] and \
                self._board[b] == self._board[c]:
                    return self._board[a]

        return None


if __name__ == "__main__": 
    t = TicTacToe()

    while not t.is_full():
        player_move = raw_input("Player move row/column (example: 1,1): ")
        if  re.match(r'\d,\d', player_move):
            t.add_token('X', int(player_move[0]), int(player_move[2]))
            t.print_board(); print '\n'
            winner = t.is_winner()
            if winner:                           
                print "Player %s wins!" % winner 
                break
            t.ai_move()
            t.print_board(); print '\n'
            winner = t.is_winner()
            if winner:
                print "Player %s wins!" % winner
                break

        else:
            print "Invalid input! Please try again..."

        


