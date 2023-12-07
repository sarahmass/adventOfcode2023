
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



def extract_numbers(lines):
    # define pattern to locate single or multi-digit numbers
    num_pattern = "([0-9]+)"

    # pattern to select all non-digit characters
    symb_pattern = "(\D+)"

    number_rows = []
    for row in range(len(lines)):
        # strip newline chars and extra white space   
        cur_row = lines[row].strip()
        
        col = 0
        while col < len(cur_row):
            # check for numbers starting at position 0 in string
            is_number = re.match(num_pattern, cur_row[col::])
            
            if is_number is not None:
                is_adj = False
                
                # take note of start and end position of the number
                start = col
                end = start + is_number.end()

                # update where to start looking for the next number
                col = end
                
                #check for a symbol just before the start of the number
                if start > 0:
                    # Splitting on "." is a simple way of removing them
                    before = "".join(cur_row[start - 1].split('.'))
                    is_adj = re.match(symb_pattern, before) is not None
                    
                # check for symbol at end of number, on same row
                if end < len(cur_row) and not is_adj:
                    after = "".join(cur_row[end].split('.'))
                    is_adj = re.match(symb_pattern, after) 
                                        
                # check in span (start-1) to (end+1) in row above and below
                if start > 0:
                    begin = start -1
                else: 
                    begin = start
                if end < len(cur_row):
                    stop = end + 1
                else:
                    stop = end 
                
                # check in span above
                if row > 0 and not is_adj:
                    row_above = lines[row-1].strip()
                    line_sega = "".join(row_above[begin:stop].split('.'))
                    is_adj = re.search(symb_pattern, line_sega) is not None
                              
                # check in span below
                if row + 1 < len(lines) and not is_adj:
                    row_below = lines[row+1].strip()
                    line_segb = "".join(row_below[begin:stop].split('.'))
                    is_adj = re.search(symb_pattern, line_segb) is not None
                
                if is_adj:
                    number_rows.append(int(is_number.group()))
            else:
                col += 1
    return number_rows
        
if __name__ == "__main__":
    test = True
    day = 2
    lines = read_input(day, test)       
    numbers = extract_numbers(lines)
    print(sum(numbers))    


