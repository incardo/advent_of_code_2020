import pandas as pd
import time
import numpy as np
import re

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


data = pd.read_csv('C://Users//incar//PycharmProjects//Advent_calendar//venv//day8_input.txt', header = None)
print(data)

data.rename(columns = {0:'init'}, inplace = True)
data = data['init'].str.split(' ',expand=True)
data.rename(columns = {0:'instr', 1:'num'}, inplace = True)

#PART1

accumulator = 0
index = 0
data['stop'] = 0

while data['stop'][index] == 0:
    print(index, accumulator)
    data.iloc[index, :]
    if data['instr'][index] == 'acc':
        accumulator += int(data['num'][index])
        data['stop'][index] = 1
        index += 1
    elif data['instr'][index] == 'jmp':
        data['stop'][index] = 1
        index += int(data['num'][index])
    elif data['instr'][index] == 'nop':
        data['stop'][index] = 1
        index += 1
print(accumulator)

#PART2

def run_program(data):
    accumulator = 0
    index = 0
    data['stop'] = 0
    end_loop = 0

    while (data['stop'][index] == 0):
        print(index, accumulator)
        if data['instr'][index] == 'acc':
            accumulator += int(data['num'][index])
            data['stop'][index] = 1
            index += 1
        elif data['instr'][index] == 'jmp':
            data['stop'][index] = 1
            index += int(data['num'][index])
        elif data['instr'][index] == 'nop':
            data['stop'][index] = 1
            index += 1
        print('Execution stopped at index:', index, 'Accumulator =', accumulator)

        if index == len(data['instr']):
            end_loop = 1
            break
    print('The program was executed correctly - index:', index, 'Accumulator =', accumulator)
    return True if end_loop == 1 else False

data['instr_orig'] = data['instr'].copy()

for index, row in data[data.instr=='jmp'].iterrows():
    print('Checking jmp '+str(index))
    data['instr'][index] = 'nop'
    if run_program(data) ==True:
        break
    data['instr']=data['instr_orig'].copy()
    print('The jmp in this position was changed to nop: ' + str(index))


