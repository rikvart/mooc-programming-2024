# Write your solution here
my_list = []
while True:
    num = int(input("New item:"))
    if num != 0:
        my_list.append(num)
        
        print(f"The list now: {my_list}")
        print("The list in order: " + str(sorted(my_list)))
    else:
        print("Bye!")
        break