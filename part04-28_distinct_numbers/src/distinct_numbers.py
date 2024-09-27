# Write your solution here

def distinct_numbers(my_list):
    sorted_list = sorted(my_list)
    new_list = []
    for item in sorted_list:
        if item in new_list:
            continue
        else:
            new_list.append(item)

    return new_list

