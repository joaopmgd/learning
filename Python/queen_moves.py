def create_board(size, pieces):
    board = []
    for lines in range(size):
        board.append([ i * 0 for i in range(size)])

    for piece in pieces:
        if piece[0] < size and piece[1] < size:
            board[piece[0]][piece[1]] = 1
    return board

def print_board(board):
    print()
    print(' _' +'___' * len(board) + '_ ')
    for row in board:
        print('| ', end="")
        for number in row:
            if number == 0:
                print(' ', end="")
            else:
                print(number, end="")
            print('  ', end="")
        print(" |")
    print('|_' +'___' * len(board) + '_|\n\n')

def possible_moves(board, queen_position):
    positions = []
    board[queen_position[0]][queen_position[1]] = 9
    distance = 1
    changed = [True, True, True, True, True, True, True, True]
    while sum(changed) > 0:
        
        # up
        if changed[0] and queen_position[0]-distance >= 0 and board[queen_position[0]-distance][queen_position[1]] != 1 :
            changed[0] = True
            positions.append((queen_position[0]-distance, queen_position[1]))
            board[queen_position[0]-distance][queen_position[1]] = 2
        else:
            changed[0] = False

        # down
        if changed[1] and queen_position[0]+distance < len(board) and board[queen_position[0]+distance][queen_position[1]] != 1 :
            changed[1] = True
            positions.append((queen_position[0]+distance, queen_position[1]))
            board[queen_position[0]+distance][queen_position[1]] = 2
        else:
            changed[1] = False

        # left
        if changed[2] and queen_position[1]-distance >= 0 and board[queen_position[0]][queen_position[1]-distance] != 1 :
            changed[2] = True
            positions.append((queen_position[0], queen_position[1]-distance))
            board[queen_position[0]][queen_position[1]-distance] = 2
        else:
            changed[2] = False

        # right
        if changed[3] and queen_position[1]+distance < len(board) and board[queen_position[0]][queen_position[1]+distance] != 1 :
            changed[3] = True
            positions.append((queen_position[0], queen_position[1]+distance))
            board[queen_position[0]][queen_position[1]+distance] = 2
        else:
            changed[3] = False

        # leftup
        if changed[4] and queen_position[0]-distance >= 0 and queen_position[1]-distance >= 0 and board[queen_position[0]-distance][queen_position[1]-distance] != 1 :
            changed[4] = True
            positions.append((queen_position[0]-distance, queen_position[1]-distance))
            board[queen_position[0]-distance][queen_position[1]-distance] = 2
        else:
            changed[4] = False

        # leftdown
        if changed[5] and queen_position[0]+distance < len(board) and queen_position[1]-distance >= 0 and board[queen_position[0]+distance][queen_position[1]-distance] != 1 :
            changed[5] = True
            positions.append((queen_position[0]+distance, queen_position[1]-distance))
            board[queen_position[0]+distance][queen_position[1]-distance] = 2
        else:
            changed[5] = False

        # rightup
        if changed[6] and queen_position[0]-distance >= 0 and queen_position[1]+distance < len(board) and board[queen_position[0]-distance][queen_position[1]+distance] != 1 :
            changed[6] = True
            positions.append((queen_position[0]-distance, queen_position[1]+distance))
            board[queen_position[0]-distance][queen_position[1]+distance] = 2
        else:
            changed[6] = False

        # rightdown
        if changed[7] and queen_position[0]+distance < len(board) and queen_position[1] + distance < len(board) and board[queen_position[0]+distance][queen_position[1]+distance] != 1 :
            changed[7] = True
            positions.append((queen_position[0]-distance, queen_position[1]))
            board[queen_position[0]+distance][queen_position[1]+distance] = 2
        else:
            changed[7] = False

        distance += 1

    print_board(board)
    return positions

if __name__ == '__main__':
    size = 10
    pieces = [(3,5), (7,5), (5,3), (5,7), (7,3), (7,7), (3,3), (3,7)]
    queen_position = (5, 5)
    board = create_board(size, pieces)
    print(possible_moves(board, queen_position))