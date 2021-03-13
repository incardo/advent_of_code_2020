# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 20:11:53 2020

@author: incardo
"""

import pandas as pd
import numpy as np

with open('C://Users//incar//PycharmProjects//Advent_calendar//venv//day11_input.txt') as f:
    contents = [line.rstrip() for line in f]

#Part1

def find_adjacents(data, row, col):
    width = len(data[0])
    height = len(data)

    possible_rows = []
    if row-1>=0: possible_rows.append(row-1)
    if row+1<=height-1: possible_rows.append(row+1)
    possible_rows.append(row)

    possible_cols = []
    if col - 1 >= 0: possible_cols.append(col - 1)
    if col + 1 <= width - 1: possible_cols.append(col + 1)
    possible_cols.append(col)

    #print(possible_cols, possible_rows)
    adjacent_cells = [data[x][y] for x in possible_rows for y in possible_cols if [x, y] != [row, col]]
    return adjacent_cells

def set_empty_to_occupied(data, row, col):
    if data[row][col] == 'L':
        if '#' not in find_adjacents(data, row, col):
            #print('Cell ' + str(row), str(col) + ' should be occupied')
            return '#'
        else:
            #print('Adjacent cells not empty - no change for cell '+str(row), str(col))
            return data[row][col]
    else:
        return data[row][col]


def set_occupied_to_empty(data, row, col):
    if data[row][col] == '#':
        if len([elem for elem in find_adjacents(data, row, col) if elem == '#'])>=4:
            #print('Cell '+str(row), str(col)+' should be empty')
            return 'L'
        else:
            #print('Less than 4 adjacent cells are occupied - no change for cell '+str(row), str(col))
            return data[row][col]
    else:
        return data[row][col]

def round_change(data):

    data_it1 = data.copy()
    for row in range(0, len(data_it1)):
        for col in range(0, len(data_it1[0])):
            #print(row, col, data_new[row][col])
            new_seat = set_empty_to_occupied(data, row, col)
            if col +1 <= len(data_it1[0])-1:
                data_it1[row] = data_it1[row][:col] + str(new_seat) + data_it1[row][col + 1:]
            else:
                data_it1[row] = data_it1[row][:col] + str(new_seat)

    data_it2 = data_it1.copy()
    for row in range(0, len(data_it2)):
        for col in range(0, len(data_it2[0])):
            #print(row, col, data_new[row][col])
            new_seat = set_occupied_to_empty(data_it1, row, col)
            if col +1 <= len(data_it2[0])-1:
                data_it2[row] = data_it2[row][:col] + str(new_seat) + data_it2[row][col + 1:]
            else:
                data_it2[row] = data_it2[row][:col] + str(new_seat)
    return data_it2

def get_stable_seats(data):
    data_start = data.copy()
    data_end = round_change(data_start)
    while data_start != data_end:
        data_start = data_end.copy()
        data_end = round_change(data_start)
    print('Stable seats found: '+ str(''.join(data_end).count('#')))
    return data_end

get_stable_seats(contents)


#Part2

def find_adjacents_all_dir(data, row, col):
    width = len(data[0])
    height = len(data)

    possible_rows = []
    if row-1>=0: possible_rows.append(row-1)
    if row+1<=height-1: possible_rows.append(row+1)
    possible_rows.append(row)

    possible_cols = []
    if col - 1 >= 0: possible_cols.append(col - 1)
    if col + 1 <= width - 1: possible_cols.append(col + 1)
    possible_cols.append(col)

    print(possible_cols, possible_rows)
    adjacent_cells = []
    for x in possible_rows:
        for y in possible_cols:
            if [x, y] != [row, col]:
                if data[x][y] != '.':
                    adjacent_cells.append(data[x][y])
                elif data[x][y] == '.':
                    adj_exp = data[x][y]
                    var_x = x - row
                    var_y = y - col
                    while adj_exp == '.':
                        #print(x + var_x, y + var_y)
                        if (x+var_x<0) | (y+var_y<0) | (x+var_x>height-1) | (y+var_y>width-1):
                            break
                        if data[x+var_x][y+var_y] != '.':
                            adjacent_cells.append(data[x+var_x][y+var_y])
                        adj_exp = data[x+var_x][y+var_y]
                        if var_x != 0: var_x = var_x + (np.sign(var_x))
                        if var_y != 0: var_y = var_y + (np.sign(var_y))

    return adjacent_cells

def set_empty_to_occupied_new(data, row, col):
    if data[row][col] == 'L':
        if '#' not in find_adjacents_all_dir(data, row, col):
            #print('Cell ' + str(row), str(col) + ' should be occupied')
            return '#'
        else:
            #print('Adjacent cells not empty - no change for cell '+str(row), str(col))
            return data[row][col]
    else:
        return data[row][col]


def set_occupied_to_empty_new(data, row, col):
    if data[row][col] == '#':
        if len([elem for elem in find_adjacents_all_dir(data, row, col) if elem == '#'])>=5:
            #print('Cell '+str(row), str(col)+' should be empty')
            return 'L'
        else:
            #print('Less than 4 adjacent cells are occupied - no change for cell '+str(row), str(col))
            return data[row][col]
    else:
        return data[row][col]

def round_change_new(data):
    data_it1 = data.copy()
    for row in range(0, len(data_it1)):
        for col in range(0, len(data_it1[0])):
            #print(row, col, data_it1[row][col])
            new_seat = set_empty_to_occupied_new(data, row, col)
            if col +1 <= len(data_it1[0])-1:
                data_it1[row] = data_it1[row][:col] + str(new_seat) + data_it1[row][col + 1:]
            else:
                data_it1[row] = data_it1[row][:col] + str(new_seat)

    data_it2 = data_it1.copy()
    for row in range(0, len(data_it2)):
        for col in range(0, len(data_it2[0])):
            #print(row, col, data_it2[row][col])
            new_seat = set_occupied_to_empty_new(data_it1, row, col)
            if col +1 <= len(data_it2[0])-1:
                data_it2[row] = data_it2[row][:col] + str(new_seat) + data_it2[row][col + 1:]
            else:
                data_it2[row] = data_it2[row][:col] + str(new_seat)
    return data_it2

def get_stable_seats_new(data):
    data_start = data.copy()
    data_end = round_change_new(data_start)
    while data_start != data_end:
        data_start = data_end.copy()
        data_end = round_change_new(data_start)
    print('Stable seats found: '+ str(''.join(data_end).count('#')))
    return data_end

get_stable_seats_new(contents)

for row in contents:
    print(row)

find_adjacents_all_dir(contents, 8, 95)