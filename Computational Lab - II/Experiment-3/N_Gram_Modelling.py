"""
============================================================================================
Experiment 3: N-Gram Modelling
============================================================================================
Course: Natural Language Processing (DLO8012)
Lab: Computational Lab II (CSL804)
Experiment No: 3
Roll No: 50
Name: Amey Thakur
Class: BE Comps B
Batch: B3
Date: February 07, 2022

Aim:
Perform and analyse an n-gram modelling for corpuses using Virtual Lab.

Description:
This program implements a Bigram Language Model to calculate the probability of word 
sequences. An N-gram model predicts the occurrence of a word based on the occurrence of its 
N-1 previous words. In this experiment, we focus on N=2 (Bigrams).

The code specifically addresses the problem statement from the standard lab manual/report:
"Find bigram probabilities for given sentences (CORPUS)."

Corpus:
1. "can one play on ground"
2. "only work no play"
3. "one is on ground"

Use Case:
N-gram models are widely used in statistical natural language processing for tasks such as:
- Speech Recognition
- Machine Translation
- Spelling Correction
- Predictive Text Input

Algorithm:
1. Preprocess the corpus:
   - Tokenize sentences into words.
   - Add padding (<start>, <end> tokens) if necessary (simplified here to raw counts).
2. Generate all unique words (vocabulary) to form the matrix rows and columns.
3. Count frequencies of individual words (Unigrams).
4. Count frequencies of adjacent word pairs (Bigrams).
5. Calculate Bigram Probabilities using the formula:
   P(Wn | Wn-1) = Count(Wn-1, Wn) / Count(Wn-1)
6. Display the probability matrix.
============================================================================================
Repositories:
- NLP Lab: https://github.com/Amey-Thakur/NATURAL-LANGUAGE-PROCESSING-AND-COMPUTATIONAL-LAB-II
- Main: https://github.com/Amey-Thakur/COMPUTER-ENGINEERING
- Profile: https://github.com/Amey-Thakur
============================================================================================
"""

# ==========================================
# Corpus Definition
# ==========================================
# The specific sentences provided in the problem statement.
corpus = [
    "can one play on ground",
    "only work no play",
    "one is on ground"
]

def generate_bigram_model(corpus):
    """
    Generates and displays a bigram probability matrix for the given corpus.
    """
    print("=========================================")
    print("      Experiment 3: N-Gram Modelling     ")
    print("=========================================")
    print("Input Corpus (Sentences):")
    for i, sent in enumerate(corpus, 1):
        print(f"{i}. {sent}")
    print("\nProcessing...")

    # Step 1: Tokenization and Vocabulary Building
    tokens = []
    for sentence in corpus:
        # Simple whitespace tokenization
        tokens.extend(sentence.lower().split())
    
    # Get unique words for the matrix axes, sorted for consistent output
    # 'ground' appears twice, 'play' appears twice, etc.
    vocab = sorted(list(set(tokens)))
    vocab_size = len(vocab)
    
    print(f"Vocabulary ({vocab_size} words): {vocab}")

    # Step 2: Calculate Counts
    # We need a matrix to store Bigram counts: Count(WordA followed by WordB)
    # And a dictionary for Unigram counts: Count(WordA)
    
    bigram_counts = {w1: {w2: 0 for w2 in vocab} for w1 in vocab}
    unigram_counts = {w: 0 for w in vocab}

    # Count occurrences
    for sentence in corpus:
        words = sentence.lower().split()
        for i in range(len(words)):
            # Count Unigram
            unigram_counts[words[i]] += 1
            
            # Count Bigram (if there is a next word)
            if i < len(words) - 1:
                w1 = words[i]
                w2 = words[i+1]
                bigram_counts[w1][w2] += 1

    # Step 3: Calculate Probabilities and Display Matrix
    # P(w2 | w1) = Count(w1, w2) / Count(w1)
    
    print("\n--- Bigram Probability Matrix ---")
    print("Format: P(Column Word | Row Word)\n")

    # Print Header Row
    header = "       " + "".join([f"{w:>8}" for w in vocab])
    print(header)
    print("-" * len(header))

    # Print Rows
    for w1 in vocab:
        row_str = f"{w1:>6} |"
        for w2 in vocab:
            count_w1_w2 = bigram_counts[w1][w2]
            count_w1 = unigram_counts[w1]
            
            # Calculate Probability
            # If a word appears at the end of a sentence but never starts a bigram 
            # (conceptually), count_w1 might be valid, but we strictly follow the corpus pairs.
            # In this simple model w/o line-bridging:
            # count_w1 is the total times w1 appears. 
            # However, for P(w2|w1), the denominator represents times w1 is *followed* by something.
            # For this specific textbook problem, we usually take total count of w1.
            
            if count_w1 > 0:
                prob = count_w1_w2 / count_w1
            else:
                prob = 0.0
            
            # Formatting to match the typical "0" or "0.5" or "1" style
            # Using 2 decimal places for clarity
            row_str += f"{prob:>8.2f}"
        print(row_str)

    print("\n-----------------------------------------")
    print("Interpretation:")
    print("Each cell value represents the conditional probability P(Next | Previous).")
    print("e.g., if Row='can' and Col='one', value is P(one | can).")
    print("=========================================")

# ==========================================
# Main Execution Block
# ==========================================
if __name__ == "__main__":
    generate_bigram_model(corpus)
