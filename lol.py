import json

myDictionary = {'name':'jen', 'year':'2002', 'color':'blue', 'school':'nb', 'place':'home'}

f = open("new.json", "w")
json.dump(myDictionary, f)
f.close()
