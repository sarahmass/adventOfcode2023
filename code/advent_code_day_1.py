
import os
import sys
import numpy as np
import re


TEST_INPUTa = [
    '1abc2',
    'pqr3stu8vwx',
    'a1b2c3d4e5f',
    'treb7uchet',
    ]

TEST_INPUTb = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"
    ]

def read_input(day, test = False, part = 'a'):
    if test:
        if part == 'a':
            return TEST_INPUTa
        elif part == 'b':
            return TEST_INPUTb
    
    file_name = os.path.join("my_inputs", f"adventDay{day}_input.txt")
    
    with open(file_name, "r") as f:
        flines = f.readlines()
    
    return flines



def words_to_digit(word):
    words2digit = {
        'one': '1',
        'two' : '2',
        'three': '3',
        'four':'4',
        'five': '5',
        'six': '6',
        'seven': '7', 
        'eight': '8', 
        'nine': '9',
        }
    return words2digit[word]


def extract_num(line, part = 'a'):
    # for part a we only need digits
    if part == 'a':
        pattern = "[0-9]"
    
    # for part b we need digits and digits spelled out
    elif part == 'b':
        pattern = "([0-9]|one|two|three|four|five|six|seven|eight|nine)"
    
    line_len = len(line)
    matches = []
    for idx in range(line_len):
        # check for patterns at each character
        is_match = re.match(pattern,line[idx:])
                
        if is_match is not None:
             # if match is found retrieve it  
             matches.append(is_match.group())
    
    first = matches[0]
    last = matches[-1]
    
    if not first.isdigit():
        first = words_to_digit(first) 
    
    if not last.isdigit():
        last = words_to_digit(last)
    
    return int(first + last)
    
    
if __name__ == "__main__":
    test = False
    part = 'a'
    day = 1
    lines = read_input(day, test, part)

    sum_total = 0
    for line in lines:
        num = extract_num(line, part)
        sum_total += num
    
    print(sum_total)