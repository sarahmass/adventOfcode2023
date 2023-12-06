import os
import sys
import numpy as np
import re
import math

#C:\Users\sarah\OneDrive\Documents\My Tableau Repository\Datasources\adventDay6_input.txt
day = 6



TEST_INPUT = ['Time:      7  15   30',
              'Distance:  9  40  200'
              ]

def read_input(day, test = False):
    if test:
        return TEST_INPUT
    file_name = os.path.join(os.getcwd(),f"adventDay{day}_input.txt")
    with open(file_name, "r") as f:
        flines = f.readlines()
    return flines

def map_to_int(s):
    return list(map(lambda i: int(i),s))

def clean_input(dataf, part = 'a'):
    
    for line in dataf:
        if "Time" in line:
            max_times = re.findall("[0-9]+",line)
            if part == 'a':
                max_times = map_to_int(max_times)
            elif part == 'b':
                max_times = [int(''.join(max_times))]
                    
        elif "Distance" in line:
            rec_dists = re.findall("[0-9]+",line)
            if part == 'a':
                rec_dists = map_to_int(rec_dists)
            elif part == 'b':
                rec_dists = [int(''.join(rec_dists))]
    return (max_times, rec_dists)


def extract_margin(tmax,dmax):
    # solve quadratic: f(t) = (tmax-t)t > dmax
    # use quad formula to calculate t1, t2
    
    a = -1
    b = tmax
    c = -dmax
    t1 = (-b - math.sqrt(b**2 - (4*a*c)))/(2*a)
    t2 = (-b + math.sqrt(b**2 - (4*a*c)))/(2*a)
    
    # f(t1) = f(t2) = dmax  may or may not be integers
    # by taking the floor of the larger of the two will 
    # move up the back side of the parabola making the distance
    # larger, the ceiling will move up the front side of the parabola
    # (moving from left to right). this way we get the correct
    # rounded integers
    t1, t2 = math.ceil(min(t1,t2)), math.floor(max(t1,t2))
    
    # if t1 and/or t2 are integers already then they will
    # be unchanged and f(t) will equal dmax, but we want
    # to beat tmax so we need to move towards the vertex
    # of the parabola.  up for t1 and down for t2
    if (tmax - t1)*t1 == dmax:
        t1 += 1
    if (tmax - t2)*t2 == dmax:
        t2 -= 1
    # number of int values on [t1,t2]
    # note the hard brackets are inclusive so we add one
       
    return (t2 - t1) + 1
        



if __name__ == '__main__':
    test = False
    part = "b"
    
    data = read_input(day = 6, test=test)
    max_times, max_dists = clean_input(data, part = part)
    print(max_times,max_dists)
    ways = 1
    for tmax, dmax in zip(max_times, max_dists):
        marg = extract_margin(tmax, dmax)
        ways *= marg
    print(ways)
    