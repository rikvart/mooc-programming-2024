# Write your solution here

def even_numbers(my_list):

    new_list = []
    for item in my_list:
        if item % 2 == 0:
            new_list.append(item)
        else: 
            continue

    return new_list

