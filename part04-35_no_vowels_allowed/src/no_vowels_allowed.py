# Write your solution here

def no_vowels(string: str):
    newString = ""
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for char in string:
        if char in vowels:
            continue
        else: 
            newString = newString + char

    return newString    

        