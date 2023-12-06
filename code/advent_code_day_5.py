import os
import sys
import numpy as np
import re
from math import inf

#C:\Users\sarah\OneDrive\Documents\My Tableau Repository\Datasources\adventDay5_input.txt
day = 5



TEST_INPUT = ['seeds: 79 14 55 13',
              'seed-to-soil map:',
              '50 98 2',
              '52 50 48',
              'soil-to-fertilizer map:',
              '0 15 37',
              '37 52 2',
              '39 0 15',
              'fertilizer-to-water map:',
              '49 53 8',
              '0 11 42',
              '42 0 7',
              '57 7 4',
              'water-to-light map:',
              '88 18 7',
              '18 25 70',
              'light-to-temperature map:',
              '45 77 23',
              '81 45 19',
              '68 64 13',
              'temperature-to-humidity map:',
              '0 69 1',
              '1 0 69',
              'humidity-to-location map:',
              '60 56 37',
              '56 93 4'
              ]


def read_input(day, test = False):
    if test:
        return TEST_INPUT
    file_name = os.path.join(os.getcwd(),f"adventDay{day}_input.txt")
    with open(file_name, "r") as f:
        flines = f.readlines()
    return flines

def map_to_int(s):
    return list(map(lambda i: int(i),s.strip().split(" ")))

def clean_input(dataf, part = 'a'):
    # first line: 'seeds: int, int, ...'
    init_line = dataf.pop(0).strip()
    seeds = init_line.split("seeds:")[1].strip()
    seeds = map_to_int(seeds)
        
    # next line: "source-to-dest map:"
    conv_table = {}
    line_no = 0
    while line_no < (len(dataf)):

        # empty lines show up between conversion tables
        if dataf[line_no].strip() == '':
            line_no += 1
            continue
        # get source and destination names
        elif dataf[line_no][0].isalpha():
            cur_line = dataf[line_no].split("-to-")
            dest = cur_line[1].split(" ")[0]
            
            source = cur_line[0].strip()
            line_no += 1
            conv_table[(source,dest)] = []
            
            # converstion maps come in dest_v int, source_v int, range_value
            while line_no < len(dataf) and dataf[line_no].strip() != '' and dataf[line_no].strip()[0].isdigit():
                # extract source, dest, and range values
                dest_v, source_v, range_v = map_to_int(dataf[line_no])
                # print(dest_v, source_v, range_v)
                # (avoid brain pretzle by) reorder values to be source,dest, range_v
                conv_table[(source,dest)].append((source_v, dest_v, range_v))
                line_no += 1 
    print("done cleaning")  
    return (seeds, conv_table) 

def get_location(seed_v):
    source = 'seed'
    source_v = seed_v
    
    # Travel from source to destination and break once source is destination
    while True:
        for s,d in conv_table.keys():
            if s == source:
                # traverse through source start, dest start, and range values for source to dest conversion table
                for ss,ds,r in conv_table[s,d]:
                    # if source value in the interval [source_start, source_start+range)
                    # then calculate linear shift using the diff between dest_start and source_start
                    if source_v in range(ss,ss+r):
                        source_v = source_v + (ds - ss)

                        # now set destination to source to move to the next conv table 
                        # and break inner loop
                        source = d
                        break
                # if source_v not in above ranges then dest_v = source_v
                source = d
                
            # print(source,source_v)
            if source == 'location':
                return source_v

if __name__ == '__main__':
    test = False
    part = "b"
    
    data = read_input(day = 5, test=test)
    seeds, conv_table = clean_input(data, part = part)
    locations = []
    if part == 'b':
        min_location = inf
        count = 0
        for seed_start, range_v in zip(seeds[0:len(seeds):2],seeds[1:len(seeds):2]):
            print(f"interval num: {count}")
            if 4088757830 >= seed_start >= 3964756945:
                
                start = seed_start
                end = min(seed_start +range_v-1, 4088757830) 
                for seed in range(start, end):
                    loc = get_location(seed)
                    locations.append(loc)
                    if seed%1000000 == 0:
                        print(f"seednum,loc: {seed:,}   {loc:,}")
                print(min(locations))
            count +=1
    else:
        
        for seed in seeds:
            locations.append(get_location(seed))
            min_location = min(locations)
    
