# Write your solution here
def length_of_longest(my_list):
    i = -1
    longest = my_list[1]

    for item in my_list:
        i+=1
        if len(item) >= len(longest):
            longest=my_list[i]
        else:
            longest = longest

    toreturn = len(longest)

    return toreturn
    
