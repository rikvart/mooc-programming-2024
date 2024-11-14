# Write your solution here
def everything_reversed(names: list):
    
    i = 0
    length = len(names) - 1
    newList = []
    for name in names: 
            newList.append(name[::-1])
           
    return (newList[::-1])


oc