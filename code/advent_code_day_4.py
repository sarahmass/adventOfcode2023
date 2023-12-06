
import os
import sys
import numpy as np
import re

#C:\Users\sarah\OneDrive\Documents\My Tableau Repository\Datasources\adventDay1_input.txt
day = 4



TEST_INPUT = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
              "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
              "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
              "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
              "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
              "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
              ]


def read_input(day, test = False):
    if test:
        return TEST_INPUT
    file_name = os.path.join(os.getcwd(),f"adventDay{day}_input.txt")
    with open(file_name, "r") as f:
        flines = f.readlines()
    return flines

def extract_number_sets(card):
    ''' in -> card: string  "card {int string}: winning ints | card's hopefulls ints
        the set of w are the numbers that need to be matched for a win
        the set of c are the numbers that need to match to the set of w
        
        returns <- w: set; int strings 
                   c: set; int strings
    '''
    _ , nums = card.split(":")
    w , c = nums.split("|")
    w = set([int(i) for i in w.split(' ') if i not in ['', ' ']])
    c = set([int(i) for i in c.split(' ') if i not in ['', ' ']])
    return(w,c)


def num_matches(w,c):
    ''' in -> w: set of winners
              c: set of possible matches
        
        returns <- num: int, size of intersection
    '''
    intrsct = w & c
    return (len(intrsct))


def get_card_value(c):
    ''' in -> string 
        return <- value int of card

        first first match equals 1, every other
        match doubles (multiplies by two)
        if num_matches > 0 val = 1 * 2^(num_matches - 1)
        else val = 0:
    '''
    win, nums = extract_number_sets(card.strip())
    # print(f"wins:{win}, nums: {nums} ")
    num_pairs = num_matches(win,nums)
    print(num_pairs)
    if num_pairs > 0:
        return 1 * pow(2, num_pairs - 1)
    else:
        return 0




if __name__ == "__main__":
    day = 4
    part = "b"
    all_cards = read_input(day)
    winnings = 0
    num_cards = [1]*len(all_cards)
    for i,card in enumerate(all_cards):
        if part == 'a':
            val = get_card_value(card)
            winnings += val
        elif part == 'b':
            win, nums = extract_number_sets(card)
            to_copy = num_matches(win,nums)
            
            # update the number of copies of each card
            # if there are n matches then the next n 
            # cards gets a copy made for each of the
            # current cards' copy.  They all start with one
            # copy.  If no matches then no cards will get 
            # additional coppies.
            for n in range(1,to_copy + 1):
                if i+n < len(all_cards):
                    num_cards[i+n] += num_cards[i]
    if part == 'a':
        print(winnings) 
    else:
        # count total number originals + copies
        print(sum(num_cards))   
        