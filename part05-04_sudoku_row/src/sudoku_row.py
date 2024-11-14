# Write your solution here

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
           

