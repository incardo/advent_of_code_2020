import pandas as pd
import numpy as np
import re
from itertools import product


with open('C://Users//incar//PycharmProjects//Advent_calendar//venv//day14_input.txt') as f:
    program = [line.rstrip() for line in f]

#Convert number to binary representation
f'{101:036b}'

def apply_mask(mask, value):
    val_bin = f'{value:036b}'
    result_bin = val_bin
    for index, bit in enumerate(mask):
        if bit != 'X':
            result_bin = result_bin[0:index]+mask[index]+result_bin[index+1:]
      result=int(result_bin, 2)
    return result

#apply_mask('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 11)

memory = {}
for item in program:
    if item[0:4] == 'mask':
        mask = item[7:len(item)]
    if item[0:3] == 'mem':
        address = item[4:item.find(']')]
        value = int(item[item.find('=')+2:len(item)])
        memory[address] = apply_mask(mask, value)

#Sum of all the numbers in memory
sum(memory.values())

#PART 2

def apply_mask2(mask, value):
    val_bin = f'{value:036b}'
    result_bin = val_bin
    for index, bit in enumerate(mask):
        if bit != '0':
            result_bin = result_bin[0:index]+mask[index]+result_bin[index+1:]
    return result_bin

memory = {}
for item in program:
    if item[0:4] == 'mask':
        mask = item[7:len(item)]
    if item[0:3] == 'mem':
        address = int(item[4:item.find(']')])
        value = int(item[item.find('=')+2:len(item)])
        generic_address = apply_mask2(mask, address)

        num_floats = len([m.start() for m in re.finditer('X', generic_address)])
        list_rep = list(product([0, 1], repeat=num_floats))
        for comb in list_rep:
            float_address = generic_address
            for index, float_pos in enumerate([m.start() for m in re.finditer('X', generic_address)]):
                float_address = float_address[0:float_pos]+str(comb[index])+float_address[float_pos+1:]
            memory[int(float_address, 2)] = value
#Sum of all the numbers in memory
sum(memory.values())
