# Write your solution here

def all_the_longest(my_list): 
    new_list = []
    i = 0
    max_length = max(len(item) for item in my_list)
    
    for item in my_list:
        if len(item) == max_length:
            new_list.append(item)
    
    return new_list

#     print(new_list)
 
# if __name__ == "__main__":
#     all_the_longest(["ab", "test", "test", "abc", "test"])