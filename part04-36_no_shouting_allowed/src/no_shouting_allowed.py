# Write your solution here
def no_shouting(my_list: list):
    
    new_list = []

    for word in my_list:
        if (word.isupper() == True):
            continue
        else:
            new_list.append(word)
    
    return new_list
