
import os
import sys
import numpy as np
import re

#C:\Users\sarah\OneDrive\Documents\My Tableau Repository\Datasources\adventDay1_input.txt
day = 3



# linef = ["467..114..\n",
#          "...*......",
#          "..35..633.\n",
#          "......#...",
#          "617*......",
#          ".....+.58.",
#          "..592.....",
#          "......755.",
#          "...$.*...*",
#          ".664.598.."]

file_name = os.path.join(os.getcwd(),f"adventDay{day}_input.txt")
with open(file_name, "r") as f:
    linef = f.readlines()



# I wanted to change the number-words into digit strings
num_pattern = "([0-9]+)"
symb_pattern = "(\D+)"
number_rows = []
sum_total = 0
for row in range(len(linef)):
    # if row >6:
    #     break
    print(linef[row])
    cur_row = linef[row].strip()
    col = 0
    count_numbers_r = []
    while col < len(cur_row):
        #print(f"col num: {col}")
        #print(f"length of row: {len(linef[row])}")
        # check for numbers
        is_number = re.match(num_pattern, cur_row[col::])
        
        if is_number is not None:
            is_adj = False
            print(f"is_num {is_number.group()}")
            start = col
            end = start + is_number.end()
            col = end
            print(f"start: {start}, end: {end}")
            #check for symbol before on same row:
            
            if start > 0:
                before = "".join(cur_row[start - 1].split('.'))
                if len(before)>0:
                    print(f"before: {cur_row[start - 1]}")
                is_adj = re.match(symb_pattern, before) is not None
                #sum_total += int(is_number.group())
                #print(is_number.group(), sum_total)
                #continue
            # check for symbol after, on same row
            if end < len(cur_row) and not is_adj:
                after = "".join(cur_row[end].split('.'))
                if len(after)>0:
                    print(f"after: {cur_row[end]}")
                is_adj = re.match(symb_pattern, after) 
                # sum_total += int(is_number.group())
                # print(is_number.group(), sum_total)
                
            # check in span start -1 to end+1 in row above
            if start > 0:
                begin = start -1
            else: 
                begin = start
            if end < len(cur_row):
                stop = end + 1
            else:
                stop = end 
            # check in span start -1 to end+1 in row above
            if row > 0 and not is_adj:
                last_row = linef[row-1].strip()
                # print(last_row)
                line_sega = "".join(last_row[begin:stop].split('.'))
                print(f"line_seg above: {line_sega}")
                is_above = re.search(symb_pattern, line_sega)
                if is_above is not None:
                    print(is_above) 
                    print(cur_row)
                    is_adj = True
                    # sum_total += int(is_number.group())
                    # print(is_number.group(), sum_total)
                    
            # check in span start -1 to end+1 in row below
            if row + 1 < len(linef) and not is_adj:
                next_row = linef[row+1].strip()
                print(cur_row)
                print(next_row)
                line_segb = "".join(next_row[begin:stop].split('.'))
                print(f"line_seg below: {line_segb}")
                is_below = re.search(symb_pattern, line_segb)
                if is_below is not None:
                    print(is_below) 
                    is_adj = True
                    # sum_total += int(is_number.group())
                    # print(is_number.group(), sum_total)
            if is_adj:
                sum_total += int(is_number.group())
                print(is_number.group(), sum_total)
                count_numbers_r.append(is_number.group())

        # increment row and look for more numbers
        else:
            col += 1
    number_rows.append(count_numbers_r)
        
        
        

        
        
    
print(sum_total)

with open("output.txt", "w+") as f:
    for row in number_rows:
        f.write(" ".join(row))
        f.write('\n')


