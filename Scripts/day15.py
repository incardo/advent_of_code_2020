import pandas as pd
import numpy as np
import re
from itertools import product


with open('C://Users//incar//PycharmProjects//Advent_calendar//venv//day15_input.txt') as f:
    starting_num = [line.rstrip().split(',') for line in f]

#sequence = [3,1,2]
sequence = starting_num[0].copy()
sequence = [ int(x) for x in sequence ]

def speak_number(sequence, number_to_speak):
    for i in range(0, number_to_speak):
        print(i)
        if i > len(sequence)-1:
            #print('checking index '+str(i)+' previous:'+ str(sequence[i-1]))
            if sequence.count(sequence[i-1]) == 1:
                sequence.append(0)
            elif sequence.count(sequence[i-1]) > 1:
                spoken_rounds = [index for index, x in enumerate(sequence) if x == sequence[i-1]]
                #print(spoken_rounds)
                sequence.append(spoken_rounds[-1]-spoken_rounds[-2])
            #print('New number: '+str(sequence[i]))
    print('Last number in 2020th position:'+str(sequence[-1]))

speak_number(sequence, 2020)

#Part2
sequence = starting_num[0].copy()
sequence = [ int(x) for x in sequence ]
#speak_number(sequence, 30000000) too slow

def speak_number_fast(sequence, number_to_speak):
    starting_nums = [ int(x) for x in sequence ]
    last_times_spoken_dict = dict(zip(starting_nums, range(1, len(starting_nums) + 1)))
    last_time_spoken = None  # assume that starting nums contain no duplicates
    for turn in range(len(starting_nums) + 1, number_to_speak + 1):
        spoken_num = 0 if last_time_spoken is None else (turn - 1) - last_time_spoken
        last_time_spoken = last_times_spoken_dict[spoken_num] if spoken_num in last_times_spoken_dict else None
        last_times_spoken_dict[spoken_num] = turn
    print(spoken_num)
B
 speak_number_fast(sequence, 30000000)