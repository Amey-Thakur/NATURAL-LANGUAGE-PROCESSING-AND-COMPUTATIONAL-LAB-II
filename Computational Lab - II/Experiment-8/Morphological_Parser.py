"""
============================================================================================
Experiment 8: Morphological Parsing
============================================================================================
Course: Natural Language Processing (DLO8012)
Lab: Computational Lab II (CSL804)
Experiment No: 8
Roll No: 50
Name: Amey Thakur
Class: BE Comps B
Batch: B3
Date: April 01, 2022

Aim:
Implement morphological parser to accept and reject given string.

Description:
This program implements a basic morphological parser that accepts or rejects a word based 
on whether it can be decomposed into a stem (root) and affixes.

Logic:
1. Input: A single word (e.g., "programming").
2. Operations:
   - Stemming: Uses NLTK's PorterStemmer to reduce the word to its root form.
     Example: "programming" -> "program"
   - Acceptance Criteria:
     - If the stemmed word != original word, it implies the word has affixes (e.g., "-ing").
       In this context, the parser "Accepts" the string as morphologically parsed.
     - If the stemmed word == original word, it implies it is already a root or unparsable 
       by this stemmer logic. The parser "Rejects" it (or considers it a root).
3. POS Tagging: Uses Spacy to provide the Part-of-Speech tag and description for the word,
   adding context to the morphological analysis.

Dependencies:
- spacy: For POS tagging. (Requires 'en_core_web_sm' model)
- nltk: For stemming.
============================================================================================
Repositories:
- NLP Lab: https://github.com/Amey-Thakur/NATURAL-LANGUAGE-PROCESSING-AND-COMPUTATIONAL-LAB-II
- Main: https://github.com/Amey-Thakur/COMPUTER-ENGINEERING
- Profile: https://github.com/Amey-Thakur
============================================================================================
"""

import spacy
from nltk.stem import PorterStemmer

# Load Spacy English model
# Ensure you have run: python -m spacy download en_core_web_sm
try:
    sp = spacy.load('en_core_web_sm')
except OSError:
    print("Error: Spacy model 'en_core_web_sm' not found. Please run: python -m spacy download en_core_web_sm")
    exit()

def morphological_parser(word_list):
    """
    Parses words to check if they contain morphological components (affixes).
    """
    ps = PorterStemmer()
    
    print("-" * 50)
    print(f"{'Original':<15} | {'Stemmed':<15} | {'Status'}")
    print("-" * 50)

    for word in word_list:
        stemmed_word = ps.stem(word)
        status = "Accepted"
        
        # If the stem is different, it means morphology was parsed (affixes removed)
        # Logic: If Stem != Word, then Word = Stem + Affix -> Accepted
        # Logic: If Stem == Word, then Word is Root -> Rejected (for parsing/decomposition)
        if stemmed_word == word:
             status = "Reject" 
        
        print(f"{word:<15} | {stemmed_word:<15} | {status}")
        
        if status == "Accepted":
             print(f"  -> Successfully parsed '{word}' into stem '{stemmed_word}'.")
        else:
             print(f"  -> '{word}' is already a root form or unparsable.")

    print("-" * 50)
    print("\n")

def pos_tagging_analysis(word_list):
    """
    Performs POS tagging on the words using Spacy.
    """
    print("-" * 65)
    print("POS Tagging Analysis")
    print("-" * 65)
    print(f"{'Word':<15} | {'POS':<10} | {'Description'}")
    print("-" * 65)

    for word_text in word_list:
        # Process the word (string) with Spacy
        doc = sp(str(word_text))
        for token in doc:
             print(f"{token.text:<15} | {token.pos_:<10} | {spacy.explain(token.tag_)}")
    
    print("-" * 65)

# ==========================================
# Main Execution
# ==========================================
if __name__ == '__main__':
    print("=========================================")
    print("      Experiment 8: Morphological Parser ")
    print("=========================================")

    # Test Input
    input_words = ["programming"]
    
    print(f"Input Word(s): {input_words}\n")

    # 1. Run Morphological Parser
    morphological_parser(input_words)

    # 2. Run POS Analysis
    pos_tagging_analysis(input_words)

    print("=========================================")
