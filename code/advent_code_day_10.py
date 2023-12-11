import os
import sys
import numpy as np
import re


TEST_INPUTA = [
    "...........",
    ".S-------7.",
    ".|F-----7|.",
    ".||.....||.",
    ".||.....||.",
    ".|L-7.F-J|.",
    ".|..|.|..|.",
    ".L--J.L--J.",
    "...........",
    ]
TEST_INPUTB = [
    "..F7.",
    ".FJ|.",
    "SJ.L7",
    "|F--J",
    "LJ...",
]
TEST_INPUTC = [
"FF7FSF7F7F7F7F7F---7",
"L|LJ||||||||||||F--J",
"FL-7LJLJ||||||LJL-77",
"F--JF--7||LJLJ7F7FJ-",
"L---JF-JLJ.||-FJLJJ7",
"|F|F-JF---7F7-L7L|7|",
"|FFJF7L7F-JF7|JL---7",
"7-L-JL7||F7|L7F-7F7|",
"L.L7LFJ|||||FJL7||LJ",
"L7JLJL-JLJLJL--JLJ.L",
]
def read_input(day, test = False):
    if test:
        return TEST_INPUTC
    file_name = os.path.join("my_inputs", f"adventDay{day}_input.txt")
    with open(file_name, "r") as f:
        file_lines = f.readlines()
    return file_lines

def get_index_change(dir):
    if dir == "up":
        return [-1, 0]
    if dir == "down":
        return [1, 0]
    if dir == "left":
        return [0, -1]
    if dir == 'right':
        return [0, 1]


next_move = {
    ("left","L"): "up",
    ("left","F"): "down",
    ("left", "-"): "left",
    ("right", "J"): "up",
    ("right", "7"): "down",
    ("right", "-"): "right",
    ("down", "|"): "down",
    ("down", "L"): "right",
    ("down", "J"): "left",
    ("up", "|"): "up",
    ("up","F"): "right",
    ("up","7"): "left",
    ("left", "S"): "Done",
    ("right", "S"): "Done",
    ("down", "S"): "Done",
    ("up", "S"): "Done",

}

def found_s(i,r):
    try:
        return [i, r.index("S")]
    except ValueError:
        return None 


def get_direction(came_from, shape):
    return next_move[came_from, shape]

def extract_start_map(data):
    map_array = []
    for i, line in enumerate(data):
        if line.strip() == '':
            continue
        found_S = False
        row = list(line.strip())
        print(row)
        if not found_S and found_s(i,row) is not None:
            start = found_s(i,row)
        map_array.append(row)
    return start, map_array  

def get_first_move(cur_pos, m): 
        for move in ["left", "right", "down", "up"]:
            v, h = get_index_change(move)
            pos_next_pos = [cur_pos[0] + v, cur_pos[1] + h]
            pos_next_pipe = m[cur_pos[0] + v] [cur_pos[1] + h]
            if (move, pos_next_pipe) in next_move.keys():
                #print(move,pos_next_pos,pos_next_pipe)
                next_dir = next_move[(move,pos_next_pipe)]
                return [pos_next_pipe, pos_next_pos, next_dir, move] 

def get_next_move(cur_pos, move, m):
        
        v, h = get_index_change(move)
        next_pos = [cur_pos[0] + v, cur_pos[1] + h]
        next_pipe = m[cur_pos[0] + v] [cur_pos[1] + h]
        next_dir = next_move[move, next_pipe]
        #print(next_dir, next_pipe)
        return [next_pos, next_dir] 


if __name__ == '__main__':
    day = 10
    test = False
    data = read_input(day=day, test=test)
    
    
    start_pos, map_array = extract_start_map(data)
    
    #print(f"start: {start_pos}")
    shape, pos, move, last_move = get_first_move(start_pos, map_array)
    all_pos = [start_pos]
    print(f"first move dir: {last_move}")
    print(f"second move dir: {move}")
    pos_col_to_row = {start_pos[1]:[[pos[0], last_move]]}
    all_moves = [last_move]
    all_moves.append(move)
    all_pos.append(pos)
    if pos[1] is pos_col_to_row.keys():
        pos_col_to_row[pos[1]].append([pos[0],move])
    else:
        pos_col_to_row[pos[1]] = [[pos[0],move]]
    count = 1
    while move != "Done":
        pos, move = get_next_move(pos, move, map_array)
        #print(pos)
        all_pos.append(pos)
        if pos[1] in pos_col_to_row.keys():
            pos_col_to_row[pos[1]].append([pos[0], move])
            pos_col_to_row[pos[1]] = sorted(pos_col_to_row[pos[1]])
        else:
            pos_col_to_row[pos[1]] = [[pos[0],move]]
        
        
        all_moves.append(move)
        count += 1
    print(f"Furthest point along pip trail of length {count} is {count//2} steps away")

    print(all_moves[0], all_moves[-2])
    clean_array = []
    for i in range(len(map_array)):
        row = []
        for j in range(len(map_array[0])):
            row.append("0")
        clean_array.append(row)

    for p,m in zip(all_pos,all_moves):
        if m == "right":
            clean_array[p[0]][p[1]] = "^"
        elif m == "down":
            clean_array[p[0]][p[1]] = ">"
        elif m == "left":
            clean_array[p[0]][p[1]] = "V"
        elif m == "up":
            clean_array[p[0]][p[1]] = "<"
    for i in range(len(clean_array)):
        for j in range(len(clean_array[0])):
            if clean_array[i][j] == "0":
                if (i == 0 or j == 0 or i == len(clean_array)-1 or j == len(clean_array[0])-1 ) :
                    clean_array[i][j] = "X"
                if clean_array[i-1][j] == "^" or clean_array[i-1][j] == "X":
                    clean_array[i][j]="X"
                if i!= len(clean_array)-1 and (clean_array[i+1][j] == "V" or clean_array[i+1][j] == "X"):
                    clean_array[i][j]="X"
                if j!= len(clean_array[0])-1 and (clean_array[i][j+1] == ">" or clean_array[i][j+1] == "X"):
                    clean_array[i][j]="X"
                if clean_array[i][j-1] == "<" or clean_array[i][j-1]=="X":
                    clean_array[i][j] = "X"
    for row in clean_array:
        print(row)

    count = 0
    for i in range(len(clean_array)):
        for j in range(len(clean_array[0])):
            if clean_array[i][j] == '0':
                count += 1           
           
    print(f"There are {count} internal points of the path found in part a.")
    

