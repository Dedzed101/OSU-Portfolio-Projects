# Name: Daniel Bracamontes
# Date: 12/1/2020
# Description: A class that allows two people to simulate a board game.

class BuildersGame():
    '''A class that initializes a game board as a list of lists, the current status of the game, whose turn it is, and the board coordinates of each player piece.
        Player X builder coordinates: xb1 and xb2. Player O builder coordinates ob1 nad ob2. Initialized at none.
    '''

    def __init__(self):
        self._board = [[0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0]]

        self._current_state = "UNFINISHED"
        self._turn = 'x'
        self._xb1 = 0
        self._xb2 = 0
        self._ob1 = 0
        self._ob2 = 0

    def get_current_state(self):
        '''Returns the game status.
        '''
        return self._current_state

    # Print board
    '''
    def print_board(self):
        for lists in self._board:
            for i in lists:
                print(i,end='\t')
            print()
    '''

    def initial_placement(self, r1, c1, r2, c2, player):
        '''Initial placement: r for row, c for column, player. When it's a given player's turn, then the arguments passed are held as strings and each builder's
        coordinates are updated. If positions are already occupied, then False is returned.
        '''
        if player == 'x' and self._turn != 'o':
            self._xb1 = str(r1) + str(c1)
            self._xb2 = str(r2) + str(c2)
            self._turn = 'o'
            return True

        elif player == 'o' and self._turn != 'x':
            coord_ob1 = str(r1) + str(c1)
            coord_ob2 = str(r2) + str(c2)
            self._turn = 'x'

            if coord_ob1 != self._xb1 and coord_ob2 != self._xb1 and coord_ob1 != self._xb2 and coord_ob2 != self._xb2:
                self._ob1 = coord_ob1
                self._ob2 = coord_ob2
                return True

            else:
                return False
        else:
            return False

    def _is_adjacent(self, r1, c1, r2, c2):
        '''Adding a method to determine if positions are adjacent, to be called later in the make_move method.
        '''
        if (r1 == r2 and c1 + 1 == c2) \
                or (r1 == r2 and c1 - 1 == c2)\
                or (r1 + 1 == r2 and c1 - 1 == c2)\
                or (r1 + 1 == r2 and c2 == c1)\
                or (r1 + 1 == c2 and c1 + 1 == c2)\
                or (r1 - 1 == r2 and c1 - 1 == c2)\
                or (r1 - 1 == r2 and c1 == c2) \
                or (r1 - 1 == r2 and c1 + 1 == c2):

            return True

        else:

            return False

    def make_move(self, r1, c1, r2, c2, r3, c3):
        '''Make_move determines whose turn it is. If it's X's turn then it updates the data member and vice versa.
                Then determines if the player location passed belongs to the other player. If it does, it returns false. 
                    Then determines if the player destination passed belongs to the other player or already has a piece on it. If it does, it returns false.
                        Then it checks to see how tall the builing is on the intended destination space. If it's not a legal height, it returns false.
                            Then it checks to see if it can add a level to an adjacent position. If the necessary critiria are met, a winner is declared.
            Repeat for second players turn.
        '''
        player_location = str(r1) + str(c1)
        player_destination = str(r2) + str(c2)

        if self._turn == 'x':
            self._turn = 'o'
            return True

            if player_location != self._ob1 and player_location != self._ob2:

                if self._ob1 != player_destination and self._ob2 != player_destination and self._xb1 != player_destination and self._xb2 != player_destination:

                    if self._board[r2][c2] - self._board[r1][c1] < 2:

                        if self._is_adjacent(r2, c2, r3, c3):
                            if self._xb1 == player_location:
                                self._xb1 = player_destination
                            else:
                                self._xb2 = player_destination

                            if self._board[r2][c2] != 3 or 4:
                                self._board[r3][c3] += 1
                                return True

                            if self._board[r2][c2] == 3:
                                self._current_state = 'X_WON'
                                return True

                            if self._board[r2][c2] != 3 and self._board[r2][c2] == 4:
                                self._current_state = 'O_WON'
                                return True
                        else:
                            self._turn = 'x'
                            return False
                    else:
                        self._turn = 'x'
                        return False
                else:
                    self._turn = 'x'
                    return False
            else:
                self._turn = 'x'
                return False

        elif self._turn == 'o':
            self._turn = 'x'
            return True

            if self._xb1 != player_location and self._xb2 != player_location:

                if self._ob1 != player_destination and self._ob2 != player_destination and self._xb1 != player_destination and self._xb2 != player_destination:

                    if self._board[r2][c2] - self._board[r1][c1] < 2:

                        if self._is_adjacent(r2, c2, r3, c3):
                            if self._ob1 == player_location:
                                self._ob1 = player_destination
                            else:
                                self._ob2 = player_destination

                            if self._board[r2][c2] != 3 or 4:
                                self._board[r3][c3] += 1
                                return True

                            if self._board[r2][c2] == 3:
                                self._current_state = 'O_WON'
                                return True

                            if self._board[r2][c2] != 3 and self._board[r2][c2] == 4:
                                self._current_state = 'X_WON'
                                return True

                        else:
                            self._turn = 'o'
                            return False
                    else:
                        self._turn = 'o'
                        return False
                else:
                    self._turn = 'o'
                    return False
            else:
                self._turn = 'o'
                return False
        else:
            return False


# Testing

game = BuildersGame()
game.initial_placement(2, 2, 1, 2, 'x')
game.initial_placement(0, 1, 4, 2, 'o')

# game.make_move(2,2,1,1,1,0) #x
# game.make_move(0,1,1,0,2,0) #o

# game.make_move(1,2,2,0,3,0) #x
# game.make_move(1,0,0,1,0,0) #o

# game.make_move(2,0,1,0,0,0) #x
# game.make_move(4,2,4,3,3,3) #o

# game.make_move(1,0,2,0,2,1) #x
# game.make_move(4,3,3,3,3,2) #o

# game.make_move(2,0,2,1,1,0) #x
# game.make_move(3,3,3,2,2,3) #o

# game.make_move(2,1,1,1,2,0) #x
# game.make_move(3,2,3,3,3,4) #o

# game.make_move(1,1,2,0,3,0) #x
# game.make_move(3,3,2,2,2,3) #o

# game.make_move(2,0,1,0,0,0) #x
# game.make_move(2,2,3,1,4,1) #o

# game.make_move(1,0,0,0,1,1)
# game.make_move(1,0,2,0,1,1)

# b = game.get_current_state()
# a = game.print_board()
# print(b)
# #print(b)
