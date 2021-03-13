import pandas as pd
import time
import numpy as np
import re

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


file_input = open('C://Users//incar//PycharmProjects//Advent_calendar//venv//day4_input.txt', 'r')
with file_input as f:
    lines = [line.rstrip() for line in f]

lines_split = ' '.join(lines).split('  ')
passport_list = [line.split(' ') for line in lines_split]

passport_columns = ['byr','iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

passport_df = pd.DataFrame(index=range(0,len(passport_list)),columns=passport_columns)

for row_index in range(0,len(passport_list)):
    row = passport_list[row_index]
    for id_col in row:
        col_title = id_col.split(sep=":")[0]
        col_value = id_col.split(sep=":")[1]
        print(col_title, col_value)
        passport_df[str(col_title)][row_index] = col_value

passport_df['invalid']=''
for index, row in passport_df.iterrows():
    print('index '+ str(index) )
    print(passport_df.iloc[index])
    if  (pd.isnull(passport_df['byr'][index])) | \
        (pd.isnull(passport_df['iyr'][index])) | \
        (pd.isnull(passport_df['eyr'][index])) | \
        (pd.isnull(passport_df['hgt'][index])) | \
        (pd.isnull(passport_df['hcl'][index])) | \
        (pd.isnull(passport_df['ecl'][index])) | \
        (pd.isnull(passport_df['pid'][index])):
        passport_df['invalid'][index] = True
    else: passport_df['invalid'][index] = False

print('Valid passports: ', len(passport_df[passport_df.invalid == False]))

#Part 2
def validate_years(year, min_target, max_target):
    #try:
        if (sum(c.isdigit() for c in str(year)) == 4) & \
           (int(year) >= min_target) & (int(year) <= max_target):
            return True
        else:
            print('Invalid year')
            return False
    #except:
    #    print('Invalid year')
    #    return False


def validate_hgt(hgt):
    #try:
        if  (hgt[-2:] == 'cm') | (hgt[-2:] == 'in'):
            if ((hgt[-2:] == 'cm') & (int(hgt[0:-2]) >= 150) & (int(hgt[0:-2]) <= 193)) | \
               ((hgt[-2:] == 'in') & (int(hgt[0:-2]) >= 59) & (int(hgt[0:-2]) <= 76)):
                return True
            else:
                return False
                print('Invalid hgt')
        else:
            return False
            print('Invalid hgt')

    #except:
    #    return False
    #    print('Invalid hgt')

def validate_hcl(hcl):
    if ((hcl[0] == "#") & (len(re.findall('[#]', hcl)) )==1) & (len(hcl) == 7) & ((len(re.findall('[a-f]', hcl))>0) | (sum(map(str.isnumeric, hcl)) == 6)):
        return True
    else:
        return False
        print('Invalid hcl')


def validate_ecl(ecl):
    if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    else:
        return False
        print('Invalid ecl')

def validate_pid(pid):
    if (sum(map(str.isnumeric, pid)) == 9):
        return True
    else:
        return False
        print('Invalid pid')


passport_df['invalid2']=''
for index, row in passport_df.iterrows():
    print('index '+ str(index) )

    if passport_df['invalid'][index] == True:
        passport_df['invalid2'][index] = True
    else:
        if  (validate_years(passport_df['byr'][index], 1920, 2002)) & \
            (validate_years(passport_df['iyr'][index], 2010, 2020)) & \
            (validate_years(passport_df['eyr'][index], 2020, 2030)) & \
            (validate_hcl(passport_df['hcl'][index])) & \
            (validate_hgt(passport_df['hgt'][index])) & \
            (validate_ecl(passport_df['ecl'][index])) & \
            (validate_pid(passport_df['pid'][index])):
                passport_df['invalid2'][index] = False
        else: passport_df['invalid2'][index] = True
    print(passport_df.iloc[index])

print('Valid passports 2: ', len(passport_df[passport_df.invalid2 == False]))



index = 72
(validate_years(passport_df['byr'][index], 1920, 2002)) &\
(validate_years(passport_df['iyr'][index], 2010, 2020)) & \
(validate_years(passport_df['eyr'][index], 2020, 2030)) & \
(validate_hcl(passport_df['hcl'][index])) & \
(validate_hgt(passport_df['hgt'][index])) & \
(validate_ecl(passport_df['ecl'][index])) & \
(validate_pid(passport_df['pid'][index]))

passport_df[(passport_df.invalid2 == False) ]