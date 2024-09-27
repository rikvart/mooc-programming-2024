# Write your solution here

def shortest(my_list):
    shortest = my_list[0]
    for item in my_list:
        if len(item) < len(shortest):
            shortest = item

    return shortest