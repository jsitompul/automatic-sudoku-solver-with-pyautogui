#Name: Automatic Sudoku Solver
#Author: Jimmy Sitompul
#@MIT License

# Importing the pyautogui library as pg to simulate keyboard and mouse actions
import pyautogui as pg 
# Importing numpy as np for potential numerical operations (although not used here)
import numpy as np 
# Importing the time library to add delays
import time


# Initializing an empty list to store the Sudoku puzzle
sudoku = []


# Infinite loop to input each row of the Sudoku puzzle
while True:
    # Asking the user to input a row (a 9-digit number) of the Sudoku puzzle
    curr_row = list(input('Insert row: '))
    # Initializing a temporary list to store the current row
    rows = []

    # Converting each character in the input row to an integer and adding it to the rows list
    for n in curr_row:
        rows.append(int(n))
    # Adding the current row to the sudoku list
    sudoku.append(rows)

    # Breaking the loop if all 9 rows have been inputted
    if len(sudoku) == 9:
        break
    # Printing a message indicating that the current row is complete
    print('Row ' + str(len(sudoku)) + ' Complete.')


# Adding a delay of 3 seconds before starting the solver
time.sleep(3)


# Function to check if placing a number in a specific position is valid
def is_valid(row, col, num):
    global sudoku
    # Checking if the number already exists in the current row or column
    for i in range(9):
        if sudoku[row][i] == num or sudoku[i][col] == num:
            # Returns False if the number already exists in the current row or column
            return False
        
    # Calculating the starting indices of the 3x3 subgrid [checkRow,checkCol]
    checkRow = row - (row % 3)
    checkCol = col - (col % 3)
    # Checking if the number already exists in the 3x3 subgrid
    for i in range(3):
        for j in range(3):
            if sudoku[checkRow + i][checkCol + j] == num:
                # Returns False if the number already exists in the 3x3 subgrid
                return False
    
    # Returning True if the number can be placed in the position
    return True


# Function to print the solved Sudoku puzzle using pyautogui
def print_sudoku(matrix):
    # Iterate through each row and column in the matrix
    for i in range(9):
        for j in range(9):
            # Press the key corresponding to the number at matrix[i][j]
            pg.press(str(matrix[i][j]))
            
            # Move to the right unless it's the last column
            if j < 8:
                pg.hotkey('right')
        
        # After completing a row, move down unless it's the last row
        if i < 8:
            for _ in range(8):
                pg.hotkey('left')  # Move back to the start of the row
            pg.hotkey('down')


# Function to solve the Sudoku puzzle using backtracking
def solve_sudoku():
    global sudoku
    # Looping through each cell in the Sudoku puzzle
    for i in range(9):
        for j in range(9):
            # Checking if the current cell is empty (contains 0)
            if sudoku[i][j] == 0:
                # Trying each number from 1 to 9 in the empty cell
                for num in range(1, 10):
                    # Checking if the number can be placed in the cell
                    if is_valid(i, j, num):
                        sudoku[i][j] = num  # Placing the number in the cell
                        solve_sudoku()  # Recursively solving the rest of the puzzle
                        sudoku[i][j] = 0  # Resetting the cell if the solution is not valid
                return  # Returning if the puzzle is solved
    # Printing the solved Sudoku puzzle
    print_sudoku(sudoku)


# Calling the solve_sudoku function to solve the Sudoku puzzle
solve_sudoku()
