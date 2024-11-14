# Write your solution here
def print_sudoku(sudoku: list):
    sudoku = sudoku
    new_sudoku = sudoku[:]
    for row in sudoku: 
        print(row)

    for r in new_sudoku:
        print(r)
    

def add_number(sudoku:list, row_no: int, column_no: int, number:int):
    sudoku = sudoku
    new_sudoku = sudoku[:]
    new_sudoku[r][c] == number
    print_sudoku(new_sudoku)