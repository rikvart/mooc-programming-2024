# Write your solution here

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


           
