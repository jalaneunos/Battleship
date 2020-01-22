#This is a battleship game

import random, copy

board = []
print('Welcome to Battleship!')
print('Choose your board size, ? x ? (Maximum size of 10)')
boardsize = int(input())
if not type(boardsize) is int:
    raise TypeError('Only integers are allowed')
elif boardsize < 1 or boardsize > 10:
    raise ValueError('Choose a board size from 1 to 10')

for i in range(boardsize):
    board.append(['.']*boardsize)

def board_print(boarder):
    for row in boarder:
        print((' ').join(row))

    

board_print(board)
playing_board = copy.deepcopy(board) # A separate board that will only be displayed to the player

ship_length= random.randrange(1,boardsize) # Length of ship must be less than or equals to boardsize
orientations = ['horizontal','vertical'] # Possible orientations of the ship
ship_orientation = random.choice(orientations)

if ship_orientation == 'horizontal': # Following chunk decides the position of the ship in the board
    shiprow = random.randint(1, boardsize) 
    shiphead = random.randint(1, boardsize - ship_length) # Coordinate of the front of the ship, assuming all horizontal ships face left, 1 being extreme left
    board[shiprow][shiphead:shiphead+ship_length+1] = 'S'*ship_length # Planting the ship on the board
elif ship_orientation == 'vertical':
    shipcolumn = random.randint(1, boardsize-1)
    shiphead = random.randint(1, boardsize - ship_length) # Coordinate of the front of the ship assuming the ships always face up, 1 being top row
    for i in board[shiphead:]:
        i[shipcolumn] = 'S' # The position of the ship marked by S (Only on the invisible board unseen by player)


tries = 10
hits = 0

while tries > 0 and hits != int(ship_length): 
    print('You have ' + str(tries) + ' tries.')
    playerrow = int(input('Choose a row: ')) - 1
    playercolumn = int(input('Choose a column: ')) - 1
    try:
        if board[playerrow][playercolumn] == 'S':
            print('Thats a hit!')
            hits += 1
            playing_board[playerrow][playercolumn] = 'S'
            board_print(playing_board)
            if hits == ship_length:
                print('Congratulations, you have sunk the enemy ship!')
                break
    except IndexError or ValueError:
        print('Hey that\'s not even in the ocean.')
           
    else:
        print('Missed!')
        playing_board[playerrow][playercolumn] = 'X'
        board_print(playing_board)
        tries -= 1
if tries == 0:
    print('Game Over')



  

    


