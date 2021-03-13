import pandas as pd
import time
import numpy as np

pd.set_option('display.max_columns', None)

data = pd.read_csv('C://Users//incar//PycharmProjects//Advent_calendar//venv//day2_input.txt', header = None)
print(data)


data[['policy','password']] = data[0].str.split(':',expand=True)
data[['characters','letter']] = data['policy'].str.split(' ',expand=True)
data[['min_char','max_char']] = data['characters'].str.split('-',expand=True)

df.words.str.count("he|wo")
data['count_letter'] = data.apply(lambda x: x['password'].count(x['letter']), axis=1)

data.head(5)

#first challenge
data['invalid'] = data.apply(lambda x: False if (x['count_letter']>= pd.to_numeric(x['min_char'])) &
                                        (x['count_letter']<= pd.to_numeric(x['max_char'])) else True, axis=1)

sum(data['invalid']==False)

#second challenge

data['char_min'] = data.apply(lambda x: x['password'][pd.to_numeric(x['min_char'])] , axis = 1)
data['char_max'] = data.apply(lambda x: x['password'][pd.to_numeric(x['max_char'])] , axis = 1)

data['invalid2'] = data.apply(lambda x: True if ((x['letter'] == x['char_min']) & (x['letter'] == x['char_max']))
                                                | ((x['letter'] != x['char_min']) & (x['letter'] != x['char_max'])) else False, axis=1)
sum(data['invalid2']==False)