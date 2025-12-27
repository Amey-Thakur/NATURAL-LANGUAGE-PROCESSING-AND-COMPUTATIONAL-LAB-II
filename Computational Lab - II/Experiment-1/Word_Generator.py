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
This program demonstrates the process of morphological generation. Unlike analysis, which extracts
features from a word, generation constructs the specific word form (surface form) based on a 
set of provided morphological constraints (root, category, gender, number, person, tense).

This simulates how a Natural Language Generation (NLG) system might select the correct word form
to construct a grammatically correct sentence.

Algorithm:
1. Define a feature database (lexicon) mapping sets of morphological features to their corresponding word forms.
2. Prompt the user to input specific morphological features (Root, Category, Gender, Number, Person, Tense).
3. Search the database for an entry that exactly matches ALL the provided features.
4. If a match is found, return and display the corresponding word form.
5. If no match is found, inform the user.
============================================================================================
Repositories:
- NLP Lab: https://github.com/Amey-Thakur/NATURAL-LANGUAGE-PROCESSING-AND-COMPUTATIONAL-LAB-II
- Main: https://github.com/Amey-Thakur/COMPUTER-ENGINEERING
- Profile: https://github.com/Amey-Thakur
============================================================================================
"""

# ==========================================
# Feature Database (Lexicon)
# ==========================================
# This list simulates a database where each entry maps a unique combination of 
# morphological features to a specific surface word.
# 
# Structure:
# - 'root': The base form of the word.
# - 'cat': Grammatical category ('n' for noun, 'v' for verb).
# - 'gender': Grammatical gender.
# - 'num': Grammatical number ('sg' for singular, 'pl' for plural).
# - 'person': Grammatical person ('first', 'second', 'third').
# - 'tense': Grammatical tense (e.g., 'simple-present').
# - 'word': The resulting word form corresponding to these features.

feature = [
    {'root': 'boy', 'cat': 'n', 'gender': '-', 'num': 'sg', 'person': '-', 'tense': '-', 'word': 'boy'},
    {'root': 'boy', 'cat': 'n', 'gender': '-', 'num': 'pl', 'person': '-', 'tense': '-', 'word': 'boys'},
    {'root': 'child', 'cat': 'n', 'gender': '-', 'num': 'pl', 'person': '-', 'tense': '-', 'word': 'children'},
    {'root': 'play', 'cat': 'v', 'gender': 'male', 'num': 'sg', 'person': 'first', 'tense': 'simple-present', 'word': 'play'},
    {'root': 'play', 'cat': 'v', 'gender': 'male', 'num': 'sg', 'person': 'third', 'tense': 'simple-present', 'word': 'plays'},
    {'root': 'walk', 'cat': 'v', 'gender': 'male', 'num': 'sg', 'person': 'first', 'tense': 'present-continuous', 'word': 'walking'}
]

# ==========================================
# Function Definition
# ==========================================

def generate():
    """
    Prompts the user for morphological attributes and attempts to generate the corresponding word.
    
    Returns:
        str: The generated word form if successful, or a 'not found' message.
    """
    print("Please enter the following morphological features to generate a word:")
    
    # Collect inputs from the user
    # Note: Inputs are case-sensitive based on the database content
    root = input('Root word (e.g., boy, play, walk): ').strip()
    cat = input('Category (n for noun, v for verb): ').strip()
    gen = input('Gender (male, female, or -): ').strip()
    num = input('Number (sg for singular, pl for plural): ').strip()
    per = input('Person (first, second, third, or -): ').strip()
    ten = input('Tense (simple-present, present-continuous, simple-past, or -): ').strip()

    print("\nSearching database for match...")

    # Iterate through the feature database to find an exact match
    for word in feature:
        if (word['root'] == root and
            word['cat'] == cat and
            word['num'] == num and
            word['gender'] == gen and
            word['person'] == per and
            word['tense'] == ten):
            
            # Match found: return the surface form
            return word['word']
            
    # No match found after checking all entries
    return 'Transformation rule not found in database.'

# ==========================================
# Main Execution Block
# ==========================================
if __name__ == "__main__":
    print("=========================================")
    print("     Experiment 1: Word Generation       ")
    print("=========================================")
    
    # Call the generation logic
    result = generate()
    
    print("=========================================")
    print(f"Generated Result: {result}")
    print("=========================================")
