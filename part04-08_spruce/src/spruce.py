# Write your solution here
# You can test your function by calling it within the following block
def spruce(height):
    space_right = height - 1
    
    i = 0
    y = 1
    print("a spruce!")
    while i < height: 
        print(space_right * " " + "*" * y + space_right * " ")
        space_right-=1
        i+=1
        y+=2
    space_right = height - 1
    print(space_right * " " + "*" + space_right * " ")
    

if __name__ == "__main__":
    spruce(5)