# Write your solution here

def list_sum(my_list, my_list2):
    i = 0
    new_list = []
    for item in my_list:
        new_list.append(item)

    for item in my_list2:
        
        new_list[i] = new_list[i] + item
        i+=1

    return new_list
