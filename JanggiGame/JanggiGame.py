# Daniel Bracamontes
# 3/11/2021
# Write a Janggi Game

# Scenario Descriptions:
#
#
# 1. Initializing the board
#       Game board is initialized by JanggiGame, which assigns algebraic positions as keys, and strings representing pieces (or empty spaces) as values.  
#      
# 2. Determining how to represent pieces at a given location on the board
#       All pieces are initialized in their starting positions on the game board by a piece name and color (ie. BlGen, RdGen) within the initiialized dictionary. When a move
#       is to be made, the make_move fucntion passes the inforamtion to the pieces class, which translates the gameboard values into coordinates that can be referenced by the piece classes
#       when making moves.
#
# 3. Determining how to validate a given move according to the rules for each piece, turn taking and other game rules.
#       make_move method in JanggiGame takes the move and refers to the current game board to determine the piece at that position, it
#       then checks the current players turn and continues if the given position holds a piece that is allowable for that player. It then 
#       refers to the movement capability of the piece occupying the space (by checking the valid_move function in the relevent piece class) 
#       and determines if the move is valid, based on the rules of that piece (eache move should also check if the player's general will be left in check, if 
#       so, the move returns False ****I didn't get to this fucntionality****). If so, it updates the dictionary with the new values associated with the starting 
#       and ending position ('empty' and the moved piece, respectively). It then updates the player turn and returns True. If the move is invalid, the piece class returns False. 
#
# 4. Modifying the board state after each move.
#       make_move method ends by updating the board state by updating the dictionary in the JanggiGame class (by referencing the variable name that is passed as a parameter in the make_move function).
#
# 5. Determining how to track which player's turn it is to play right now.
#       Update the player turn after every valid move in make_move.
#
# 6. Determining how to detect the checkmate scenario.
#       Ideally, a function would be called at the beginning of a turn that determines if the player is in check, by seeing if their general's current position can be legally accessed
#       by an opposing player piece. If so, another function is called that checks every move available to the player's general, by seeing if any of those positions can be legally accessed by 
#       an opposing piece or the defending players pieces. Any move that is not in danger increments a count. If that count is greater than 0 it means there are moves available that can save 
#       the general. If the count is 0, then it means the general is in checkmate, and make_move updates the game state to reflect who won. The turn ends and from there, no more moves can be made.  
#       ***I was having alot of trouble conceptualizing this and didn't really figure it out in time :( ...still working on it though.  
#
# 7. Determining which player has won and also figuring out when to check that.
#       see above


class JanggiGame:
    """
    Initializes game elements, like board, game_state, player_turn, and if either player is in check. 
    make_move function manages game playability and determines move validity.
    """

    def __init__(self):
        """
        Initialize data members. 
        Game starts 'UNFINISHED'. Blue player starts.
        Player blue and red initialized to False, when determining if they are in check.
        Columns:  a-i, rows: 1-10  ; 1 is Red Side, 10 is Blue Side.
        Palace on each side with diagonal capability
        """
        self._game_state = "UNFINISHED"
        #Game board initialized as dictionary, keys are position, values are piece name or empty.
        self._game_board = {     'a1': 'RdCha', 'b1': 'RdEle', 'c1': 'RdHor', 'd1': 'RdGrd', 'e1': '-----', 'f1': 'RdGrd', 'g1': 'RdEle', 'h1': 'RdHor', 'i1': 'RdCha',                
                                 'a2': '-----', 'b2': '-----', 'c2': '-----', 'd2': '-----', 'e2': 'RdGen', 'f2': '-----', 'g2': '-----', 'h2': '-----', 'i2': '-----',                 
                                 'a3': '-----', 'b3': 'RdCan', 'c3': '-----', 'd3': '-----', 'e3': '-----', 'f3': '-----', 'g3': '-----', 'h3': 'RdCan', 'i3': '-----',                 
                                 'a4': 'RdSol', 'b4': '-----', 'c4': 'RdSol', 'd4': '-----', 'e4': 'RdSol', 'f4': '-----', 'g4': 'RdSol', 'h4': '-----', 'i4': 'RdSol',                 
                                 'a5': '-----', 'b5': '-----', 'c5': '-----', 'd5': '-----', 'e5': '-----', 'f5': '-----', 'g5': '-----', 'h5': '-----', 'i5': '-----',
                                 'a6': '-----', 'b6': '-----', 'c6': '-----', 'd6': '-----', 'e6': '-----', 'f6': '-----', 'g6': '-----', 'h6': '-----', 'i6': '-----',
                                 'a7': 'BlSol', 'b7': '-----', 'c7': 'BlSol', 'd7': '-----', 'e7': 'BlSol', 'f7': '-----', 'g7': 'BlSol', 'h7': '-----', 'i7': 'BlSol',                 
                                 'a8': '-----', 'b8': 'BlCan', 'c8': '-----', 'd8': '-----', 'e8': '-----', 'f8': '-----', 'g8': '-----', 'h8': 'BlCan', 'i8': '-----',                 
                                 'a9': '-----', 'b9': '-----', 'c9': '-----', 'd9': '-----', 'e9': 'BlGen', 'f9': '-----', 'g9': '-----', 'h9': '-----', 'i9': '-----',                 
                                 'a0': 'BlCha', 'b0': 'BlEle', 'c0': 'BlHor', 'd0': 'BlGrd', 'e0': '-----', 'f0': 'BlGrd', 'g0': 'BlEle', 'h0': 'BlHor', 'i0': 'BlCha'
        }
        self._blue_general = ['BlGen']
        self._red_general = ['RdGen']
        self._player_turn = "Blue"
        self._player_blue_in_check = False
        self._player_red_in_check = False
    
    def get_game_state(self):
        """
        Return 'UNFINISHED', or "RED_WON", or "BLUE_WON", or "DRAW"
        """
        return self._game_state
    
    #def blue_in_check(self, true):
        #if true == True:
        #    self._player_blue_in_check == True
    
    def is_in_check(self, player):
        """
        method called is_in_check, takes parameter ('red' or 'blue') return True if in Check and False if not.
        Check the given player's General and check True or False.
        """
        if player == 'blue':
            if self._player_blue_in_check == True:
                return True
            else:
                return False
        if player == 'red':
            if self._player_red_in_check == True:
                return True
            else:
                return False
    
    def print_board(self):
        """
        Print board. Slices the game board dictionary into a series of lists representing a numbered row.
        For the purposes of printing and testing.
        """
        print(list(self._game_board.items())[0:9])
        print(list(self._game_board.items())[9:18])
        print(list(self._game_board.items())[18:27])
        print(list(self._game_board.items())[27:36])
        print(list(self._game_board.items())[36:45])
        print(list(self._game_board.items())[45:54])
        print(list(self._game_board.items())[54:63])
        print(list(self._game_board.items())[63:72])
        print(list(self._game_board.items())[72:81])
        print(list(self._game_board.items())[81:90])
                  
    def make_move(self, pos_1, pos_2):
        """
        method called make_move that takes two parameters (strings that represent the square to move from, and
        the square to move to). 
        Check position 1 and determine what piece is there, check the rules of that piece and continue, based
        on position 2. 
        If valid, make move, capture piece if applicable, update player_turn, and game_state if necessary and return True. 
        If invalid move, return False. 
        If paramter 1 = parameter 2, it is considered a pass, and game state updates to next player. Return True.
        
        """
        blue_pieces = ['BlSol', 'BlCha', 'BlCan', 'BlEle', 'BlHor', 'BlGrd', 'BlGen']
        red_pieces = ['RdSol', 'RdCha', 'RdCan', 'RdEle', 'RdHor', 'RdGrd', 'RdGen']
        
        #If the game has been won or drawn, no more moves can be made
        if self._game_state != "UNFINISHED":
            return False
        
        #Converting a parameter assignation that takes place at row 10 to 0, for sake of print_board legibility.
        if pos_1 in ['a10', 'b10','c10','d10','e10','f10','g10','h10','i10']:
            pos_1 = str(pos_1[0]) + str(pos_1[2])
        
        if pos_2 in ['a10', 'b10','c10','d10','e10','f10','g10','h10','i10']:
            pos_2 = str(pos_2[0]) + str(pos_2[2])
        
        #If a player wants to skip their turn, then pos_1 will equal pos_2
        if pos_1 == pos_2:
            if self._player_turn == "Blue":
                self._player_turn = "Red"
                return True
            if self._player_turn == "Red":
                self._player_turn = "Blue"
                return True
            
        #If Blue player's turn
        if self._player_turn == "Blue":   
            piece = self._game_board.get(pos_1)  #Take pos_1 and pos_2 check all dictionary keys for values, and assign them to variables
            destination = self._game_board.get(pos_2)  
            if destination in blue_pieces:           #If player wants to move to a position occupied by a friendly piece, return False
                return False
            if piece not in blue_pieces:             #if value at pos_1 not in blue_pieces - return False
                return False
            #TODO: Check if BlGen is in check:
            #Bl_Gen_position = #call a function to find BlGen
            # BlGen_in_check = General().is_in_check(BlGen_position)
            # if BlGen_in_check == True: 
                #Call General in_check function from General class, return number of available moves, if > 0, then return True, else, update "RED_WON".
            #Check rules of piece, if pos_1 to pos_2 is a valid move, return True and proceed, else return False
            #If a move puts the BlGen in check, it should return False. Every piece class should check if making the move will put the Gen in check, return False if so
            if Pieces().valid_move(piece, pos_1, pos_2, self._game_board, self._player_blue_in_check, self._player_red_in_check) == True:
                self._game_board.update({pos_1: '-----'})
                self._game_board.update({pos_2: piece})
                #TODO: Check if opposing Gen is in check, if so update in_check status of opponant
                self._player_turn = "Red"
            else:
                return False
            return True  
        
        #If Red player's turn
        if self._player_turn == "Red":
            piece = self._game_board.get(pos_1)  #Take pos_1 and pos_2 check all dictionary keys for value, and assign them to variables
            destination = self._game_board.get(pos_2)
            if destination in red_pieces:            #If player wants to move to a position occupied by a friendly piece, return False
                return False
            if piece not in red_pieces:              #if value at pos_1 not in red_pieces - return False
                return False
            #TODO: Check if RdGen is in check:
            #Rd_Gen_position = #call a function to find BlGen#
            # RdGen_in_check = General().is_in_check(BlGen_position)
            # if RdGen_in_check == True:
                #Call General in_check function from General class, return number of available moves, if > 0, then return True, else, update "BLUE_WON".
            #Check rules of piece, if pos_1 to pos_2 is a valid move, return True and proceed, else return False
            #If a move puts the RdGEn in check, it should return False. Every piece class should check if making the move will put the Gen in check, return False if so
            if Pieces().valid_move(piece, pos_1, pos_2, self._game_board, self._player_blue_in_check, self._player_red_in_check) == True:
                self._game_board.update({pos_1: '-----'})
                self._game_board.update({pos_2: piece})
                #TODO: Check if opposing Gen is in check, if so update in_check status of opponant
                self._player_turn = "Blue"
            else:
                return False
            return True       

