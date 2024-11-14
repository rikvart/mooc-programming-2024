# Write your solution here

def count_matching_elements(my_matrix: list, element: int):
    count = 0
    for item in my_matrix:
        for entry in item:
            if entry == element:
                count += 1

    return count
