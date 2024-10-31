# write your solution here

def largest():
    with open("numbers.txt") as new_file:
        largest = 0
        for line in new_file:
            tocompare = int(line)
            if tocompare > largest:
                largest = tocompare
    return largest