class Pieces(JanggiGame):
    """   
    Pieces (per team).
    Pieces initializes a gameboard represnted by coordinates for sake of piece movement.
    Each piece will be its own class that will be called by the JanggiGame class.
    Recieves information from JanggiGame to pass to valid_move function to determine mover validity.
    """

    def __init__(self):
        """
        Initialize a game board comprised of coordinates in tuple form, to be translated from the strings input by the user.
        Initialize a red and blue palace, to faciliate checking of move validity when pieces are in a palace.
        """
        #Game Board as coordinate tuples
        self._game_board_coords = { 'a1': (1, 1), 'b1': (2, 1), 'c1': (3, 1), 'd1': (4, 1), 'e1': (5, 1), 'f1': (6, 1), 'g1': (7, 1), 'h1': (8, 1), 'i1': (9, 1),                
                                    'a2': (1, 2), 'b2': (2, 2), 'c2': (3, 2), 'd2': (4, 2), 'e2': (5, 2), 'f2': (6, 2), 'g2': (7, 2), 'h2': (8, 2), 'i2': (9, 2),                 
                                    'a3': (1, 3), 'b3': (2, 3), 'c3': (3, 3), 'd3': (4, 3), 'e3': (5, 3), 'f3': (6, 3), 'g3': (7, 3), 'h3': (8, 3), 'i3': (9, 3),                 
                                    'a4': (1, 4), 'b4': (2, 4), 'c4': (3, 4), 'd4': (4, 4), 'e4': (5, 4), 'f4': (6, 4), 'g4': (7, 4), 'h4': (8, 4), 'i4': (9, 4),                 
                                    'a5': (1, 5), 'b5': (2, 5), 'c5': (3, 5), 'd5': (4, 5), 'e5': (5, 5), 'f5': (6, 5), 'g5': (7, 5), 'h5': (8, 5), 'i5': (9, 5),
                                    'a6': (1, 6), 'b6': (2, 6), 'c6': (3, 6), 'd6': (4, 6), 'e6': (5, 6), 'f6': (6, 6), 'g6': (7, 6), 'h6': (8, 6), 'i6': (9, 6),
                                    'a7': (1, 7), 'b7': (2, 7), 'c7': (3, 7), 'd7': (4, 7), 'e7': (5, 7), 'f7': (6, 7), 'g7': (7, 7), 'h7': (8, 7), 'i7': (9, 7),                 
                                    'a8': (1, 8), 'b8': (2, 8), 'c8': (3, 8), 'd8': (4, 8), 'e8': (5, 8), 'f8': (6, 8), 'g8': (7, 8), 'h8': (8, 8), 'i8': (9, 8),                 
                                    'a9': (1, 9), 'b9': (2, 9), 'c9': (3, 9), 'd9': (4, 9), 'e9': (5, 9), 'f9': (6, 9), 'g9': (7, 9), 'h9': (8, 9), 'i9': (9, 9),                 
                                    'a0': (1, 10), 'b0': (2, 10), 'c0': (3, 10), 'd0': (4, 10), 'e0': (5, 10), 'f0': (6, 10), 'g0': (7, 10), 'h0': (8, 10), 'i0': (9, 10)
                                    }
        #List of pieces
        self._soldiers = ['RdSol', 'BlSol'] 
        self._chariots = ['RdCha', 'BlCha'] 
        self._horses =   ['RdHor', 'BlHor'] 
        self._elephants = ['RdEle', 'BlEle'] 
        self._guards = ['RdGrd', 'BlGrd'] 
        self._cannons = ['RdCan', 'BlCan'] 
        self._generals = ['RdGen', 'BlGen']
        
        #Red Palace Information
        self._red_palace_center = [(5, 2)]
        self._red_palace_left_diagonals = [(4, 1), (4, 3)]
        self._red_palace_right_diagonals = [(6, 1), (6, 3)]
        self._red_palace_inner_diagonals = [(4, 3), (6, 3)]
        self._red_palace_outer_diagonals = [(4, 1), (6, 1)]
        self._red_palace = [(4, 1), (5, 1), (6, 1),
                            (4, 2), (5, 2), (6, 2),
                            (4, 3), (5, 3), (6, 3)] 
        #Blue Palace information
        self._blue_palace_center = [(5, 9)]
        self._blue_palace_left_diagonals = [(4, 8), (4, 10)]
        self._blue_palace_right_diagonals = [(6, 8), (6, 10)]
        self._blue_palace_inner_diagonals = [(4, 8), (6, 8)]
        self._blue_palace_outer_diagonals = [(4,10), (6, 10)]
        self._blue_palace = [(4, 8), (5, 8), (6, 8),
                             (4, 9), (5, 9), (6, 9),
                             (4, 10), (5, 10), (6, 10)]
        
    #TODO: Get super to update players 'in_check' status up through the hierarchy of classes  
    #def blue_in_check(self):
        #super(Pieces, self).blue_in_check()
        
    def valid_move(self, piece, pos1, pos2, game_board, blue_in_check, red_in_check):
        """
        Takes the value assigned to piece, and determines its coordinates. It then accesses the appropirate piece class to determine move eligibility.
        """
        pos_1 = self._game_board_coords.get(pos1)              #Translating the string assignation to coordinate assignation for pos_1 and pos_2
        pos_2 = self._game_board_coords.get(pos2)
        
        if piece in self._soldiers:
            return Soldier().valid_move(piece, game_board, blue_in_check, red_in_check, self._game_board_coords, self._red_palace_center, self._red_palace_inner_diagonals, self._red_palace_outer_diagonals, \
                                        self._blue_palace_center, self._blue_palace_inner_diagonals, self._blue_palace_outer_diagonals, pos_1[0], pos_1[1], pos_2[0], pos_2[1])
            
        elif piece in self._guards:
            return Guard().valid_move(piece, self._red_palace, self._red_palace_center, self._red_palace_inner_diagonals, self._red_palace_outer_diagonals, \
                                      self._blue_palace, self._blue_palace_center, self._blue_palace_inner_diagonals, self._blue_palace_outer_diagonals, pos_1[0], pos_1[1], pos_2[0], pos_2[1])
            
        elif piece in self._horses:
            return Horse().valid_move(piece, game_board, self._game_board_coords, pos_1[0], pos_1[1], pos_2[0], pos_2[1])
        
        elif piece in self._elephants:
            return Elephant().valid_move(piece, game_board, self._game_board_coords, pos_1[0], pos_1[1], pos_2[0], pos_2[1])
        
        elif piece in self._chariots:
            return Chariot().valid_move(piece, game_board, self._game_board_coords, self._red_palace_center, self._blue_palace_center, pos_1[0], pos_1[1], pos_2[0], pos_2[1])
        
        elif piece in self._cannons:
            return Cannon().valid_move(piece, game_board, self._game_board_coords, self._red_palace_center, self._blue_palace_center, pos_1[0], pos_1[1], pos_2[0], pos_2[1])
        
        elif piece in self._generals:
            return General().valid_move(piece, self._red_palace, self._red_palace_center, self._red_palace_inner_diagonals, self._red_palace_outer_diagonals, \
                                        self._blue_palace, self._blue_palace_center, self._blue_palace_inner_diagonals, self._blue_palace_outer_diagonals, pos_1[0], pos_1[1], pos_2[0], pos_2[1])
       
