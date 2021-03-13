import pandas as pd
import time
import numpy as np
import re

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


data = pd.read_csv('C://Users//incar//PycharmProjects//Advent_calendar//venv//day5_input.txt', header = None)
print(data)

data.rename(columns = {0:'seats'}, inplace = True)

#Seats from 0 to 127
#Columns from 0 to 7

data['Row'] = ''
data['Col'] = ''
data['Mult'] = ''

for index, seat in data.seats.iteritems():
    print(seat)
    upper_row = int(127)
    lower_row = int(0)
    upper_col = int(7)
    lower_col = int(0)
    print(upper_row, lower_row, upper_col, lower_col)
    for char in seat:
        diff_row = upper_row - lower_row
        diff_col = upper_col - lower_col
        if char == 'F':
            upper_row = int(upper_row-(diff_row+ 1)/2)
        elif char == 'B':
            lower_row = int(lower_row + (diff_row + 1)/2)
        elif char == 'L':
            upper_col = int(upper_col-(diff_col+1)/2)
        elif char == 'R':
            lower_col = int(lower_col + (diff_col + 1)/2)
        print(upper_row, lower_row, upper_col, lower_col)
    data['Row'][index] = upper_row
    data['Col'][index] = upper_col
    data['Mult'][index] = upper_row * 8 + upper_col

    print('Seat '+seat+': Row - '+str(int(upper_row)) + ' Col - '+str(int(upper_col))+ ' Mult: '+str(upper_row * 8 + upper_col))

    max(data.Mult)

#Part 2

list_seats = []
for row in range(0, 128):
    for col in range(0, 8):
        list_seats += [[row, col]]

present_seats = []
for index, row in data.iterrows():
     if [data['Row'][index], data['Col'][index]] in list_seats:
         present_seats += [[data['Row'][index], data['Col'][index]]]

missing_seats = [x for x in list_seats if x not in present_seats]

print('ID '+str(81*8+1))


