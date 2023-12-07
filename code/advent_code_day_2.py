
import os
import sys
import numpy as np
import re


day = 2

TEST_INPUT = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]



def read_input(day, test = False):
    if test:
        return TEST_INPUT
    
    file_name = os.path.join("my_inputs", f"adventDay{day}_input.txt")
    
    with open(file_name, "r") as f:
        flines = f.readlines()
    
    return flines


def check_game_counts(game):
    # example game: "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    #                game id = 1
    #                Three draws were made and the results are separated by ";"
    
    # extract game id and counts of cubes and colors
    game, counts = game.split(': ')
    
    # split on game result above on space to isolate id num
    game_id = int(game.split(' ')[1])
    
    # split counts on ";" to separate out each draw of cubes
    counts = counts.split("; ")
    
    for draw in counts:
        draw = draw.strip()
        draw = draw.split(", ")
        for cubes in draw:
            cubes = cubes.strip()
            count, color = cubes.split(" ")
            if not is_game_possible(int(count), color):
                return [0, False]
    return [game_id, True]


def is_game_possible(count, color):
    max_colors = {'red':12, 'green': 13, 'blue': 14}
    return max_colors[color] >= count
    
    
if __name__ == "__main__":
    test = False
    day = 2
    games = read_input(day, test)

    sum_total = 0
    for game in games:
        if game.strip() == '':
            continue
        game_id, possible = check_game_counts(game)
        if possible:
            sum_total += game_id
    print(sum_total)