class Soldier(Pieces):
    """
    A Soldier can move or capture 1 space forward or horizontally. If they reach the opposite edge of the board 
    they can only move horizontally. They can move diagonally forward if they reach the opposing palace.
    Class holds move validity logic for the piece via valid_move function, as well as get_key and get_value
    functions to assist.
    """

    def __init__(self):
        """
        Initialize piece information as needed by valid_move function
        """
        self._piece = 'soldier'
        self._BlGen = ['BlGen']
        self._RdGen = ['RdGen']

    def valid_move(self, piece, game_board, blue_in_check, red_in_check, game_board_coords, red_palace_center, red_palace_inner_diagonals, red_palace_outer_diagonals, \
                   blue_palace_center, blue_palace_inner_diagonals, blue_palace_outer_diagonals, x1, y1, x2, y2):
        """
        According to the rules of the Soldier it moves and updates the board.
        x1 = pos_1[0]   y1 = pos_1[1]       *pos_1 and pos_2 as referenced in Pieces().valid_move()
        x2 = pos_2[0]   y2 = pos_2[1]
        """
        
        pos_1 = (x1, y1)        #position 1
        pos_2 = (x2, y2)        #position 2
        
        #Acceptable moves when traversing the board
        acceptable_moves_blue = [(x1 - 1, y1), (x1 + 1, y1), (x1, y1 - 1)]
        acceptable_moves_red = [(x1 - 1, y1), (x1 + 1, y1), (x1, y1 + 1)]
        
        #Acceptable moves when calculating if a General is in check
        #acceptable_in_check_moves_blue = [(x2 - 1, y2), (x2 + 1, y2), (x2, y2 - 1)]
        #acceptable_in_check_moves_red = [(x2 - 1, y2), (x2 + 1, y2), (x2, y2 + 1)]
        
        #Acceptable moves when a soldier has reached the opposite end of the board
        acceptable_moves_end_board = [(x1 - 1, y1), (x1 + 1, y1)]
        
        #Acceptable end board moves when calculating if a General is in check
        #acceptable_moves_in_check_end_board = [(x2 - 1, y2), (x2 + 1, y2)]
            
        if piece == 'BlSol':
            #If Blue reaches Palace 
            if pos_1 in red_palace_inner_diagonals:
                if pos_2 not in (acceptable_moves_blue and red_palace_center):                      #Ensuring that a Blue Soldier can make a diagnoal move if need be when in an appropriate position
                    return False
            if pos_1 in red_palace_center:
                if pos_2 not in (acceptable_moves_blue and red_palace_outer_diagonals):
                    return False
                else:
                    return True
            
            #Typical Blue move
            if pos_2 not in acceptable_moves_blue:
                return False
            
            #If Blue reaches end of the board
            if pos_1[1] == 1:
                if pos_2 not in acceptable_moves_end_board:
                    return False
                
            #TODO: Determine if the move will place RdGen in check, if so, update self._player_red_in_check == True  **Couldn't get this to work**
            #Check if RdGen is in check while BlSol is at the end of the board
                #for i in range(len(acceptable_moves_in_check_end_board)):
                #    key = self.get_key(game_board_coords, acceptable_moves_in_check_end_board[i])
                #    RdGen_in_check = self.get_value(game_board, key, blue_in_check, red_in_check)
                
            #If a blue soldier puts a red general in check, if any piece within valid moves is a red General, then update self._player_red_in_check == True
            #for i in range(len(acceptable_in_check_moves_blue)):
            #        key = self.get_key(game_board_coords, acceptable_in_check_moves_blue[i])
            #        RdGen_in_check = self.get_value(game_board, key, blue_in_check, red_in_check)
            #        if RdGen_in_check == True:
            #            red_in_check == True
        
        if piece == 'RdSol':
            #If Red reaches Palace
            if pos_1 in blue_palace_inner_diagonals:
                if pos_2 not in (acceptable_moves_red and blue_palace_center):                      #Ensuring that a Red Soldier can make a diagnoal move if need be when in an appropriate position
                    return False
            
            if pos_1 in blue_palace_center:
                if pos_2 not in (acceptable_moves_red and blue_palace_outer_diagonals):
                    return False
                else:
                    return True
            
            #Typical Red move    
            if pos_2 not in acceptable_moves_red:
                return False  
            
            #If Red reaches end of board
            if pos_1[1] == 10:
                if pos_2 not in acceptable_moves_end_board:
                    return False
            
            #TODO: Determine if the move will place BLGen in check, if so, update self._player_blue_in_check == True  **Couldn't get this to work** 
            #Check if RdGen is in check while BlSol is at the end of the board
                #for i in range(len(acceptable_moves_in_check_end_board)):
                #    key = self.get_key(game_board_coords, acceptable_moves_in_check_end_board[i])
                #    BlGen_in_check = self.get_value(game_board, key, blue_in_check, red_in_check)
            
            #If a blue soldier puts a red general in check, if any piece within valid moves is a red General, then update self._player_red_in_check == True
            #for i in range(len(acceptable_in_check_moves_red)):
            #        key = self.get_key(game_board_coords, acceptable_in_check_moves_red[i])
            #        BlGen_in_check = self.get_value(game_board, key, blue_in_check, red_in_check)
            #        blue_in_check(BlGen_in_check) 

                    
                        
        return True
    
    def get_key(self, game_board_coords, val):
        """
        Get number/letter key for coordinate value in self._game_board_coordinates 
        """
        for key, value in game_board_coords.items():
            if val == value:
                return key
    
    def get_value(self, game_board, key, blue_in_check, red_in_check):
        """
        Get value(coordinates) from the self._game_board dictionary.
        """
        value = game_board.get(key)
        if value in self._RdGen:
            return True
        elif value in self._BlGen:
            return True
        else:
            return False
    
    #TODO: Get super to update players 'in_check' status up through the hierarchy of classes  
    #def blue_in_check(self):
        #super(Soldier, self).blue_in_check(BlGen_in_check)
        
