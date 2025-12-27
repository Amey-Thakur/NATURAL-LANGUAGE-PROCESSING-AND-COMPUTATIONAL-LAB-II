"""
============================================================================================
Experiment 9: Chunking (Shallow Parsing)
============================================================================================
Course: Natural Language Processing (DLO8012)
Lab: Computational Lab II (CSL804)
Experiment No: 9
Roll No: 50
Name: Amey Thakur
Class: BE Comps B
Batch: B3
Date: April 01, 2022

Aim:
Perform and analyse chunking operations using the virtual lab.

Description:
This program demonstrates "Chunking" (also known as Shallow Parsing) using NLTK.
Chunking is the process of extracting phrases (like Noun Phrases, Verb Phrases) from
unstructured text. Unlike full parsing, which builds a complete parse tree, chunking
identifies constituents but does not specify their internal structure or role in the
main sentence.

The code addresses the "Question of Curiosity" from the lab report:
"Identify the errors, mark them into categories: invalid chunk boundaries, not a minimal phrase,
and incorrect chunk label."

Implementation:
1. Defines a Noun Phrase (NP) chunk grammar.
2. Uses NLTK's RegexpParser to parse sentences.
3. Demonstrates chunking on valid and erroneous examples to illustrate the concepts.

Dependencies:
- nltk: For tokenization, POS tagging, and chunking.
============================================================================================
Repositories:
- NLP Lab: https://github.com/Amey-Thakur/NATURAL-LANGUAGE-PROCESSING-AND-COMPUTATIONAL-LAB-II
- Main: https://github.com/Amey-Thakur/COMPUTER-ENGINEERING
- Profile: https://github.com/Amey-Thakur
============================================================================================
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Ensure necessary NLTK models are downloaded
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

def run_chunker(sentences):
    """
    Performs chunking on a list of sentences using a basic NP-Chunk grammar.
    """
    print("-" * 60)
    print(f"{'Sentence':<30} | {'Extracted Noun Phrase Chunks'}")
    print("-" * 60)

    # Define a simple grammar for Noun Phrases (NP)
    # NP: Optional Determiner (DT) + Any number of Adjectives (JJ) + Noun (NN)
    grammar = r"""
      NP: {<DT|PP\$>?<JJ>*<NN>}   # chunk determiner/possessive, adjectives and noun
          {<NNP>+}                # chunk sequences of proper nouns
    """
    
    cp = nltk.RegexpParser(grammar)

    for sentence in sentences:
        tokens = word_tokenize(sentence)
        tagged = pos_tag(tokens)
        tree = cp.parse(tagged)
        
        # Extract NPs from the tree (subtrees labeled 'NP')
        nps = []
        for subtree in tree.subtrees(filter=lambda t: t.label() == 'NP'):
            nps.append(" ".join([w for w, t in subtree.leaves()]))
        
        print(f"{sentence:<30} | {nps}")
        
    print("-" * 60)

if __name__ == "__main__":
    print("=========================================")
    print("      Experiment 9: Chunking Analysis    ")
    print("=========================================")
    
    # Examples derived from the "Question of Curiosity" in the Lab Report
    # Note: These sentences are used to demonstrate how a chunker processes text.
    # The 'errors' mentioned in the question (invalid boundaries, etc.) are logical errors
    # in manual chunking, but here we show programmatic chunking.
    
    test_sentences = [
        "She is a beautiful girl",          # Q1: [NP She] [VP is] [AJDP a beautiful] [NP girl]
        "He could not be tolerated",        # Q2: [NP He] [VP could not] [ADJP be tolerated]
        "They invited him to the dinner",   # Q3: [NP They] [VP invited] [NP him to] [NP the dinner party]
        "He was shot by the swats",         # Q4: [NP He] [VP was shot] [NP by the swats]
        "He longed for a hot cup of coffee" # Q5: [NP He] [VP longed] [PP for] [NP a hot cup of coffee]
    ]

    print("Analyzing sentences using NLTK RegexpParser (NP Grammar)...")
    try:
        run_chunker(test_sentences)
        print("\nNote: The output shows Noun Phrases (NP) identified by the defined grammar.")
        print("This programmatic approach creates consistent boundaries based on POS tags,")
        print("avoiding the manual errors discussed in the lab report's 'Curiosity' section.")
    except LookupError as e:
        print("\nError: NLTK resources not found.")
        print("Please run: nltk.download('punkt') and nltk.download('averaged_perceptron_tagger')")
        print(e)

    print("=========================================")
