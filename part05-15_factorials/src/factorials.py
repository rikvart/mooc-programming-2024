
def factorials(n: int):
    my_dictionary = {}
    for num in range(1, n + 1):
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        my_dictionary[num] = factorial
    print(my_dictionary)
    return my_dictionary


if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])