class Guard(Pieces):
    """
    2 Guards start behind General, they can move 1 space per turn within the palace.
    Cannot leave palace. Used to protect the general         
    """
    def __init__(self):
        """
        Initialize piece information as needed by valid_move function
        """
        self._guards = ['RdGrd', 'BlGrd']

    def valid_move(self, piece, red_palace, red_palace_center, red_palace_inner_diagonals, red_palace_outer_diagonals, \
                   blue_palace, blue_palace_center, blue_palace_inner_diagonals, blue_palace_outer_diagonals, x1, y1, x2, y2):
        """
        According to the rules of the Guard it moves and updates the board.
        x1 = pos_1[0]   y1 = pos_1[1]       *pos_1 and pos_2 as referenced in Pieces().valid_move()
        x2 = pos_2[0]   y2 = pos_2[1]
        """
        pos_1 = (x1, y1)        #position 1
        pos_2 = (x2, y2)        #position 2
        
        #Acceptable moves when traversing the board
        acceptable_moves_blue = [(x1 - 1, y1), (x1 + 1, y1), (x1, y1 - 1), (x1, y1 + 1)]
        acceptable_moves_red = [(x1 - 1, y1), (x1 + 1, y1), (x1, y1 - 1), (x1, y1 + 1)]
        
        #Typical Blue move    
        if piece == 'BlGrd':
            if pos_2 not in (blue_palace or acceptable_moves_blue):      #Guard can only move to positions allowed by movement rules, within the palace.
                return False
        #If Blue is on inner or outer diagonals
            if pos_1 in (blue_palace_inner_diagonals and blue_palace_outer_diagonals):
                if pos_2 not in (blue_palace_center and acceptable_moves_blue):
                    return False
                else:
                    return True
        
        #Typical Red move
        if piece == 'RdGrd':
            if pos_2 not in (red_palace or acceptable_moves_red):
                return False
        #If Red is on inner or outer diagonals
            if pos_1 in (red_palace_inner_diagonals and red_palace_outer_diagonals):
                if pos_2 not in (red_palace_center and acceptable_moves_red):
                    return False
                else:
                    return True 
        return True

class Horse(Pieces):
    """
    Horses move 1 space vertically (forward or back) and 1 space horizontally(left or right). Initial setup is 
    not perfectly symmetrical on board. Cannot "Jump over" another piece; if a piece occupies a square in 
    the intended path, then the move is invalid. 
    Class holds move validity logic for the piece via valid_move function, as well as get_key and get_value
    functions to assist.
    """
    
    def __init__(self):
        """
        Initialize piece information as needed by valid_move function
        """
        self._horses =   ['RdHor', 'BlHor']
        self._pieces = ['RdSol', 'BlSol', 'RdCha', 'BlCha', 'RdHor', 'BlHor', 'RdEle', 'BlEle', 'RdGrd', 'BlGrd', 'RdCan', 'BlCan', 'RdGen', 'BlGen'] 


    def valid_move(self, piece, game_board, game_board_coords, x1, y1, x2, y2):
        """
        According to the rules of the Horse it moves and updates the board.
        x1 = pos_1[0]   y1 = pos_1[1]       *pos_1 and pos_2 as referenced in Pieces().valid_move()
        x2 = pos_2[0]   y2 = pos_2[1]
        """
        pos_1 = (x1, y1)        #position 1
        pos_2 = (x2, y2)        #position 2
        
        #Acceptable moves when traversing the board
        acceptable_moves = [(x1 - 1, y1 + 2), (x1 + 1, y1 + 2), (x1 + 2, y1 + 1), (x1 + 2, y1 - 1), (x1 + 1, y1 - 2), (x1 - 1, y1 - 2), (x1 - 2, y1 -1), (x1 - 2, y1 + 1)]
        blocked_moves = [(x1, y1 + 1), (x1, y1 + 1), (x1 + 1, y1), (x1 + 1, y1), (x1, y1 - 1), (x1, y1 - 1), (x1 - 1, y1), (x1 - 1, y1)]
        
        if piece in self._horses:
            #Typical move
            if pos_2 not in acceptable_moves:
                return False
            else:              #If there is a blocking piece in the way of a legal move, return False. There is one blockable position for any given horse move.
                if pos_2 == acceptable_moves[0]:
                    key = self.get_key(game_board_coords, blocked_moves[0])
                    return self.get_value(game_board, key)
                elif pos_2 == acceptable_moves[1]:
                    key = self.get_key(game_board_coords, blocked_moves[1])
                    return self.get_value(game_board, key)
                elif pos_2 == acceptable_moves[2]:
                    key = self.get_key(game_board_coords, blocked_moves[2])
                    return self.get_value(game_board, key)
                elif pos_2 == acceptable_moves[3]:
                    key = self.get_key(game_board_coords, blocked_moves[3])
                    return self.get_value(game_board, key)
                elif pos_2 == acceptable_moves[4]:
                    key = self.get_key(game_board_coords, blocked_moves[4])
                    return self.get_value(game_board, key)
                elif pos_2 == acceptable_moves[5]:
                    key = self.get_key(game_board_coords, blocked_moves[5])
                    return self.get_value(game_board, key)
                elif pos_2 == acceptable_moves[6]:
                    key = self.get_key(game_board_coords, blocked_moves[6])
                    return self.get_value(game_board, key)
                elif pos_2 == acceptable_moves[7]:
                    key = self.get_key(game_board_coords, blocked_moves[7])
                    return self.get_value(game_board, key)
                else:
                    return False
            
            return True
    
    def get_key(self, game_board_coords, val):
        """
        Get number/letter key for coordinate value in self._game_board_coordinates 
        """
        for key, value in game_board_coords.items():
            if val == value:
                return key
    
    def get_value(self, game_board, key):
        """
        Get value(coordinates) from the self._game_board dictionary in the JanggiGame.
        """
        value = game_board.get(key)
        if value in self._pieces:
            return False
        else:
            return True

