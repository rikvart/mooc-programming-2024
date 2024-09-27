# Write your solution here

def sum_of_positives(my_list):
    total = 0
    for item in my_list:
        if item > 0: 
            total = total + item
    
    return total

