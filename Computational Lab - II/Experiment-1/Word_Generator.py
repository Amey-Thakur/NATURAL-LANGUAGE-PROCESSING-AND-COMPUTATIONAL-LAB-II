"""
============================================================================================
Experiment 1: Word Generation
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
This program performs word generation. It takes morphological features (root, category,
gender, number, person, tense) as input and returns the corresponding word form
from the lexicon. This illustrates morphological generation.
============================================================================================
Repositories:
- NLP Lab: https://github.com/Amey-Thakur/NATURAL-LANGUAGE-PROCESSING-AND-COMPUTATIONAL-LAB-II
- Main: https://github.com/Amey-Thakur/COMPUTER-ENGINEERING
- Profile: https://github.com/Amey-Thakur
============================================================================================
"""

# Feature database for generation
feature = [
    {'root': 'boy', 'cat': 'n', 'gender': '-', 'num': 'sg', 'person': '-', 'tense': '-', 'word': 'boy'},
    {'root': 'boy', 'cat': 'n', 'gender': '-', 'num': 'pl', 'person': '-', 'tense': '-', 'word': 'boys'},
    {'root': 'child', 'cat': 'n', 'gender': '-', 'num': 'pl', 'person': '-', 'tense': '-', 'word': 'children'},
    {'root': 'play', 'cat': 'v', 'gender': 'male', 'num': 'sg', 'person': 'first', 'tense': 'simple-present', 'word': 'play'},
    {'root': 'play', 'cat': 'v', 'gender': 'male', 'num': 'sg', 'person': 'third', 'tense': 'simple-present', 'word': 'plays'},
    {'root': 'walk', 'cat': 'v', 'gender': 'male', 'num': 'sg', 'person': 'first', 'tense': 'present-continuous', 'word': 'walking'}
]

def generate():
    """
    Prompts user for morphological features and returns the matching word from the database.
    
    Returns:
        str: The generated word or specific message if not found.
    """
    print("Enter the following morphological features:")
    root = input('Root word: ')
    cat = input('Category (n/v): ')
    gen = input('Gender (male/female/-): ')
    num = input('Number (sg/pl): ')
    per = input('Person (first/second/third/-): ')
    ten = input('Tense (simple-present/present-continuous/simple-past/-): ')

    for word in feature:
        if (word['root'] == root and
            word['cat'] == cat and
            word['num'] == num and
            word['gender'] == gen and
            word['person'] == per and
            word['tense'] == ten):
            return word['word']
            
    return 'Word not found in the database.'

# Main Execution
if __name__ == "__main__":
    print("--- Word Generation System ---")
    result = generate()
    print('The generated word is:', result)
