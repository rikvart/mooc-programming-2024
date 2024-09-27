# Write your solution here
def same_chars(word, num1, num2):

    leng = len(word) - 1

    if num2 <= leng and num1 <= leng and word[num1] == word[num2] :
        return True
    else:
        return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 10, 1))