class Elephant(Pieces):
    """
    Elephants can move 1 space vertically (forward or back) and 2 spaces horizontally (left or right) outward (1 space more than a Horse).
    Cannot "Jump over" another piece; if a piece occupies a square in the intended path, then the move is invalid.
    Class holds move validity logic for the piece via valid_move function, as well as get_key and get_value
    functions to assist.
    """

    def __init__(self):
        """
        Initialize piece information as needed by valid_move function
        """
        self._elephants = ['RdEle', 'BlEle']
        self._pieces = ['RdSol', 'BlSol', 'RdCha', 'BlCha', 'RdHor', 'BlHor', 'RdEle', 'BlEle', 'RdGrd', 'BlGrd', 'RdCan', 'BlCan', 'RdGen', 'BlGen']

    def valid_move(self, piece, game_board, game_board_coords, x1, y1, x2, y2):
        """
        According to the rules of the Horse it moves and updates the board.
        """
        pos_1 = (x1, y1)        #position 1
        pos_2 = (x2, y2)        #position 2
        
        #Acceptable moves when traversing the board
        acceptable_moves = [(x1 - 2, y1 + 3), (x1 + 2, y1 + 3), (x1 + 3, y1 + 2), (x1 + 3, y1 - 2), (x1 + 2, y1 - 3), (x1 - 2, y1 - 3), (x1 - 3, y1 - 2), (x1 - 3, y1 + 2)]
        #First possible positons where there might be a movement obstructing piece
        blocked_moves = [(x1, y1 + 1), (x1, y1 + 1), (x1 + 1, y1), (x1 + 1, y1), (x1, y1 - 1), (x1, y1 - 1), (x1 - 1, y1), (x1 - 1, y1)]
        #Second possible positions where there might be a movement obstructing piece
        blocked_moves_2 = [(x1 - 1, y1 + 2), (x1 + 1, y1 + 2), (x1 + 2, y1 + 1), (x1 + 2, y1 - 1), (x1 + 1, y1 - 2), (x1 - 1, y1 - 2), (x1 - 2, y1 - 1), (x1 - 2, y1 + 1)]
        
        if piece in self._elephants:
            if pos_2 not in acceptable_moves:
                return False
            else:              #If there is a blocking piece in the way of a legal move, return False. There are two possible positions that can block any given elephant move
                if pos_2 == acceptable_moves[0]:
                    key = self.get_key(game_board_coords, blocked_moves[0])
                    if self.get_value(game_board, key) == True:                                 #If there is NOT a piece at the first blockable position, return True
                        empty_square = self.get_key(game_board_coords, blocked_moves_2[0])
                        return self.get_value(game_board, empty_square)                                 #If there is NOT a piece at the second blockable position, return True
                elif pos_2 == acceptable_moves[1]:
                    key = self.get_key(game_board_coords, blocked_moves[1])
                    if self.get_value(game_board, key) == True:
                        empty_square = self.get_key(game_board_coords, blocked_moves_2[1])
                        return self.get_value(game_board, empty_square)   
                elif pos_2 == acceptable_moves[2]:
                    key = self.get_key(game_board_coords, blocked_moves[2])
                    if self.get_value(game_board, key) == True:
                        empty_square = self.get_key(game_board_coords, blocked_moves_2[2])
                        return self.get_value(game_board, empty_square)   
                elif pos_2 == acceptable_moves[3]:
                    key = self.get_key(game_board_coords, blocked_moves[3])
                    if self.get_value(game_board, key) == True:
                        empty_square = self.get_key(game_board_coords, blocked_moves_2[3])
                        return self.get_value(game_board, empty_square)   
                elif pos_2 == acceptable_moves[4]:
                    key = self.get_key(game_board_coords, blocked_moves[4])
                    if self.get_value(game_board, key) == True:
                        empty_square = self.get_key(game_board_coords, blocked_moves_2[4])
                        return self.get_value(game_board, empty_square)   
                elif pos_2 == acceptable_moves[5]:
                    key = self.get_key(game_board_coords, blocked_moves[5])
                    if self.get_value(game_board, key) == True:
                        empty_square = self.get_key(game_board_coords, blocked_moves_2[5])
                        return self.get_value(game_board, empty_square)   
                elif pos_2 == acceptable_moves[6]:
                    key = self.get_key(game_board_coords, blocked_moves[6])
                    if self.get_value(game_board, key) == True:
                        empty_square = self.get_key(game_board_coords, blocked_moves_2[6])
                        return self.get_value(game_board, empty_square)   
                elif pos_2 == acceptable_moves[7]:
                    key = self.get_key(game_board_coords, blocked_moves[7])
                    if self.get_value(game_board, key) == True:
                        empty_square = self.get_key(game_board_coords, blocked_moves_2[7])
                        return self.get_value(game_board, empty_square)   
                else:
                    return False
            
            return True
    
    def get_key(self, game_board_coords, val):
        """
        Get number/letter key for coordinate value in self._game_board_coordinates 
        """
        for key, value in game_board_coords.items():
            if val == value:
                return key
    
    def get_value(self, game_board, key):
        """
        Get value from the self._game_board dictionary in the JanggiGame.
        """
        value = game_board.get(key)
        if value in self._pieces:
            return False
        else:
            return True

