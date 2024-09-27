# Write your solution here

my_list = [1, 2, 3, 4, 5]

while True:
    i = int(input("Index: "))
    if i >= 0: 
        num = int(input("New value: "))
        my_list[i] = num
        print(my_list)

    else:
        break
    