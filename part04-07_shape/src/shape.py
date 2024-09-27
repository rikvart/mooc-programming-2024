# Copy here code of line function from previous exercise and use it in your solution
def line(num, char):
    if char == "":
        print("*"*num)
    else:
        print(char[0]*num)

def shape(num1, char1, num2, char2):
    i = 1
    width = 1
    y = 0
    while i <= num1:
        line(i, char1)
        i = i + 1
        width = i - 1
    while y < num2:
        line(width, char2)
        y+=1



# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")