class Chariot(Pieces):
    """
    Chariot can move an unlimited number of spaces in any vertical/horizontal direction (or diagonally if inside the palace)
    in a straight line.
    Class holds move validity logic for the piece via valid_move function, as well as get_key and get_value
    functions to assist.
    """

    def __init__(self):
        """
        Initialize piece information as needed by valid_move function
        """
        self._pieces = ['RdSol', 'BlSol', 'RdCha', 'BlCha', 'RdHor', 'BlHor', 'RdEle', 'BlEle', 'RdGrd', 'BlGrd', 'RdCan', 'BlCan', 'RdGen', 'BlGen']
        self._chariots = ['RdCha', 'BlCha']
        
    def valid_move(self, piece, game_board, game_board_coords, red_palace_center, blue_palace_center, x1, y1, x2, y2):
        """
        According to the rules of the Chariot it moves and updates the board.
        """
        pos_1 = (x1, y1)        #position 1
        pos_2 = (x2, y2)        #position 2
        
        #Acceptable moves for typical orthogonal movement
        acceptable_moves = [(x1+1, y1), (x1+2, y1), (x1+3, y1), (x1+4, y1), (x1+5, y1), (x1+6, y1), (x1+7, y1), (x1+8, y1), \
                            (x1-1, y1), (x1-2, y1), (x1-3, y1), (x1-4, y1), (x1-5, y1), (x1-6, y1), (x1-7, y1), (x1-8, y1), \
                            (x1, y1+1), (x1, y1+2), (x1, y1+3), (x1, y1+4), (x1, y1+5), (x1, y1+6), (x1, y1+7), (x1, y1+8), \
                            (x1, y1-1), (x1, y1-2), (x1, y1-3), (x1, y1-4), (x1, y1-5), (x1, y1-6), (x1, y1-7), (x1, y1-8)]
        acceptable_moves_right = acceptable_moves[0:8]
        acceptable_moves_left = acceptable_moves[8:16]
        acceptable_moves_down = acceptable_moves[16:24]
        acceptable_moves_up = acceptable_moves[24:32]
        
        #Special circumstances for when in the red palace
        red_upper_left_diagonal = game_board_coords.get('d1')
        red_lower_left_diagonal = game_board_coords.get('d3')
        red_upper_right_diagonal = game_board_coords.get('f1')
        red_lower_right_diagonal = game_board_coords.get('f3')
        
        #Special circumstances for when in the blue palace
        blue_upper_left_diagonal = game_board_coords.get('d8')
        blue_lower_left_diagonal = game_board_coords.get('d0')
        blue_upper_right_diagonal = game_board_coords.get('f8')
        blue_lower_right_diagonal = game_board_coords.get('f0')
        
        #If blue or red reaches either palace
        if piece in self._chariots:
            #If in the red palace
            if pos_1 in (red_upper_left_diagonal):
                if pos_2 not in (acceptable_moves and red_palace_center and red_lower_right_diagonal):                      
                    return False
                if pos_2 in red_lower_right_diagonal:
                    key = self.get_key(game_board_coords, red_palace_center)
                    empty_square = self.get_value(game_board, key)
                    if empty_square == False:
                        return False
            
            if pos_1 in (red_lower_left_diagonal):
                if pos_2 not in (acceptable_moves and red_palace_center and red_upper_right_diagonal):                      
                    return False
                if pos_2 in red_upper_right_diagonal:
                    key = self.get_key(game_board_coords, red_palace_center)
                    empty_square = self.get_value(game_board, key)
                    if empty_square == False:
                        return False
            
            if pos_1 in (red_upper_right_diagonal):
                if pos_2 not in (acceptable_moves and red_palace_center and red_lower_left_diagonal):                      
                    return False
                if pos_2 in red_lower_right_diagonal:
                    key = self.get_key(game_board_coords, red_palace_center)
                    empty_square = self.get_value(game_board, key)
                    if empty_square == False:
                        return False
            
            if pos_1 in (red_lower_right_diagonal):
                if pos_2 not in (acceptable_moves and red_palace_center and red_upper_left_diagonal):                      
                    return False
                if pos_2 in red_upper_left_diagonal:
                    key = self.get_key(game_board_coords, red_palace_center)
                    empty_square = self.get_value(game_board, key)
                    if empty_square == False:
                        return False
            
            #If in the blue palace
            if pos_1 in (blue_upper_left_diagonal):
                if pos_2 not in (acceptable_moves and blue_palace_center and blue_lower_right_diagonal):                      
                    return False
                if pos_2 in blue_lower_right_diagonal:
                    key = self.get_key(game_board_coords, blue_palace_center)
                    empty_square = self.get_value(game_board, key)
                    if empty_square == False:
                        return False
            
            if pos_1 in (blue_lower_left_diagonal):
                if pos_2 not in (acceptable_moves and blue_palace_center and blue_upper_right_diagonal):                      
                    return False
                if pos_2 in blue_upper_right_diagonal:
                    key = self.get_key(game_board_coords, blue_palace_center)
                    empty_square = self.get_value(game_board, key)
                    if empty_square == False:
                        return False
            
            if pos_1 in (blue_upper_right_diagonal):
                if pos_2 not in (acceptable_moves and blue_palace_center and blue_lower_left_diagonal):                      
                    return False
                if pos_2 in blue_lower_right_diagonal:
                    key = self.get_key(game_board_coords, blue_palace_center)
                    empty_square = self.get_value(game_board, key)
                    if empty_square == False:
                        return False
            
            if pos_1 in (blue_lower_right_diagonal):
                if pos_2 not in (acceptable_moves and blue_palace_center and blue_upper_left_diagonal):                      
                    return False
                if pos_2 in blue_upper_left_diagonal:
                    key = self.get_key(game_board_coords, blue_palace_center)
                    empty_square = self.get_value(game_board, key)
                    if empty_square == False:
                        return False
        
        #For any tytpical, non palace move, check if there's a piece in the way
        if pos_2 in acceptable_moves_right:                                                     #Moving rightward - check every intervening space between pos_1 and Pos_2 for occupancy.
            pos2 = acceptable_moves_right.index(pos_2)
            for i in range(len(acceptable_moves_right[0:pos2])):
                    key = self.get_key(game_board_coords, acceptable_moves_right[i])
                    empty_square = self.get_value(game_board, key)
                    if empty_square == False:
                        return False
                    
        if pos_2 in acceptable_moves_left:                                                      #Moving leftward - check every intervening space between pos_1 and Pos_2 for occupancy.
            pos2 = acceptable_moves_left.index(pos_2)
            for i in range(len(acceptable_moves_left[0:pos2])):
                    key = self.get_key(game_board_coords, acceptable_moves_left[i])
                    empty_square = self.get_value(game_board, key)
                    if empty_square == False:
                        return False
                    
        if pos_2 in acceptable_moves_up:                                                        #Moving upward - check every intervening space between pos_1 and Pos_2 for occupancy.
            pos2 = acceptable_moves_up.index(pos_2)
            for i in range(len(acceptable_moves_up[0:pos2])):
                    key = self.get_key(game_board_coords, acceptable_moves_up[i])
                    empty_square = self.get_value(game_board, key)
                    if empty_square == False:
                        return False
                    
        if pos_2 in acceptable_moves_down:                                                      #Moving downward - check every intervening space between pos_1 and Pos_2 for occupancy.
            pos2 = acceptable_moves_down.index(pos_2)
            for i in range(len(acceptable_moves_down[0:pos2])):
                    key = self.get_key(game_board_coords, acceptable_moves_down[i])
                    empty_square = self.get_value(game_board, key)
                    if empty_square == False:
                        return False
                    
        return True
        
    def get_key(self, game_board_coords, val):
        """
        Get number/letter key for coordinate value in self._game_board_coordinates 
        """
        for key, value in game_board_coords.items():
            if val == value:
                return key
    
    def get_value(self, game_board, key):
        """
        Get value from the self._game_board dictionary in the JanggiGame.
        """
        value = game_board.get(key)
        if value in self._pieces:
            return False
        else:
            return True

