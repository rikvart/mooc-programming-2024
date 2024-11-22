# Write your solution here
1



while True:
    command = int(input("1 - add an entry, 2 - read entries, 0 - quit: "))
    if command == 1:
        entry = input("Diary entry?")
        with open("diary.txt", "a") as my_file:
            my_file.write(entry)
        
    elif command == 2:
        with open("diary.txt") as new_file:
            contents = new_file.read()
            print(contents)
    elif command == 0:
        break