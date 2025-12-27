"""
============================================================================================
Experiment 10: Case Study - Semantic Analysis of NLP
============================================================================================
Course: Natural Language Processing (DLO8012)
Lab: Computational Lab II (CSL804)
Experiment No: 10
Roll No: 50
Name: Amey Thakur
Class: BE Comps B
Batch: B3
Date: April 14, 2022

Aim:
A State of Art for Semantic Analysis of Natural Language Processing.

Description:
This program is a practical demonstration of the concepts discussed in the Case Study:
"A State of Art for Semantic Analysis of Natural Language Processing".
The research paper analyzes various NLP techniques including Tokenization, Named Entity 
Recognition (NER), and Sentiment Analysis.

This script implements:
1. Tokenization: Breaking text into individual units.
2. Named Entity Recognition (NER): Identifying real-world objects (PERSON, ORG, etc.).
3. Semantic/Sentiment Analysis: Determining the emotional tone (Polarity) and subjectivity.

Dependencies:
- spacy: For robust Tokenization and NER.
- textblob: For simple API access to Sentiment Analysis.
============================================================================================
Repositories:
- NLP Lab: https://github.com/Amey-Thakur/NATURAL-LANGUAGE-PROCESSING-AND-COMPUTATIONAL-LAB-II
- Main: https://github.com/Amey-Thakur/COMPUTER-ENGINEERING
- Profile: https://github.com/Amey-Thakur
============================================================================================
"""

import spacy
from textblob import TextBlob

# Load Spacy English model
try:
    nlp = spacy.load('en_core_web_sm')
except OSError:
    print("Error: Spacy model 'en_core_web_sm' not found. Please run: python -m spacy download en_core_web_sm")
    exit()

def semantic_analysis_demo(text):
    """
    Demonstrates Tokenization, NER, and Sentiment Analysis on the input text.
    """
    print("-" * 60)
    print(f"Input Text: \"{text}\"")
    print("-" * 60)

    # 1. Processing with Spacy (Tokenization & NER)
    doc = nlp(text)

    print("\n--- 1. Tokenization & POS Tagging (Spacy) ---")
    print(f"{'Token':<15} | {'POS':<10} | {'Explanation'}")
    print("-" * 60)
    for token in doc:
        print(f"{token.text:<15} | {token.pos_:<10} | {spacy.explain(token.pos_)}")

    print("\n--- 2. Named Entity Recognition (NER) ---")
    if doc.ents:
        print(f"{'Entity':<15} | {'Label':<10} | {'Explanation'}")
        print("-" * 60)
        for ent in doc.ents:
            print(f"{ent.text:<15} | {ent.label_:<10} | {spacy.explain(ent.label_)}")
    else:
        print("No named entities found.")

    # 2. Processing with TextBlob (Sentiment Analysis)
    blob = TextBlob(text)
    sentiment = blob.sentiment

    print("\n--- 3. Semantic / Sentiment Analysis (TextBlob) ---")
    print(f"Polarity: {sentiment.polarity:.4f}  (Range: -1.0 to 1.0)")
    print(f"Subjectivity: {sentiment.subjectivity:.4f} (Range: 0.0 to 1.0)")
    
    # Interpretation
    if sentiment.polarity > 0:
        tone = "Positive"
    elif sentiment.polarity < 0:
        tone = "Negative"
    else:
        tone = "Neutral"
    
    print(f"Overall Tone: {tone}")
    print("-" * 60)
    print("\n")

if __name__ == "__main__":
    print("=========================================")
    print("      Experiment 10: Semantic Analysis   ")
    print("=========================================")
    
    # Sample texts demonstrating different sentiments and entities
    samples = [
        "Apple is looking at buying U.K. startup for $1 billion.",
        "I love this product! It is absolutely amazing and useful.",
        "The experience was terrible. I hated the service and the food was cold.",
        "Python is a programming language created by Guido van Rossum."
    ]

    for sample in samples:
        semantic_analysis_demo(sample)

    print("=========================================")
