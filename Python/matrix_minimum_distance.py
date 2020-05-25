import numpy as np
import random

matrixSize = 10

# The way that I solved
def minimumDistance(numRows, numColumns, matrix):
    steps = 0
    spread = True
    final = False
    while spread:
        spread = False
        updateMatrix(matrix)
        for i in range(numRows):
            for j in range(numColumns):
                if matrix[i][j] == 3:
                    final = spreadValues(i, j, matrix, numRows, numColumns)
                    if final:
                        steps +=1
                        print('Number of steps: ' + str(steps))
                        return matrix
                    matrix[i][j] = 4
                    spread = True
        steps +=1
    if not final:
        steps = -1
    print('Number of steps: ' + str(steps))
    return matrix

def updateMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 2:
                matrix[i][j] = 3

def spreadValues(line, column, matrix, numRows, numColumns):
    if ((line < numRows - 1 and matrix[line + 1][column] == 9) or
    (column < numColumns -1 and matrix[line][column + 1] == 9) or
    (line != 0 and matrix[line - 1][column] == 9) or
    (column != 0 and matrix[line][column - 1] == 9)):
        return True

    if line < numRows - 1 and matrix[line + 1][column] == 1:
        matrix[line + 1][column] = 2
    if column < numColumns -1 and matrix[line][column + 1] == 1:
        matrix[line][column + 1] = 2
    if line != 0 and matrix[line - 1][column] == 1:
        matrix[line - 1][column] = 2
    if column != 0 and matrix[line][column - 1] == 1:
        matrix[line][column - 1] = 2 
    return False

# generate new matrix will generate a new random matrix with random values but with a fixed size
def generateNewMatrix(size):
    newMatrix = []
    # setting up the matrix path for the truck
    for i in range(size):
        newMatrix.append(np.random.choice(2, size, p=[0.3, 0.7]))
    
    # Setting up the nine position / final position
    newMatrix[random.randrange(1,size)][random.randrange(1,size)] = 9

    # Setting up the truck starting position
    newMatrix[0][0] = 2

    return newMatrix

def printMatrix(matrix):
    print(' _' +'___' * len(matrix) + '_ ')
    for row in matrix:
        print('| ', end="")
        for number in row:
            if number == 0:
                print(' ', end="")
            else:
                print(number, end="")
            print('  ', end="")
        print(" |")
    print('|_' +'___' * len(matrix) + '_|\n\n')


if __name__ == '__main__':
    # Creating the matrix
    matrix = generateNewMatrix(matrixSize)
    printMatrix(minimumDistance(matrixSize, matrixSize, matrix))