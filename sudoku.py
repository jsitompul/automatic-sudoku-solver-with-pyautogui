import pyautogui as pg
import numpy as np
import time


sudoku = []


while True:
    curr_row = list(input('Insert row: '))
    rows = []

    for n in curr_row:
        rows.append(int(n))
    sudoku.append(rows)

    if len(sudoku) == 9:
        break
    print('Row ' + str(len(sudoku)) + ' Complete.')


time.sleep(3)

def is_valid(row, col, num):
    global sudoku
    for i in range(9):
        if sudoku[row][i] == num or sudoku[i][col] == num:
            return False
        
    checkRow = row - (row % 3)
    checkCol = col - (col % 3)
    for i in range(3):
        for j in range(3):
            if sudoku[checkRow + i][checkCol + j] == num:
                return False
    
    return True


def print_sudoku(matrix):
    final = []
    str_final = []
    for i in range(9):
        final.append(matrix[i])

    for lists in final:
        for num in lists:
            str_final.append(str(num))

    counter = []
    for num in str_final:
        pg.press(num)
        pg.hotkey('right')
        counter.append(num)
        if len(counter) % 9 == 0:
            for x in range(8):
                pg.hotkey('left')
            pg.hotkey('down')



def solve_sudoku():
    global sudoku
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for num in range(1,10):
                    if is_valid(i,j,num):
                        sudoku[i][j] = num
                        solve_sudoku()
                        sudoku[i][j] = 0
                return 
    print_sudoku(sudoku)

solve_sudoku()