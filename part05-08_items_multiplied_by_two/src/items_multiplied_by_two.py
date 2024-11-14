# Write your solution here

def double_items(numbers: list):

    newlist = numbers[:]
    newdoubled = []

    for item in newlist:
        doubled = item * 2
        newdoubled.append(doubled)



    return newdoubled



if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)