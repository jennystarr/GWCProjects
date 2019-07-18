#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
aList = ["carrot", "orange", "yellow", "blue", "water", "apple", "lollypop", "cake", "fruit", "mango"]
adjetives = ["kind", "smart", "loving", "caring", "mean", "funny", "stinky", "controling", "angry", "clumsy"]
#Generates a random integer.
aRandomIndex = randint(0, len(aList)-1)
aRandomad = randint(0, len(aList)-1)
print(adjetives[aRandomad])
print(aList[aRandomIndex])
