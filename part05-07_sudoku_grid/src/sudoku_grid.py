# Write your solution here


def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:
    to_return = True
    filtered = []
    
    
    for r in range(row_no, row_no + 3):
        for c in range(column_no, column_no + 3):
            if sudoku[r][c] != 0:
                filtered.append(sudoku[r][c])
    
    for num in filtered:
        if filtered.count(num) < 2:
            continue
        else:
            to_return = False
    
    return to_return


def sudoku_grid_correct(sudoku: list):

    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            if not block_correct(sudoku, row, col):
                return False
    return True

