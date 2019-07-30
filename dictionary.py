#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")

print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
test_password = input("Type in a trial password: ")
for word in f:
    if word.strip() == test_password.strip():
        print("I got it ha")

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

for num in numbers:
    if num in numbers:
        print("That is week")
        break
#Write logic to see if the password is in the dictionary file below here:
