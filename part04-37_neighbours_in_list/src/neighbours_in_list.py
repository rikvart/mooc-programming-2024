# Write your solution here
def longest_series_of_neighbours(my_list: list):
    longest = 1
    counter = 1

    for i in range(1, len(my_list)):
        if abs(my_list[i] - my_list[i - 1]) == 1:
            counter += 1
        else:
            if counter > longest:
                longest = counter
            counter = 1

    if counter > longest:
        longest = counter

    return longest


if __name__ == "__main__":

    testlist = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    longest_series_of_neighbours(testlist)
