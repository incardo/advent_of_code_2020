# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 14:25:13 2020

@author: incardo
"""

#PART 1

import pandas as pd
import numpy as np

data = pd.read_csv('C://Users//incar//PycharmProjects//Advent_calendar//venv//day10_input.txt', header = None)
data.columns = ['jolts']

data = data.sort_values(by = 'jolts', ascending = True).reset_index(drop=True)

data = pd.concat([pd.DataFrame({'jolts':[0]}), data], axis = 0).reset_index(drop=True)
data_diff = data.diff(axis = 0)

print('jolts multiplication = '+str((len(data_diff[data_diff.jolts==3])+1) * len(data_diff[data_diff.jolts==1])))


data_diff.jolts.value_counts()

#PART 2

# part 2

count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0

counter = 0
for index, row in data_diff.iterrows():
    if index != 0:
        print('index', index)
        if data_diff.iloc[index].jolts == 1:
            counter += 1
            print('counter', counter)
            if (index != len(data_diff)-1):
                print('next:',data_diff.iloc[index+1].jolts )
                if (counter == 1) & (data_diff.iloc[index+1].jolts == 3):
                    count_1 +=1
                    counter = 0
                elif (counter == 2) & (data_diff.iloc[index+1].jolts == 3):
                    count_2 +=1
                    counter = 0
                elif (counter == 3) & (data_diff.iloc[index+1].jolts == 3):
                    count_3 += 1
                    counter = 0
                elif (counter == 4) & (data_diff.iloc[index+1].jolts == 3):
                    count_4 += 1
                    counter = 0
            else:
                if (counter == 1):
                    count_1 +=1
                    counter = 0
                if (counter == 2):
                    count_2 +=1
                    counter = 0
                elif (counter == 3):
                    count_3 += 1
                    counter = 0
                elif (counter == 4) :
                    count_4 += 1
                    counter = 0            
    print(count_3, count_4)
print('counter_1:', count_1, 'counter_2:', count_2, 'counter_3:', count_3, 'counter_4:', count_4)



print('Total possibilities ', str((2**count_2)*(4**count_3)*(7**count_4)))

