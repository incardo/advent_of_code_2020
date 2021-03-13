import pandas as pd
import numpy as np

with open('C://Users//incar//PycharmProjects//Advent_calendar//venv//day13_input.txt') as f:
    timetable = [line.rstrip() for line in f]

#PART1
start_time = int(timetable[0])
list_bus = [int(bus) for bus in timetable[1].split(',') if bus != 'x']

stop_found = False
timestamp = start_time
bus_stopping = None
while stop_found == False:
    for bus in list_bus:
        print('Time:',str(timestamp) ,'Bus:', str(bus), str(timestamp % bus))
        if timestamp%bus == 0:
            stop_found = True
            bus_stopping = bus
    if stop_found == False: timestamp +=1

print('First bus stops in '+ str(timestamp-start_time) + 'min BusID:'+str(bus_stopping))
print('Answer: '+str((timestamp-start_time)*bus_stopping))

#PART2

list_bus_ind = [[i , int(timetable[1].split(',')[i])] for i in range(0, len(timetable[1].split(','))) if timetable[1].split(',')[i]!= 'x']

timestamp = list_bus_ind[0][1]
bus_counter = 0

len(list_bus_ind) #9 buses need to leave at the same time
timestamp = 23
while bus_counter !=9:
    bus_counter = 0
    for bus in list_bus_ind:
        print('checking bus'+str(bus[1])+' lag '+str(bus[0] )+' timestamp ' +str(timestamp))
        if (timestamp + bus[0]) % bus[1] == 0:
            print('Bus '+str(bus[1])+' Leaving at '+str(timestamp + bus[0]))
            bus_counter += 1
            print(bus_counter)
        else:
            print('breaking sequence at '+str(timestamp))
            break
    if bus_counter==1:
        timestamp +=list_bus_ind[0][1]
    elif bus_counter == 2:
        timestamp += list_bus_ind[0][1]*list_bus_ind[1][1]
    elif bus_counter ==3:
        timestamp += list_bus_ind[0][1] * list_bus_ind[1][1]* list_bus_ind[2][1]
    elif bus_counter ==4:
        timestamp += list_bus_ind[0][1] * list_bus_ind[1][1]* list_bus_ind[2][1] \
                     * list_bus_ind[3][1]
    elif bus_counter == 5:
        timestamp += list_bus_ind[0][1] * list_bus_ind[1][1]* list_bus_ind[2][1] \
                     * list_bus_ind[3][1]* list_bus_ind[4][1]
    elif bus_counter == 6:
        timestamp += list_bus_ind[0][1] * list_bus_ind[1][1]* list_bus_ind[2][1] \
                     * list_bus_ind[3][1]* list_bus_ind[4][1]* list_bus_ind[5][1]
    elif bus_counter ==7:
        timestamp += list_bus_ind[0][1] * list_bus_ind[1][1]* list_bus_ind[2][1] \
                     * list_bus_ind[3][1]* list_bus_ind[4][1]* list_bus_ind[5][1]   * list_bus_ind[6][1]
    elif bus_counter ==8:
        timestamp += list_bus_ind[0][1] * list_bus_ind[1][1]* list_bus_ind[2][1] \
                     * list_bus_ind[3][1]* list_bus_ind[4][1]* list_bus_ind[5][1]   * list_bus_ind[6][1] * list_bus_ind[7][1]
    elif bus_counter==9:
        print('Sequence bus leaving together at :'+str(timestamp))
        print('Time:',str(timestamp) ,'Bus:', str(bus), str(timestamp % bus))


