import pandas as pd
import numpy as np
import re
from itertools import product


with open('C://Users//incar//PycharmProjects//Advent_calendar//venv//day16_input.txt') as f:
    tickets = [line.rstrip() for line in f]

#PART1
rules = tickets[0:20]
myticket = tickets[22]
nearby_tickets = [re.split(',', ticket) for ticket in tickets[25:]]
rules_split = [re.split(': |-| or ', rule) for rule in rules]

invalid_nrs = []
for index, nticket in enumerate(nearby_tickets):
   print('Checking ticket nr: '+str(index))
   for number in nticket:
      valid_rule = 0
      for rule in rules_split:
        if ((int(number) >= int(rule[1])) & (int(number) <= int(rule[2]))) | ((int(number) >= int(rule[3])) & (int(number) <= int(rule[4]))):
            #print(number, 'is valid for rule', rule)
            valid_rule += 1
        else:
            print(number, 'is INVALID for rule', rule)
      if valid_rule == 0 :
        invalid_nrs.append(int(number)) #Number is not valid for any rule
print(invalid_nrs)
print('ticket scanning error rate ', sum(invalid_nrs))

#PART2

#Discard invalid tickets
valid_tickets = []
for index, nticket in enumerate(nearby_tickets):
    invalid_nr = 0
    for number in nticket:
        if int(number) in invalid_nrs:
            invalid_nr +=1
    if invalid_nr == 0:
        valid_tickets.append(nticket)
        print('Ticket nr ', str(index), 'is valid')
print(valid_tickets)

#identify the fields

field1 = [ticket[0] for ticket in valid_tickets]

def check_valid_rule(field, rules_to_check):
    valid_rules=[]
    for rule in rules_to_check:
        rule_counter = 0
        for number in field:
            if ((int(number) >= int(rule[1])) & (int(number) <= int(rule[2]))) | ((int(number) >= int(rule[3])) & (int(number) <= int(rule[4]))):
                rule_counter +=1
                #(number, 'is valid for rule', rule)
        if rule_counter == len(field):
            #print('This column can be ', rule[0])
            valid_rules.append(rule[0])
    return valid_rules


check_rules = rules_split
fields_found =dict()
while len(fields_found) < len(valid_tickets[0]):
    for field in range(0, len(valid_tickets[0])):
        #print('Checking field', str(field))
        valid_fields = check_valid_rule([ticket[field] for ticket in valid_tickets], check_rules) if field not in list(fields_found.values()) else None
        if len(valid_fields) == 1:
            print('Field '+str(field)+' is '+ valid_fields[0])
            check_rules = [rule for rule in check_rules if  rule[0] != valid_fields[0]]
            fields_found[field] = valid_fields[0]

fields_found = dict(sorted(fields_found.items()))
fields_found

myticket_split = myticket.split(',')
departure_index = [k for k,v in fields_found.items() if 'departure' in v]

def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result

multiplyList([int(myticket_split[index]) for index in departure_index])





