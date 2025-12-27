"""
============================================================================================
Experiment 1: Word Analysis
============================================================================================
Course: Natural Language Processing (DLO8012)
Lab: Computational Lab II (CSL804)
Experiment No: 1
Roll No: 50
Name: Amey Thakur
Class: BE Comps B
Batch: B3
Date: January 19, 2022

Description:
This program demonstrates word analysis by identifying the root, category, and grammatical
features (gender, number, case, person, tense, aspect) of a given word from a predefined
lexicon. It helps in understanding morphological analysis.
============================================================================================
Repositories:
- NLP Lab: https://github.com/Amey-Thakur/NATURAL-LANGUAGE-PROCESSING-AND-COMPUTATIONAL-LAB-II
- Main: https://github.com/Amey-Thakur/COMPUTER-ENGINEERING
- Profile: https://github.com/Amey-Thakur
============================================================================================
"""

# Predefined lexicon with grammatical features
wordListE = [
    {"word": "trained", "rt": "train", "cat": "v", "gen": "male", "num": "sg", "case": "", "per": "first", "tense": "simple-past", "aspect": ""},
    {"word": "stood", "rt": "stand", "cat": "v", "gen": "male", "num": "sg", "case": "", "per": "first", "tense": "simple-past", "aspect": ""},
    {"word": "walking", "rt": "walk", "cat": "v", "gen": "male", "num": "sg", "case": "", "per": "first", "tense": "present-continuous", "aspect": ""}
]

def process(word):
    """
    Analyzes the input word and prints its morphological features if found in the lexicon.
    
    Args:
        word (str): The word to analyze.
    """
    found = False
    for x in wordListE:
        if word == x["word"]:
            found = True
            if x['cat'] == "v":
                print(f"Root of word is : {x['rt']}, category is verb, gender is {x['gen']}, "
                      f"number is {x['num']}, tense is {x['tense']}, person is {x['per']}, "
                      f"aspect is: {x['aspect']}")
            else:
                print(f"Root of word is : {x['rt']}, category is noun, gender is {x['gen']}, "
                      f"number is {x['num']}")
            break
    
    if not found:
        print("Word not found in the lexicon.")

# Main Execution
if __name__ == "__main__":
    print("--- Word Analysis System ---")
    user_word = input("Enter the word: ")
    print("Your word is:", user_word)
    process(user_word)
