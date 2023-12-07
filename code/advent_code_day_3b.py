
import os
import sys
import numpy as np
import re


day = 3
TEST_INPUT = [
    "467..114..\n",
    "...*......",
    "..35..633.\n",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*...*",
    ".664.598.."]

def read_input(day, test = False):
    if test:
        return TEST_INPUT
    
    file_name = os.path.join("my_inputs", f"adventDay{day}_input.txt")
    
    with open(file_name, "r") as f:
        flines = f.readlines()
    
    return flines



def extract_sum_of_ratios(lines):
    # define pattern to locate single or multi-digit numbers
    num_pattern = "([0-9]+)"
    
    # define gear pattern
    gear_pattern = "([*])"

    sum_gear_ratios = 0
    for row in range(len(lines)):
        # locate gears on current row
        cur_row = lines[row].strip()
        gear_match = re.finditer(gear_pattern, cur_row)
        for gear in gear_match:
            
            left = gear.start() - 1
            mid = gear.start()
            right = gear.end()
            adj_numbers = []
            
            # collect numbers adjacent to the gear on the row above
            if row > 0:
                row_above = lines[row-1].strip()
                numbers_above = re.finditer(num_pattern,row_above)
                for num_match in numbers_above:
                    if num_match.start() <= right and num_match.end() >= mid:
                        adj_numbers.append(int(num_match.group()))

            # collect adjacent numbers on the same row; ending right before 
            # or starting right after the gear
            numbers_cur_row = re.finditer(num_pattern,cur_row)
            for num_match in numbers_cur_row:
                    if num_match.end() == mid or num_match.start() == right:
                        adj_numbers.append(int(num_match.group()))
            
            # collect adjacent numbers on the row below
            if row < len(lines):
                row_below = lines[row+1].strip()
                numbers_below = re.finditer(num_pattern,row_below)
                for num_match in numbers_below:
                    if num_match.start() <= right and num_match.end() >= mid:
                        adj_numbers.append(int(num_match.group()))
                        
            # only want gears with exactly two adjacent numbers
            if len(adj_numbers) == 2:
                sum_gear_ratios += (adj_numbers[0]*adj_numbers[1])
    return sum_gear_ratios           



if __name__ == "__main__":
    test = False
    day = 3
    lines = read_input(day, test)
    sum_total = extract_sum_of_ratios(lines)
    print(sum_total) 