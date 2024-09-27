# Write your solution here
def  mean(list):
    total = 0
    i = 0
    for item in list:
        total = total + item
        i+=1
    result = total / i
    return result
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)