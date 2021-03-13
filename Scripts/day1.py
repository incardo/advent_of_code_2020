
#################################à
import pandas as pd
import time

data = pd.read_csv('C://Users//incar//PycharmProjects//Advent_calendar//venv//day1_input.txt', header = None)
print(data)

def find_prod_of_pair(nums, target=2020):
    pairs = target - nums
    for i, pair in enumerate(pairs):
        if pair in set(nums):
            print(nums[i]*pair)
            print(pair, nums[i])
            break

start = time.time()
find_prod_of_pair(data[0])
end = time.time()
print(end - start)

def find_prod_of_three(nums, target=2020):
    for i, n in enumerate(nums):
        for j, m, in enumerate(nums):
        if 2020-n-m in set(nums):
            print(n * m * (2020-n-m))
            print(n, m, 2020-n-m)
            break

start = time.time()
find_prod_of_three(data[0])
end = time.time()
print(end - start)