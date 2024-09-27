# Write your solution here
num = int(input("Please type in a positive integer: "))
nega = num * -1
for i in range(nega, num + 1):
    if i == 0:
        continue
    else:
        print(i)