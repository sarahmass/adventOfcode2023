import os
import sys
import numpy as np
import re
import time
import math

TEST_INPUT = [
    '0 3 6 9 12 15',
    '1 3 6 10 15 21',
    '10 13 16 21 30 45', 
]


def read_input(day, test = False):
    if test:
        return TEST_INPUT
    file_name = os.path.join("my_inputs",f"adventDay{day}_input.txt")
    with open(file_name, "r") as f:
        flines = f.readlines()
    return flines

def map_to_int(s):
    return list(map(lambda i: int(i),s.strip().split(" ")))

def extract_next_num(seq, part = 'a'):
    last_numbs = [seq[-1]]
    first_numbs = [seq[0]]
    while seq.count(0) != len(seq):
        next_seq = []
        for i in range(1,len(seq)):
            next_seq.append(seq[i]-seq[i-1])
        last_numbs.append(next_seq[-1])
        if len(first_numbs) % 2 == 1:
            # after working out the system of equations
            # it turns out that if the original first
            # num in the series is x0 then subtract
            # x1 which is the first num of the first
            # difference, then add x2 the first num
            # in the second difference seq. and so on
            first_numbs.append(-1* next_seq[0])
        else:
            first_numbs.append(next_seq[0])
        seq = next_seq[:]
    if part == 'a':
        return sum(last_numbs)
    else:
        return sum(first_numbs)
        
            
            


if __name__ == '__main__':
    time_start = time.time()
    test = False
    part = "b"
    day = 9
    data = read_input(day = day, test=test)
    sum_of_next_nums = 0
    for i,line in enumerate(data):
        if line.strip() == '':
            continue
        seq = map_to_int(line)
        # real_first = seq.pop(0)
        next_num = extract_next_num(seq, part)
        # print(real_first)
        # print(next_num)
        # print(real_first==next_num)
        # assert(next_num==real_first)
        sum_of_next_nums += next_num
    print(f"Day {day}, Advent of Code part {part} solution: {sum_of_next_nums}")