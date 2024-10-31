# Write your solution here

def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:
    to_return = True
    filtered = []
    start_row, start_col = 3 * (row_no // 3), 3 * (column_no // 3)
    
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if sudoku[r][c] != 0:
                filtered.append(sudoku[r][c])
    
    for num in filtered:
        if filtered.count(num) < 2:
            continue
        else:
            to_return = False
    
    return to_return