class Cannon(Pieces):
    """
    Cannons can move and capture by 'jumping' over any piece horizontally or vertically, any distance, as long as there is 1 piece
    (any color) to be jumped. Cannons cannot jump over or capture other cannons. They can jump or capture pieces diagonally if they are in the palace.
    Class holds move validity logic for the piece via valid_move function, as well as get_key and get_value
    functions to assist.
    """

    def __init__(self):
        """
        Initialize piece information as needed by valid_move function
        """
        self._cannons = ['RdCan', 'BlCan']
        self._pieces = ['RdSol', 'BlSol', 'RdCha', 'BlCha', 'RdHor', 'BlHor', 'RdEle', 'BlEle', 'RdGrd', 'BlGrd', 'RdGen', 'BlGen']

    def valid_move(self, piece, game_board, game_board_coords, red_palace_center, blue_palace_center, x1, y1, x2, y2):
        """
        According to the rules of the Cannon it moves and updates the board.
        """
        pos_1 = (x1, y1)        #position 1
        pos_2 = (x2, y2)        #position 2
        
        #Acceptable moves for typical orthogonal movement
        acceptable_moves = [(x1+1, y1), (x1+2, y1), (x1+3, y1), (x1+4, y1), (x1+5, y1), (x1+6, y1), (x1+7, y1), (x1+8, y1), \
                            (x1-1, y1), (x1-2, y1), (x1-3, y1), (x1-4, y1), (x1-5, y1), (x1-6, y1), (x1-7, y1), (x1-8, y1), \
                            (x1, y1+1), (x1, y1+2), (x1, y1+3), (x1, y1+4), (x1, y1+5), (x1, y1+6), (x1, y1+7), (x1, y1+8), \
                            (x1, y1-1), (x1, y1-2), (x1, y1-3), (x1, y1-4), (x1, y1-5), (x1, y1-6), (x1, y1-7), (x1, y1-8)]
        acceptable_moves_right = acceptable_moves[0:8]
        acceptable_moves_left = acceptable_moves[8:16]
        acceptable_moves_down = acceptable_moves[16:24]
        acceptable_moves_up = acceptable_moves[24:32]
        
        #Special circumstances for when in the red palace
        red_upper_left_diagonal = game_board_coords.get('d1')
        red_lower_left_diagonal = game_board_coords.get('d3')
        red_upper_right_diagonal = game_board_coords.get('f1')
        red_lower_right_diagonal = game_board_coords.get('f3')
        
        #Special circumstances for when in the blue palace
        blue_upper_left_diagonal = game_board_coords.get('d8')
        blue_lower_left_diagonal = game_board_coords.get('d0')
        blue_upper_right_diagonal = game_board_coords.get('f8')
        blue_lower_right_diagonal = game_board_coords.get('f0')
        
        #If blue or red reaches either palace
        if piece in self._cannons:
            #If in the red palace
            if pos_1 in (red_upper_left_diagonal):
                if pos_2 not in (acceptable_moves and red_palace_center and red_lower_right_diagonal):                      
                    return False
                if pos_2 in red_lower_right_diagonal:
                    key = self.get_key(game_board_coords, red_palace_center)
                    empty_square = self.get_value(game_board, key)
                    if empty_square == False:
                        return False
            
            if pos_1 in (red_lower_left_diagonal):
                if pos_2 not in (acceptable_moves and red_palace_center and red_upper_right_diagonal):                      
                    return False
                if pos_2 in red_upper_right_diagonal:
                    key = self.get_key(game_board_coords, red_palace_center)
                    empty_square = self.get_value(game_board, key)
                    if empty_square == False:
                        return False
            
            if pos_1 in (red_upper_right_diagonal):
                if pos_2 not in (acceptable_moves and red_palace_center and red_lower_left_diagonal):                      
                    return False
                if pos_2 in red_lower_right_diagonal:
                    key = self.get_key(game_board_coords, red_palace_center)
                    empty_square = self.get_value(game_board, key)
                    if empty_square == False:
                        return False
            
            if pos_1 in (red_lower_right_diagonal):
                if pos_2 not in (acceptable_moves and red_palace_center and red_upper_left_diagonal):                      
                    return False
                if pos_2 in red_upper_left_diagonal:
                    key = self.get_key(game_board_coords, red_palace_center)
                    empty_square = self.get_value(game_board, key)
                    if empty_square == False:
                        return False
            
            #If in the blue palace
            if pos_1 in (blue_upper_left_diagonal):
                if pos_2 not in (acceptable_moves and blue_palace_center and blue_lower_right_diagonal):                      
                    return False
                if pos_2 in blue_lower_right_diagonal:
                    key = self.get_key(game_board_coords, blue_palace_center)
                    empty_square = self.get_value(game_board, key)
                    if empty_square == False:
                        return False
            
            if pos_1 in (blue_lower_left_diagonal):
                if pos_2 not in (acceptable_moves and blue_palace_center and blue_upper_right_diagonal):                      
                    return False
                if pos_2 in blue_upper_right_diagonal:
                    key = self.get_key(game_board_coords, blue_palace_center)
                    empty_square = self.get_value(game_board, key)
                    if empty_square == False:
                        return False
            
            if pos_1 in (blue_upper_right_diagonal):
                if pos_2 not in (acceptable_moves and blue_palace_center and blue_lower_left_diagonal):                      
                    return False
                if pos_2 in blue_lower_right_diagonal:
                    key = self.get_key(game_board_coords, blue_palace_center)
                    empty_square = self.get_value(game_board, key)
                    if empty_square == False:
                        return False
            
            if pos_1 in (blue_lower_right_diagonal):
                if pos_2 not in (acceptable_moves and blue_palace_center and blue_upper_left_diagonal):                      
                    return False
                if pos_2 in blue_upper_left_diagonal:
                    key = self.get_key(game_board_coords, blue_palace_center)
                    empty_square = self.get_value(game_board, key)
                    if empty_square == False:
                        return False
        
        #For any typical, non palace move, check if there's a piece in the way
        if pos_2 in acceptable_moves_right:                                                     #Moving rightward - check every intervening space between pos_1 and Pos_2 for occupancy.
            pos2 = acceptable_moves_right.index(pos_2)                                          #If there is more than one piece in the path, return False
            count = 0                                                                           #If there is chariot piece in the path, return False
            for i in range(len(acceptable_moves_right[0:pos2])):
                key = self.get_key(game_board_coords, acceptable_moves_right[i])
                obstacles = self.get_value(game_board, key)
                if obstacles == True:
                    count += 1 
            if count > 1 or count == 0:
                return False  
                    
        if pos_2 in acceptable_moves_left:                                                      #Moving leftward - check every intervening space between pos_1 and Pos_2 for occupancy.
            pos2 = acceptable_moves_left.index(pos_2)                                           #If there is more than one piece in the path, return False
            count = 0                                                                           #If there is chariot piece in the path, return False
            for i in range(len(acceptable_moves_left[0:pos2])):
                key = self.get_key(game_board_coords, acceptable_moves_left[i])
                obstacles = self.get_value(game_board, key)
                if obstacles == True:
                    count += 1 
            if count > 1 or count == 0:
                return False  
                    
        if pos_2 in acceptable_moves_up:                                                        #Moving upward - check every intervening space between pos_1 and Pos_2 for occupancy.
            pos2 = acceptable_moves_up.index(pos_2)                                             #If there is more than one piece in the path, return False
            count = 0                                                                           #If there is chariot piece in the path, return False
            for i in range(len(acceptable_moves_up[0:pos2])):
                key = self.get_key(game_board_coords, acceptable_moves_up[i])
                obstacles = self.get_value(game_board, key)
                if obstacles == True:
                    count += 1 
            if count > 1 or count == 0:
                return False  
                    
        if pos_2 in acceptable_moves_down:                                                      #Moving downward - check every intervening space between pos_1 and Pos_2 for occupancy.
            pos2 = acceptable_moves_down.index(pos_2)                                           #If there is more than one piece in the path, return False
            count = 0                                                                           #If there is chariot piece in the path, return False
            for i in range(len(acceptable_moves_down[0:pos2])):
                key = self.get_key(game_board_coords, acceptable_moves_down[i])
                obstacles = self.get_value(game_board, key)
                if obstacles == True:
                    count += 1 
            if count > 1 or count == 0:
                return False                
        if pos_2 not in(acceptable_moves):
            return False
        
        return True
        
    def get_key(self, game_board_coords, val):
        """
        Get number/letter key for coordinate value in self._game_board_coordinates 
        """
        for key, value in game_board_coords.items():
            if val == value:
                return key
    
    def get_value(self, game_board, key):
        """
        Get value from the self._game_board dictionary in the JanggiGame.
        """
        value = game_board.get(key)
        if value in self._pieces:
            return True    
        elif value in self._cannons:
            return False

