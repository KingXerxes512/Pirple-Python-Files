import os

inputFile = input("Please enter the filename to be used: ")
if os.path.exists(inputFile):
    action = input("Found an existing file, would you like to: read, delete, or continue the file? ")
    if action == "read":
        print("File Contains:")
        with open(inputFile, "r") as read_file:
            print(read_file.read())
    elif action == "delete":
        print("File contents deleted...")
        with open(inputFile, "w") as write_file:
            write_file.write(input("Enter your note:"))
    elif action == "continue":
        text = input("Please enter your note: ")
        with open(inputFile, "a") as append_file:
            append_file.write(text + "\n")
    else:
        print("Sorry, unrecognized action...")
else:
    print("This file does not exist, I'm going to create it for you!")
    text = input("Please enter your note: ")
    with open(inputFile, "w") as write_file:
        write_file.write(text + "\n")
