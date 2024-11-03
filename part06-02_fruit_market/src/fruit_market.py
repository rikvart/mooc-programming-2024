# write your solution here
def read_fruits():
    with open("fruits.csv") as new_file:
        for line in new_file:
            
            parts = line.split(";")
            name = parts[0]
            prices = parts[1:]
            print(parts + print(name + float(prices)))

if __name__ == "__main__":

    read_fruits


    