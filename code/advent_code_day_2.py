
import os
import sys
import numpy as np
import re

#C:\Users\sarah\OneDrive\Documents\My Tableau Repository\Datasources\adventDay1_input.txt
day = 2
# possible = "12 red cubes, 13 green cubes, and 14 blue cubes"




file_name = os.path.join(os.getcwd(),f"adventDay{day}_input.txt")
with open(file_name, "r") as f:
    linesf = f.readlines()
sum_total = 0
count = 0
# numbers can come as digits or names, so patter needs to include all number posibilities
pattern =  "([0-9]|one|two|three|four|five|six|seven|eight|nine)"

# I wanted to change the number-words into digit strings
max_colors = {'red':12, 'green': 13, 'blue': 14}
for line in linesf:
    print(line)
    count_game = True
    game, counts = line.split(': ')
    print(count)
    game = game.split(' ')[1]
    print(f"game: {game}")
    counts = counts.split("; ")
    for draw in counts:
        draw.strip()
        print(f"draw before split {draw}")
        draw = draw.split(" ")
        print(draw)
        len_draw = len(draw)
        for i in range(0, len_draw,2):
            #remove comma:
            count = draw[i]
            color = draw[i+1]
            if color[-1] == ',' or color[-1] == '\n':
                color = color[0:len(color)-1] 
            
            print(count, color)
            if int(count) > max_colors[color]:
                count_game = False
                break
        
        if not count_game:
            break
    print(count_game)
    if count_game:
        sum_total += int(game)
        print(sum_total)
    if int(game)==100:
        break
print(sum_total)



