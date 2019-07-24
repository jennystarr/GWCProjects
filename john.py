import json
from survey import*

pythonDictionary = {'name':'', 'year':'', 'color':'', 'school':'', 'place':''}
dictionaryToJson = json.dumps(pythonDictionary)
print(dictionaryToJson)
