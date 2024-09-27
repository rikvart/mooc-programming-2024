# Write your solution here
def formatted(my_list):
    new_list = []
    for item in my_list:
        string = f"{item:.2f}"
        new_list.append(string)

    return new_list