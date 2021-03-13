import pandas as pd
import numpy as np

with open('C://Users//incar//PycharmProjects//Advent_calendar//venv//day12_input.txt') as f:
    instructions = [line.rstrip() for line in f]

#PART1
position = [0, 0, 0]
for row in instructions:
    print('Start position: '+str(position))
    if row[0] == 'N':
        position[1] +=  int(row[1:])
    elif row[0] == 'S':
        position[1] -=  int(row[1:])
    elif row[0] == 'E':
        position[0] += int(row[1:])
    elif row[0] == 'W':
        position[0] -= int(row[1:])
    elif row[0] == 'L':
        position[2] -= int(row[1:])
        position[2] = (abs(position[2])-360) * np.sign(position[2]) if abs(position[2]) >=360 else position [2]
    elif row[0] == 'R':
        position[2] += int(row[1:])
        position[2] = (abs(position[2])-360) * np.sign(position[2]) if abs(position[2]) >=360 else position [2]
    elif row[0] == 'F':
        if (position[2] == 0): #E
            position[0] += int(row[1:])
        elif (position[2] == 90) | (position[2] == -270): #S
            position[1] -= int(row[1:])
        elif (position[2] == 180) | (position[2] == -180):  #W
            position[0] -= int(row[1:])
        elif (position[2] == 270) | (position[2] == -90):  #N
            position[1] += int(row[1:])
    print('New position: '+str(position))

print(abs(position[0])+abs(position[1]))

#PART2
position = [0, 0]
waypoint = [10, 1]
for row in instructions:
    print('Start position: '+str(position))
    print('Start waypoint: ' + str(waypoint))
    print(row)
    if row[0] == 'N':
        waypoint[1] +=  int(row[1:])
    elif row[0] == 'S':
        waypoint[1] -=  int(row[1:])
    elif row[0] == 'E':
        waypoint[0] += int(row[1:])
    elif row[0] == 'W':
        waypoint[0] -= int(row[1:])
    elif row[0] == 'L':
        if int(row[1:])== 90: #rotate anticlockwise from EN to WN
            waypoint[0],waypoint[1]  = -waypoint[1], waypoint[0]
        elif int(row[1:]) == 180: #rotate anticlockwise from EN to WS
            waypoint[0], waypoint[1]  = -waypoint[0], -waypoint[1]
        elif int(row[1:]) == 270: #rotate anticlockwise from EN to ES
            waypoint[0], waypoint[1]  = waypoint[1], -waypoint[0]
    elif row[0] == 'R':
        if int(row[1:]) == 90:  # rotate clockwise from EN to ES
            waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
        elif int(row[1:]) == 180:  # rotate clockwise from EN to WS
            waypoint[0], waypoint[1] = -waypoint[0], -waypoint[1]
        elif int(row[1:]) == 270:  # rotate clockwise from EN to WN
            waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
    elif row[0] == 'F':
            position[0] += waypoint[0]*int(row[1:])
            position[1] += waypoint[1]*int(row[1:])
    print('New position: '+str(position))
    print('New waypoint: ' + str(waypoint))

print(abs(position[0])+abs(position[1]))


