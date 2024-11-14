# Write your solution here

def factorials(n: int):
    i = n
    total = 0
    my_dictionary = {}
    if n == 1:
        total = 1
    else: 
        while i > 0:
            total = n * i
            i -= 1

    
    my_dictionary[n] = total
    return my_dictionary