class General(Pieces):
    """
    The General starts in the palace center and can move 1 space per turn within the palace.
    The General cannot leave palace. A player loses if their General is checkmated.
    A player can skip their turn if doing so would preserve their General that turn.
    Update if_in_check if an opposing piece is capable of capturing next turn.
    Determine CHeckmate and Check.
    Class holds move validity logic for the piece via valid_move function, as well as get_key and get_value
    functions to assist.
    """

    def __init__(self):
        """
        Initialize piece information as needed by valid_move function
        """
        self._piece = 'general'
        self._pieces = ['BlSol', 'BlHor','BlEle','BlCha','BlCan', 'RdSol', 'RdHor', 'RdEle', 'RdCha', 'RdCan']
        

    def valid_move(self, piece, red_palace, red_palace_center, red_palace_inner_diagonals, red_palace_outer_diagonals, \
                   blue_palace, blue_palace_center, blue_palace_inner_diagonals, blue_palace_outer_diagonals, x1, y1, x2, y2):
        """
        According to the rules of the General it moves and updates the board.
        x1 = pos_1[0]   y1 = pos_1[1]       *pos_1 and pos_2 as referenced in Pieces().valid_move()
        x2 = pos_2[0]   y2 = pos_2[1]
        """
        pos_1 = (x1, y1)        #position 1
        pos_2 = (x2, y2)        #position 2
        
        #Acceptable moves when traversing the board
        acceptable_moves_blue = [(x1 - 1, y1), (x1 + 1, y1), (x1, y1 - 1), (x1, y1 + 1)]
        acceptable_moves_red = [(x1 - 1, y1), (x1 + 1, y1), (x1, y1 - 1), (x1, y1 + 1)]
        
        #Typical Blue move    
        if piece == 'BlGen':
            if pos_2 not in (blue_palace or acceptable_moves_blue):      #General can only move to positions allowed by movement rules, within the palace.
                return False
        #If Blue is on inner or outer diagonals
            if pos_1 in (blue_palace_inner_diagonals or blue_palace_outer_diagonals):
                if pos_2 not in (blue_palace_center and acceptable_moves_blue):
                    return False
                else:
                    return True
        
        #Typical Red move
        if piece == 'RdGen':
            if pos_2 not in (red_palace or acceptable_moves_red):
                return False
        #If Red is on inner or outer diagonals
            if pos_1 in (red_palace_inner_diagonals or red_palace_outer_diagonals):
                if pos_2 not in (red_palace_center and acceptable_moves_red):
                    return False
                else:
                    return True 
        return True
        
    def is_in_check(self):
        """
        Checks every space surrounding the General that could qualify as a check scenario, depending on the rules of each piece.
        """
        pass
    
        #TODO:
        #Soldier's acceptable moves
        #Horse's acceptable moves
        #Elephant's acceptable moves
        #Chariot's acceptable moves
        #Cannon's acceptable moves
        
        
        #TODO: if piece == "BlGen":

            #soldier: check all positions that comply with the rules of soldier's acceptable movement patterns, relative to the General's position:
            #For i in range(len(acceptable_moves_blue_soldier)):
            #key = self.get_key(game_board_coords, acceptable_moves_left[i])
                #RdSol = self.get_value(game_board, key)
                #if RdSol == 'RdSol':
                    #return True     
                               
            #horse: check all positions that comply with the rules of horse's acceptable movement patterns, relative to the General's position:
            #For i in range(len(acceptable_moves_blue_horse)):
            #key = self.get_key(game_board_coords, acceptable_moves_left[i])
                #RdHor = self.get_value(game_board, key)
                #if RdHor == 'RdHor':
                    #return True   
                    #Disqualify if block conditons apply
                          
            #elephant: check all positions that comply with the rules of elephant's acceptable movement patterns, relative to the General's position:
            #For i in range(len(acceptable_moves_blue_elephant)):
            #key = self.get_key(game_board_coords, acceptable_moves_left[i])
                #RdSol = self.get_value(game_board, key)
                #if RdEle == 'RdEle':
                    #return True   
                    #Disqualify if block conditons apply
                          
            #chariot: check all positions that comply with the rules of chariot's acceptable movement patterns, relative to the General's position:
            #For i in range(len(acceptable_moves_blue_chario†)):
            #key = self.get_key(game_board_coords, acceptable_moves_left[i])
                #RdCha = self.get_value(game_board, key)
                #if RdCHa == 'RdCha':
                    #return True 
                    #Disqualify if block conditons apply
                            
            #cannon: check all positions that comply with the rules of cannon's acceptable movement patterns, relative to the General's position:
            #For i in range(len(acceptable_moves_blue_cannon)):
            #key = self.get_key(game_board_coords, acceptable_moves_left[i])
                #RdCan = self.get_value(game_board, key)
                #if RdCan == 'RdCan':
                    #return True
                    #Disqualify if block conditons apply
        #return False         
        
        #TODO: if piece == "RdGen":
        
        #For every possible position available to the General:
        #For i in range(len(acceptable_moves_general)):
            #soldier: check all positions that comply with the rules of soldier's acceptable movement patterns, relative to the General's position:
            #For i in range(len(acceptable_moves_red_soldier)):
            #key = self.get_key(game_board_coords, acceptable_moves_left[i])
                #BlSol = self.get_value(game_board, key)
                #if BlSol == 'BlSol':
                    #return True    
                                
            #horse: check all positions that comply with the rules of horse's acceptable movement patterns, relative to the General's position:
            #For i in range(len(acceptable_moves_red_horse)):
            #key = self.get_key(game_board_coords, acceptable_moves_left[i])
                #BlHor = self.get_value(game_board, key)
                #if BlHor == 'BlHor':
                    #return True        
                    #Disqualify if block conditons apply
                     
            #elephant: check all positions that comply with the rules of elephant's acceptable movement patterns, relative to the General's position:
            #For i in range(len(acceptable_moves_red_soldier)):
            #key = self.get_key(game_board_coords, acceptable_moves_left[i])
                #BlELe = self.get_value(game_board, key)
                #if BlEle == 'BlEle':
                    #return True  
                    #Disqualify if block conditions apply   
                        
            #chariot: check all positions that comply with the rules of chariot's acceptable movement patterns, relative to the General's position:
            #For i in range(len(acceptable_moves_red_soldier)):
            #key = self.get_key(game_board_coords, acceptable_moves_left[i])
                #BlCha = self.get_value(game_board, key)
                #if BlCHa == 'BlCha':
                    #return True    
                    #Disqualify if block conditions apply
                         
            #cannon: check all positions that comply with the rules of cannon's acceptable movement patterns, relative to the General's position:
            #For i in range(len(acceptable_moves_red_soldier)):
            #key = self.get_key(game_board_coords, acceptable_moves_left[i])
                #BlCan = self.get_value(game_board, key)
                #if BlCan == 'BlCan':
                    #return True
                    #Disqualify if block conditons apply
        #return False         
        
    
     #def get_key(self, game_board_coords, val):
        #"""
        #Get number/letter key for coordinate value in self._game_board_coordinates 
        #"""
        #for key, value in game_board_coords.items():
        #    if val == value:
        #        return key
    
    #def get_value(self, game_board, key):
    #    """
    #    Get value from the self._game_board dictionary in the JanggiGame.
    #    """
    #    value = game_board.get(key)
    #    if value in self._pieces:
    #        return True
    #    else:
    #        return False
