# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def main():
    while True:
        word = input("Please type in a palindrome:")
        if palindromes(word) == True:
            print(f"{word} is a palindrome!")
            break
        else: 
            print("that wasn't a palindrome")
    


def palindromes(word):
    sorted = word[::-1]
    if word == sorted: 
        return True
    else:
        return False


main()


