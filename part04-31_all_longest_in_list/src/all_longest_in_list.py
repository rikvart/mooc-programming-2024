# Write your solution here

def all_the_longest(my_list): 

    new_list = []
    i = 0
    longest = my_list[0]
    for item in my_list:
        if len(item) >= len(longest):
            new_list.append(item)
    
    return new_list