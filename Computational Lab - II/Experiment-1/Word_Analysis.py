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
This program performs morphological analysis on input words. It utilizes a predefined lexicon 
containing words and their associated grammatical features (root form, category, gender, number, 
person, tense, aspect). 

The primary objective is to demonstrate how individual words can be analyzed to extract their 
underlying morphological structure, which is a fundamental step in Natural Language Processing (NLP)
tasks such as Part-of-Speech (POS) tagging and parsing.

Algorithm:
1. Define a lexicon (database) of words with their corresponding morphological tags.
2. Accept a word as input from the user.
3. Search for the word in the lexicon.
4. If found, retrieve and display its morphological features.
5. If not found, inform the user that the word is not in the lexicon.
============================================================================================
Repositories:
- NLP Lab: https://github.com/Amey-Thakur/NATURAL-LANGUAGE-PROCESSING-AND-COMPUTATIONAL-LAB-II
- Main: https://github.com/Amey-Thakur/COMPUTER-ENGINEERING
- Profile: https://github.com/Amey-Thakur
============================================================================================
"""

# ==========================================
# Lexicon Definition
# ==========================================
# The lexicon is implemented as a list of dictionaries. Each dictionary represents a word entry
# and contains key-value pairs for its morphological attributes.
# Keys:
# - 'word': The surface form of the word (the word as it appears in text).
# - 'rt': The root or lemma of the word.
# - 'cat': The grammatical category (e.g., 'v' for verb, 'n' for noun).
# - 'gen': Gender (e.g., 'male', 'female', '-').
# - 'num': Number (e.g., 'sg' for singular, 'pl' for plural).
# - 'case': Case (e.g., nominative, accusative; often empty for English verbs).
# - 'per': Person (e.g., 'first', 'second', 'third').
# - 'tense': Tense (e.g., 'simple-past', 'present-continuous').
# - 'aspect': Aspect (e.g., progressive, perfect).

wordListE = [
    {
        "word": "trained", 
        "rt": "train", 
        "cat": "v", 
        "gen": "male", 
        "num": "sg", 
        "case": "", 
        "per": "first", 
        "tense": "simple-past", 
        "aspect": ""
    },
    {
        "word": "stood", 
        "rt": "stand", 
        "cat": "v", 
        "gen": "male", 
        "num": "sg", 
        "case": "", 
        "per": "first", 
        "tense": "simple-past", 
        "aspect": ""
    },
    {
        "word": "walking", 
        "rt": "walk", 
        "cat": "v", 
        "gen": "male", 
        "num": "sg", 
        "case": "", 
        "per": "first", 
        "tense": "present-continuous", 
        "aspect": ""
    }
]

# ==========================================
# Function Definition
# ==========================================

def process(word):
    """
    Analyzes the input word and prints its morphological features if found in the lexicon.
    
    This function iterates through the predefined 'wordListE' to find a matching entry.
    If a match is found, it extracts and formats the morphological information for display.
    
    Args:
        word (str): The word to analyze.
    """
    found = False
    
    # Iterate through each entry in the lexicon
    for x in wordListE:
        # Check if the input word matches the 'word' key in the current entry
        if word == x["word"]:
            found = True
            
            # Check the grammatical category to determine which features to print
            if x['cat'] == "v": # Logic for Verbs
                print(f"\n--- Morphological Analysis Result ---")
                print(f"Surface Word : {word}")
                print(f"Root (Lemma) : {x['rt']}")
                print(f"Category     : Verb")
                print(f"Gender       : {x['gen']}")
                print(f"Number       : {x['num']}")
                print(f"Tense        : {x['tense']}")
                print(f"Person       : {x['per']}")
                print(f"Aspect       : {x['aspect'] if x['aspect'] else 'N/A'}")
                
            else: # Logic for Nouns (and other categories if extended)
                print(f"\n--- Morphological Analysis Result ---")
                print(f"Surface Word : {word}")
                print(f"Root (Lemma) : {x['rt']}")
                print(f"Category     : Noun")
                print(f"Gender       : {x['gen']}")
                print(f"Number       : {x['num']}")
            
            # Exit loop once the word is found
            break
    
    # Handle the case where the word is not present in the lexicon
    if not found:
        print(f"\nError: The word '{word}' was not found in the system lexicon.")
        print("Please try words like: 'trained', 'stood', or 'walking'.")

# ==========================================
# Main Execution Block
# ==========================================
if __name__ == "__main__":
    print("=========================================")
    print("      Experiment 1: Word Analysis        ")
    print("=========================================")
    
    # Prompt user for input
    user_word = input("Enter the word to analyze: ").strip() # .strip() removes accidental whitespace
    
    print(f"\nProcessing word: '{user_word}'...")
    
    # Call the processing function
    process(user_word)
    
    print("\n=========================================")
