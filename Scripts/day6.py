import pandas as pd
import time
import numpy as np
import re

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#PART1

file_input = open('C://Users//incar//PycharmProjects//Advent_calendar//venv//day6_input.txt', 'r')
with file_input as f:
    lines = [line.rstrip() for line in f]

lines_split = ' '.join(lines).split('  ')
groups_list = [list(set(x.replace(' ', ''))) for x in lines_split]

count_questions = 0
for group in groups_list:
    count_questions += len(group)

print('Total count ' + str(count_questions))

#PART2
groups_list2 = [list(x.split(' ')) for x in lines_split]

count_questions2 = 0
for group in groups_list2:
    print(group, set.intersection(*map(set,group)))
    count_questions2 += len(set.intersection(*map(set,group)))

print('Total count ' + str(count_questions2))

