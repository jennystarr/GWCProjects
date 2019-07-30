import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud
from textblob import TextBlob
import os
from os import path
import election
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
list_of_result = election.get_results(test=True)
# print(list_of_result)

finalResult = {}
for row in list_of_result:
    if row['Location']['State'] not in finalResult:
        continue

for row in list_of_result:
    #(row["Location"]["State"])
    Bernie = row["Location"]["State"], row["Vote Data"]["Bernie Sanders"]["Percent of Votes"]
    Hillary = row["Location"]["State"], row["Vote Data"]["Hillary Clinton"]["Percent of Votes"]

objects = ['Bernie', 'Hillary']
x_pos = np.arange(len(objects))
values = [Bernie, Hillary]
clr = '#F09D00'
label = ['99', '400', '1200']

# print(values)

for i in range(len(x_pos)):
    plt.text(x = x_pos[i]-0.1, y = values[i], s = label[i], size = 9)
plt.bar(x_pos, values, align='center', color=clr)
plt.xticks(x_pos, objects)
plt.xlabel('# of people (in thousands)')
plt.ylabel('age group')
plt.title('Bernie vs. Hillary')
plt.show()
print(Bernie)
print(Hillary)
