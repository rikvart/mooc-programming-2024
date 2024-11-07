def block_correct(sudoku: list, row_no: int, col_no: int):
    filtered = []
    to_return = True
    for r in range(row_no, row_no + 3):
        for c in range(col_no, col_no + 3):
            if sudoku[r][c] != 0:
                filtered.append(sudoku[r][c])

    for num in filtered:
        if filtered.count(num) > 1:
            to_return = False
            break

    return to_return


def row_correct(sudoku: list, row_no: int):
    to_return = True
    filtered = []
    for item in sudoku[row_no]:
        if item != 0:
            filtered.append(item)

    for item in filtered:
        if filtered.count(item) < 2:
            continue
        else:
            to_return = False
        
    return to_return


def column_correct(sudoku: list, column_no: int):
    to_return = True
    filtered = []
    for row in sudoku:
        if row[column_no] != 0:
            filtered.append(row[column_no])
        
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

    for row in range(9):
        if not row_correct(sudoku, row):
            return False

    for col in range(9):
        if not column_correct(sudoku, col):
            return False

    return True

