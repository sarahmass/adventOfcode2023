import os
import sys
import numpy as np
import re
import time
import math


day = 5



TEST_INPUT = [
    'RL',
    'AAA = (BBB, CCC)',
    'BBB = (DDD, EEE)',
    'CCC = (ZZZ, GGG)',
    'DDD = (DDD, DDD)',
    'EEE = (EEE, EEE)',
    'GGG = (GGG, GGG)',
    'ZZZ = (ZZZ, ZZZ)',
              ]
TEST_INPUT2 = [
    'LLR',
    'AAA = (BBB, BBB)',
    'BBB = (AAA, ZZZ)',
    'ZZZ = (ZZZ, ZZZ)'
    ]
TEST_INPUTb = [
    'LR',
    '11A = (11B, XXX)',
    '11B = (XXX, 11Z)',
    '11Z = (11B, XXX)',
    '22A = (22B, XXX)',
    '22B = (22C, 22C)',
    '22C = (22Z, 22Z)',
    '22Z = (22B, 22B)',
    'XXX = (XXX, XXX)',
]


def read_input(day, test = False):
    if test:
        return TEST_INPUTb
    file_name = os.path.join("my_inputs",f"adventDay{day}_input.txt")
    with open(file_name, "r") as f:
        flines = f.readlines()
    return flines

def map_to_int(s):
    return list(map(lambda i: int(i),s.strip().split(" ")))

def clean_input(dataf, part = 'a'):
    # first line: 'RL...',
    init_line = dataf.pop(0).strip()
    index_pattern = list(map(lambda x: int(x == 'R'), init_line))
            
    # next line: "'AAA = (BBB, CCC)'"
    conv_table = {}
    line_no = 0
    if part == 'a':
        starts = ["AAA"]
    elif part == 'b':
        starts = []
    while line_no < (len(dataf)):

        # ignore empty lines 
        if dataf[line_no].strip() == '':
            line_no += 1
            continue
        
        # get source and destination codes an store in dictionary
        source, destinations = dataf[line_no].strip().split("=")
        source = source.strip()
        
        # for part b get starting sources that end in A
        if part == 'b'and source[-1] == 'A':
            starts.append(source)

        destinations = destinations.strip().replace("(", "")
        destinations = destinations.strip().replace(")", "")
        destinations = destinations.split(", ")
        conv_table[source] = destinations
        line_no += 1 
    print("done cleaning")  
    return (index_pattern, conv_table, starts) 

def count_steps(pattern, conv_table, part='a', start = 'AAA'):
    count = 0
    len_pattern = len(pattern)
    source = start
    
    while True:
        direction = pattern[count % len_pattern]
        source = conv_table[source][direction]
        count += 1
        if part == "a" and source == 'ZZZ':
            return count
        if part == 'b' and source[-1]=='Z':
            return count
       
if __name__ == '__main__':
    time_start = time.time()
    test = False
    part = "b"
    day = 8
    data = read_input(day = day, test=test)
    pattern, conv_table, starts = clean_input(data, part = part)
    num_steps_all = []
    count = 1
    for start in starts:
        num_steps = count_steps(pattern,conv_table, part,start)
        num_steps_all.append(num_steps)
    gcd_steps = math.gcd(*num_steps_all)
    count = gcd_steps
    for num in num_steps_all:
        num = num//gcd
        count *= num
    
    total_time = time.time() - time_start
    print(f"day {day} advent of code part {part} answer was found in {total_time}sec")
    print(f"The number of cycles through the {len(pattern)} direction list {num_steps_all}")
    print(f"Total steps to simultaneously land on patterns ending in a Z is the least")
    print(f"common multiple of the numbers set of cycles and the pattern length: {int(count):,}")