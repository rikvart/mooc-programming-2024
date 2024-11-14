# Write your solution here
def times_ten(start_index: int, end_index: int):
    my_dictionary = {}
    
    for num in range (start_index, end_index + 1):
        key = num * 10
        my_dictionary[num] = key

    return my_dictionary