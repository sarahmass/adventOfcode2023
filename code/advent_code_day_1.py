
import os
import sys
import numpy as np
import re

#C:\Users\sarah\OneDrive\Documents\My Tableau Repository\Datasources\adventDay1_input.txt
file_name = os.path.join(os.getcwd(),"adventDay1_input.txt")
with open(file_name, "r") as f:
    linesf = f.readlines()
sum_total = 0
count = 0
# numbers can come as digits or names, so patter needs to include all number posibilities
pattern =  "([0-9]|one|two|three|four|five|six|seven|eight|nine)"

# I wanted to change the number-words into digit strings
words2digit = {'one': '1',
                   'two' : '2',
                   'three': '3',
                   'four':'4', 
                   'five': '5', 
                   'six': '6', 
                   'seven': '7', 
                   'eight': '8', 
                   'nine': '9',
                   }
for line in linesf:
    count +=1
    line_len = len(line)-1
    print(f"line {count}: {line.strip()}")
    #x = re.findall(pattern, line)
    matches = []
    for idx in range(line_len):
        # check for patterns at each character
        # instead of using #x = re.findall(pattern, line)
        # because this missed the overlappint word numbers.
        # also is_match is None if no match was found
        is_match = re.match(pattern,line[idx:])
        # we could use the is_match.end to skip past some idx
        # values, but this use case did not check for performance
        
        if is_match is not None:
             #print(is_match.group())
             # To get the string object must get is_match.group()
             matches.append(is_match.group())
    
    first = matches[0]
    # by selecting the last value by choosing the first value from
    # the right in the string we are able to deal with the case when
    # there is only one match which ends up being both the first and the last value
    last = matches[-1]
    if not first.isdigit():
        first = words2digit[first] 
    
    if not last.isdigit():
        last = words2digit[last]
    
#corner cases: one number: first and last the same, 
#              one word number: first and last the same,
#              any number ending in a letter that another letter starts with could
#              cause overlapping word_numbers which will not be found in re.findall()
        
    # print(f"first: {matches[0]} = {first}")
    # print(f"last: {matches[-1]} = {last}")
    num = int(first + last)
    # print(f"line {count} value: {num}")
    sum_total += num
    # print(f"sum_total: {sum_total}")
    
print(sum_total)  
    





