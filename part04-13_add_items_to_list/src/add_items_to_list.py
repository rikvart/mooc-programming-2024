# Write your solution here
my_list = []
i = 1
num = int(input("How many items:"))

while i <= num:
    toadd = int(input(f"Item {i}:"))
    i+=1
    my_list.append(toadd)
    


print(my_list)
