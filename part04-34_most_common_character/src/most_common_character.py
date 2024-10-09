# Write your solution here

def most_common_character(string: str):

    i = 0
    largest = 0
    letter = ""
    for char in string:
        if string.count(char) > largest:
            largest = string.count(char)
            letter = char
        
        
    return letter
if __name__ == "__main__":

    stringToSend = "aabcdfgggh"
    most_common_character(stringToSend)

        