import pandas as pd
import time
import numpy as np
import re

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


data = pd.read_csv('C://Users//incar//PycharmProjects//Advent_calendar//venv//day9_input.txt', header = None)
data.rename(columns = {0:'numbers'}, inplace = True)
print(data)

#PART1
start_range = 0
end_range = 24

data['numbers'][25]

data['Index'] = ''

def check_sum(number_index):
    for index in range(number_index - 25, number_index):
        numbers_found = False
        for index_sum in range(number_index - 25, number_index):
            if index_sum == index:
                continue
            elif data['numbers'][number_index] != data['numbers'][index] + data['numbers'][index_sum]:
                continue
                # print('Numbers not summing:'+ str(data['numbers'][index]) +'+' + str(data['numbers'][index_sum]) + '!=' + str(data['numbers'][25]))
            elif data['numbers'][number_index] == data['numbers'][index] + data['numbers'][index_sum]:
                print('Sum found:' + str(data['numbers'][index]) + '+' + str(data['numbers'][index_sum]) + '=' + str(
                    data['numbers'][number_index]))
                numbers_found = True
                break
        if numbers_found == True:
            break
        elif index == number_index and numbers_found == False:
            Print('no number has been found for ' + data[index + 1] + ' index ' + index)
        else:
            continue
    return numbers_found



for number_index in range(25, len(data.numbers)):
    if check_sum(number_index) == False:
        print('No number found for '+str(data.numbers[number_index]) + ' index ' + str(number_index))
        break


#PART 2
for start_range in range(0, 539):
    for end_range in range(start_range+1, 539):
        if sum(data.numbers[start_range:end_range]) == 41682220:
            print('Sum found in range '+str(start_range)+' and '+str(end_range))
            data.numbers[start_range:end_range]
            print('Sum: '+str(max(data.numbers[start_range:end_range]+min(data.numbers[start_range:end_range]))))
            break
