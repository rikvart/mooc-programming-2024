# Write your solution here
def first_word(string):
    wlist = string.split()
    return wlist[0]
    
def second_word(string):
    wlist = string.split()
    return wlist[1]

def last_word(string):
    wlist = string.split()
    i = len(wlist) - 1
    return wlist[i]





# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))