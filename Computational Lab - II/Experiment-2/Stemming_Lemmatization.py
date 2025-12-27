"""
============================================================================================
Experiment 2: Stemming and Lemmatization
============================================================================================
Course: Natural Language Processing (DLO8012)
Lab: Computational Lab II (CSL804)
Experiment No: 2
Roll No: 50
Name: Amey Thakur
Class: BE Comps B
Batch: B3
Date: January 31, 2022

Aim:
Implement stemming and lemmatization operations for a corpus.

Description:
This program demonstrates two fundamental text normalization techniques in NLP:

1. Stemming:
   Stemming is a crude heuristic process that chops off the ends of words in the hope of 
   achieving this goal correctly most of the time, and often includes the removal of derivational 
   affixes. For example, 'walking' becomes 'walk'. We use the Porter Stemmer algorithm here.

2. Lemmatization:
   Lemmatization usually refers to doing things properly with the use of a vocabulary and 
   morphological analysis of words, normally aiming to remove inflectional endings only and 
   to return the base or dictionary form of a word, known as the lemma.
   For example, 'studies' becomes 'study' (whereas a stemmer might output 'studi').
   We use the WordNet Lemmatizer here.

Algorithm:
1. Import necessary NLTK modules (PorterStemmer, WordNetLemmatizer, tokenizers).
2. Download required NLTK data resources (punkt, wordnet, omw-1.4).
3. Demonstrate Stemming:
   a. Initialize PorterStemmer.
   b. Input a list of words or a sentence.
   c. Tokenize the sentence into individual words.
   d. Apply stemming to each token causing a reduction to its root form.
4. Demonstrate Lemmatization:
   a. Initialize WordNetLemmatizer.
   b. Input a sentence.
   c. Tokenize the sentence.
   d. Apply lemmatization to each token to find its dictionary lemma.
============================================================================================
Repositories:
- NLP Lab: https://github.com/Amey-Thakur/NATURAL-LANGUAGE-PROCESSING-AND-COMPUTATIONAL-LAB-II
- Main: https://github.com/Amey-Thakur/COMPUTER-ENGINEERING
- Profile: https://github.com/Amey-Thakur
============================================================================================
"""

# ==========================================
# Library Imports and Setup
# ==========================================
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize

# Downloading necessary NLTK data packages
# 'punkt': Pre-trained tokenizer models.
# 'wordnet': Lexical database for lemmatization.
# 'omw-1.4': Open Multilingual Wordnet (support data).
print("--- Downloading NLTK Resources ---")
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)
print("Resources downloaded successfully.\n")

# ==========================================
# Function: Demonstrate Stemming
# ==========================================
def demonstrate_stemming():
    """
    Executes various stemming examples using the Porter Stemming algorithm.
    """
    print("=========================================")
    print("           Part 1: Stemming              ")
    print("=========================================")
    
    # Initialize the Porter Stemmer
    ps = PorterStemmer()

    # --- Example 1: List of Words ---
    print("\n[Example 1] Stemming a list of related words:")
    example_words = ["walk", "walks", "walked", "walking"]
    print(f"Input Words: {example_words}")
    print("Result:")
    for w in example_words:
        root_word = ps.stem(w)
        print(f"  {w:10} -> {root_word}")

    # --- Example 2: Complete Sentence ---
    print("\n[Example 2] Stemming a complete sentence:")
    sentence = "Let me sleep through the chaos, let me escape the reality one more time, I’m tired"
    print(f"Input Sentence: \"{sentence}\"")
    
    # Tokenization: Splitting sentence into words
    words = word_tokenize(sentence)
    
    print("Result (Token -> Stem):")
    for w in words:
        root_word = ps.stem(w)
        # Printing inline for brevity, or list format
        print(f"  {w} -> {root_word}")

    # --- Example 3: Formatted Output ---
    print("\n[Example 3] Formatted Stemming on another sentence:")
    text = "walking running plays studies sleeps worked"
    print(f"Input Text: \"{text}\"")
    tokenization = nltk.word_tokenize(text)
    for w in tokenization:
        print("Stemming for {:10} is {}".format(w, ps.stem(w)))

# ==========================================
# Function: Demonstrate Lemmatization
# ==========================================
def demonstrate_lemmatization():
    """
    Executes lemmatization examples using the WordNet Lemmatizer.
    """
    print("\n=========================================")
    print("         Part 2: Lemmatization           ")
    print("=========================================")
    
    # Initialize the WordNet Lemmatizer
    wordnet_lemmatizer = WordNetLemmatizer()
    
    text = "walking running plays studies sleeps worked"
    print(f"\n[Example] Lemmatizing text: \"{text}\"")
    
    # Tokenize the text
    tokenization = nltk.word_tokenize(text)
    
    print("Result:")
    for w in tokenization:
        # Note: Without POS tags, WordNetLemmatizer defaults to Noun (n).
        # For actual verbs like 'walking', it might remain 'walking' if not specified as verb.
        # But for this experiment, we follow the basic implementation.
        lemma = wordnet_lemmatizer.lemmatize(w)
        print("Lemma for {:10} is {}".format(w, lemma))

# ==========================================
# Main Execution Block
# ==========================================
if __name__ == "__main__":
    # Execute Stemming Demonstrations
    demonstrate_stemming()
    
    # Execute Lemmatization Demonstrations
    demonstrate_lemmatization()
    
    print("\n=========================================")
    print("      End of Experiment 2                ")
    print("=========================================")
