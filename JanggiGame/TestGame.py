# Testing game

from JanggiGame import JanggiGame


'''
#Soldier Movement Tests
game = JanggiGame()
print(game.print_board())
game.make_move('a7', 'a6')      #Blue Turn
game.make_move('e4', 'e5')      #Red turn
game.make_move('a6', 'a5')      #Blue Turn
game.make_move('e5', 'e6')      #Red Turn
game.make_move('a5', 'a4')      #Blue Turn
game.make_move('e6', 'e7')      #Red Turn
game.make_move('a4', 'a3')      #Blue Turn
game.make_move('e7', 'e8')      #Red Turn
game.make_move('a3', 'a2')      #Blue Turn
game.make_move('e8', 'e9')      #Red Turn
game.make_move('a2', 'a1')      #Blue Turn
game.make_move('e9', 'd10')     #Red Turn
print(game.print_board())
print(game.get_game_state())

#Guard and General Movement Tests
game = JanggiGame()
print(game.print_board())
game.make_move('a7', 'a6')      #Blue Turn          soldier
game.make_move('d1', 'e1')      #Red turn           guard
game.make_move('d10', 'd9')      #Blue Turn          guard
game.make_move('e2', 'f3')      #Red Turn           general
game.make_move('e9', 'd10')      #Blue Turn          general
game.make_move('e1', 'd2')      #Red Turn            guard
game.make_move('f10', 'e9')      #Blue Turn          guard
game.make_move('e4', 'e5')      #Red Turn           soldier
game.make_move('e9', 'd8')      #Blue Turn          guard
#game.make_move('e5', 'e6')      #Red Turn
#game.make_move('a2', 'a1')      #Blue Turn
#game.make_move('e6', 'e7')      #Red Turn
#game.make_move('a1', 'a2')      #Blue Turn
print(game.print_board())
print(game.get_game_state())


#Horse Movement Tests
game = JanggiGame()
#print(game.print_board())
game.make_move('c7', 'c6')      #Blue Turn
game.make_move('c1', 'd3')      #Red turn
game.make_move('a7', 'a6')      #Blue Turn
game.make_move('d3', 'c5')      #Red Turn
game.make_move('a6', 'a5')      #Blue Turn
game.make_move('c5', 'd7')      #Red Turn           invalid move
print(game.print_board())
#print(game.get_board())
print(game.get_game_state())

#Elephant Movement Tests
game = JanggiGame()
#print(game.print_board())
game.make_move('a7', 'a6')      #Blue Turn  soldier
game.make_move('b1', 'd4')      #Red turn   elephant
game.make_move('c7', 'c6')      #Blue Turn  soldier
game.make_move('d4', 'f7')      #Red Turn   elephant
game.make_move('a6', 'a5')      #Blue Turn  soldier
game.make_move('f7', 'd10')      #Red Turn   elephant
print(game.print_board())
#print(game.get_board())
print(game.get_game_state())

#Chariot Movement Tests
game = JanggiGame()
#print(game.print_board())
game.make_move('a7', 'a6')      #Blue Turn  soldier
game.make_move('a1', 'a5')      #Red turn   chariot     invalid move
#game.make_move('c7', 'c6')      #Blue Turn  soldier
#game.make_move('d4', 'f7')      #Red Turn   elephant
#game.make_move('a6', 'a5')      #Blue Turn  soldier
#game.make_move('f7', 'd10')      #Red Turn   elephant
print(game.print_board())
#print(game.get_board())
print(game.get_game_state())


#Cannon Movement Tests
game = JanggiGame()
#print(game.print_board())
game.make_move('c7', 'd7')      #Blue Turn  soldier
game.make_move('a4', 'b4')      #Red turn   soldier     
game.make_move('a7', 'a6')      #Blue Turn  soldier
game.make_move('b3', 'd5')      #Red Turn   soldier
#game.make_move('a6', 'a5')      #Blue Turn  soldier
#game.make_move('c5', 'c6')      #Red Turn   Soldier
#game.make_move('b6', 'c5')      #Blue Turn  soldier
#game.make_move('b8', 'b6')      #blue Turn   cannon     invalid move
print(game.print_board())
#print(game.get_board())
print(game.get_game_state())

'''
# Soldier Movement Tests
game = JanggiGame()
# print(game.print_board())
game.make_move('a7', 'a6')  # Blue Turn      soldier
game.make_move('e4', 'e5')  # Red turn       soldier
game.make_move('a6', 'a5')  # Blue Turn      soldier
game.make_move('e5', 'e6')  # Blue Turn      soldier
game.make_move('a5', 'a4')  # Red turn       soldier
game.make_move('e6', 'e7')  # Blue Turn      soldier
game.make_move('a4', 'a3')  # Blue Turn      soldier
game.make_move('e7', 'e8')  # Red turn       soldier
# game.make_move('a6', 'a5')      #Blue Turn      soldier
print(game.print_board())
print(game.is_in_check('blue'))
