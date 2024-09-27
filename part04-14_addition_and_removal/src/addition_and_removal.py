# Write your solution here

my_list = []

print(f"The list is now {my_list}")
i = 0
while True:
    action = input("a(d)d, (r)emove or e(x)it:")
    
    if action == "d":
        my_list.append(i+1)
        print(f"The list is now {my_list}")
        i+=1
    elif action == "r": 
        my_list.pop(i-1)
        print(f"The list is now {my_list}")
        i-=1
    elif action == "x":
        print("Bye!")
        break
    else:
        continue