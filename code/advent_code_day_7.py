import os
import sys
import numpy as np
import re


TEST_INPUT = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483",
    # "23456 123",
    # "QQKKK 777",
    # "AAAAA 1111",
    # "A8234 8",
    # "A2222 333"
    ]

# Used to sort hands of the same type in ascending order
card_values_a = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1
}
card_values_b = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1
}

# used to sort types of hands in ascending order
hand_values = {
    "five_kind": 19,
    "four_kind": 18,
    "full_house": 17,
    "three_kind": 16,
    "two_pair": 15,
    "pair": 14,
    "high_card":13,
    }

def extract_hand_bid(line):
    # example line in put: "32T3K 765"
    hand, bid = line.split(' ')
    return [hand.strip(), int(bid)]


def get_hand_type(count):
    c = sorted(list(count.values()))
    if c[-1] == 5:
        return "five_kind"
    if c[-1] == 4:
        return "four_kind"
    if c[-1] == 3 and c[-2] == 2:
        return "full_house"
    if c[-1] == 3:
        return "three_kind"
    if c[-1] == 2 and c[-2] == 2:
        return "two_pair"
    if c[-1] == 2:
        return "pair"
    else:
        return "high_card"

def sort_hand_types(types):
    sorted_types = sorted(types,key=lambda hand_type: hand_values[hand_type])
    return sorted_types


def sort_hands(hands, part='a'):
    if part == 'a':
        card_values = card_values_a
    elif part == 'b':
        card_values = card_values_b
    sorted_hands = sorted(hands,key=lambda hand: 
        (card_values[hand[0][0]],
         card_values[hand[0][1]],
         card_values[hand[0][2]],
         card_values[hand[0][3]],
         card_values[hand[0][4]]
        ))
    return sorted_hands

def count_cards(hand, part = "a"):
    counts = {}
    any_Js = False
    for c in hand:
        if part == 'b' and c == "J":
            any_Js = True
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    
    # let jokers be equal to the card with highest count 
    if part == 'b' and any_Js and counts["J"] != 5:

        num_Js = counts.pop("J")
        inv_counts = {v:k for k,v in counts.items()}
        max_count = max(inv_counts.keys())
        counts[inv_counts[max_count]] += num_Js

    return counts

def read_input(day, test = False):
    if test:
        return TEST_INPUT
    file_name = os.path.join("my_inputs", f"adventDay{day}_input.txt")
    with open(file_name, "r") as f:
        file_lines = f.readlines()
    return file_lines


if __name__ == "__main__":
    test = False
    day = 7
    part = 'b'
    hands_sorted = {}
    total_winnings = 0
    lines = read_input(day, test)

    for line in lines: 
        line = line.strip()
        if line == "":
            continue      
        
        hand, bid = extract_hand_bid(line)
        
        # count the types of cards in each to get hand type
        count = count_cards(hand, part)
        type_hand = get_hand_type(count)
        
        # add hand into dict sorting hands:
        if type_hand in hands_sorted.keys():
            hands_sorted[type_hand].append([hand,bid])

            # sort the hands with in the same type as defined in game
            hands_sorted[type_hand] = sort_hands(hands_sorted[type_hand], part)
            
        else:
            hands_sorted[type_hand] = [(hand,bid)]
    
    # sort hand types from least to best type
    sorted_hand_types = sort_hand_types(hands_sorted.keys())
    print(sorted_hand_types)
    # hand winnings = score * bid, sum all winnings 
    score = 1
    for hand_type in sorted_hand_types:
        
        for hand,bid in hands_sorted[hand_type]:
            
            total_winnings += bid * score
            score += 1
    print(f"total_winnings: {total_winnings}" )    
        

       