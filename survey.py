#create an empty dictionary
import json
start1 = "Hey user! This is my survey that I am working on. Thank you for taking the time to do it. Love you!"
print(start1)
answers = {}
#create a list of survey questions
print("First question.... what is your ")
questions = ["name?", "birth year?", "favorite color?", "high school's name?", "safe place?"]
#create a list of related keys
keys = ["name","year", "color", "school", "place"]
#Loop through your list of survey questions and take user input for responses
allUsers = []
#Loop through your list of survey questions and take user input for responses
done = "no"
while done == "no":
    answers = {}
    index = 0
    for q in questions:
        ans = input(q)
        answers[keys[index]] = ans
        index +=1
    allUsers.append(answers)
    done = input("Are you finished collecting information? (yes or no):")

print(allUsers)
with open('new.json') as f:
    try:
        olddata = json.load(f)
    except ValueError:
        olddata = []
#f = open("new.json", "r")
#olddata = json.load(f)
allUsers.extend(olddata)
f.close()

f = open("new.json", "w")
json.dump(allUsers, f)
f.close()

count = 0
twocount = 0
threecount = 0
for u in allUsers:
    count +=1
    ans = u["year"]
    if ans == "2002":
        twocount +=1
    else:
        threecount +=1
if twocount > threecount:
    print(str(twocount) + "out of " + str(count) + "are born in 2002!")
else:
    print(str(threecount) + "out of " + str(count) + "are born in 2003!")
