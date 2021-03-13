import pandas as pd
import time
import numpy as np

pd.set_option('display.max_columns', None)

data = pd.read_csv('C://Users//incar//PycharmProjects//Advent_calendar//venv//day3_input.txt', header = None)
print(data)

data = data[0].astype('str')

#Part 1
max_lenght = len((data.iloc[0]))
pos = 0
count_trees = 0

for i, row in data.iteritems():
    print("row " + str(i) + " position " + str(pos))
    print(data.iloc[i][pos])
    if data.iloc[i][pos] == "#":
        count_trees +=1

    pos += 3
    if pos > max_lenght-1:
        pos -=max_lenght

print("Trees encountered: "+str(count_trees))

#Part 2

max_lenght = len((data.iloc[0]))
multiplication = 1

for shift in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
    pos = 0
    count_trees = 0

    print("Shift: ", shift[0], shift[1])

    for i in range(0,len(data), shift[1]):
        print("row " + str(i) + " position " + str(pos))
        print(data.iloc[i][pos])
        if data.iloc[i][pos] == "#":
            count_trees +=1

        pos += shift[0]
        if pos > max_lenght-1:
            pos -=max_lenght

    print("Trees encountered: "+str(count_trees), "in shift ", shift)
    multiplication *= count_trees

print("Final multiplication " , multiplication)
