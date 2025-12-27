"""
============================================================================================
Experiment 4: N-Gram Smoothing
============================================================================================
Course: Natural Language Processing (DLO8012)
Lab: Computational Lab II (CSL804)
Experiment No: 4
Roll No: 50
Name: Amey Thakur
Class: BE Comps B
Batch: B3
Date: February 14, 2022

Aim:
Perform and analyse smoothing operations for n-gram models using the virtual lab.

Description:
This program demonstrates N-gram smoothing techniques to handle the problem of sparsity in
language models (zero probabilities for unseen n-grams).

We implement three approaches to calculate the probability of the sentence 
S = "Dickens read a book":

1. Unsmoothed Probability:
   Uses raw frequency counts. If any bigram in the sentence has a count of 0 (unseen),
   the probability of the entire sentence becomes 0.

2. Add-One Smoothing (Laplace Smoothing):
   Adds 1 to every bigram count and V (vocabulary size) to the normalization factor.
   This ensures no probability is ever zero, but can shift too much mass to unseen events.
   Formula: P(w_i|w_{i-1}) = (Count(w_{i-1}, w_i) + 1) / (Count(w_{i-1}) + V)

3. Add-Delta Smoothing (Lidstone Smoothing):
   Generalization of Laplace smoothing where we add a small number δ (delta) instead of 1.
   Here, δ = 0.02.
   Formula: P(w_i|w_{i-1}) = (Count(w_{i-1}, w_i) + δ) / (Count(w_{i-1}) + δ*V)

Problem Setup:
- Calculated based on the provided "Question of Curiosity" in the lab report.
- The Bigram Count Table is hardcoded based on the report data.
- N = 5100 (Total Bigrams)
- V = 11 (Vocabulary Size: {(eos), John, read, Fountainhead, Mary, a, different, book, She, by, Dickens})

============================================================================================
Repositories:
- NLP Lab: https://github.com/Amey-Thakur/NATURAL-LANGUAGE-PROCESSING-AND-COMPUTATIONAL-LAB-II
- Main: https://github.com/Amey-Thakur/COMPUTER-ENGINEERING
- Profile: https://github.com/Amey-Thakur
============================================================================================
"""

# ==========================================
# Data Definitions
# ==========================================

# Vocabulary
vocab = ["(eos)", "John", "read", "Fountainhead", "Mary", "a", "different", "book", "She", "by", "Dickens"]
V = 11 # Vocabulary Size

# Bigram Counts (Count(w_{i-1}, w_i))
# Format: { 'previous_word': {'next_word': count, ...}, ... }
# Missing entries are assumed to be 0
bigram_counts_table = {
    "(eos)": {"John": 300, "Mary": 300, "She": 300},
    "John":  {"read": 300},
    "read":  {"Fountainhead": 300, "a": 600},
    "Fountainhead": {"(eos)": 300},
    "Mary":  {"read": 300},
    "a":     {"different": 300, "book": 300},
    "different": {"book": 300},
    "book":  {"(eos)": 300, "by": 300},
    "She":   {"Fountainhead": 300},
    "by":    {"Dickens": 300},
    "Dickens": {"(eos)": 300}
}

# Unigram Counts (Count(w_{i-1})) - The row sums
# Calculated manually from the table or derived
unigram_counts_table = {
    "(eos)": 900,
    "John": 300,
    "read": 900,
    "Fountainhead": 300,
    "Mary": 300,
    "a": 600,
    "different": 300,
    "book": 600,
    "She": 300,
    "by": 300,
    "Dickens": 300
}

# Target Sentence to Evaluate: "Dickens read a book"
# This typically implies the sequence: (eos) -> Dickens -> read -> a -> book -> (eos) 
# or just Dickens -> read -> a -> book depending on the model context.
# Based on the report calculation: p(JOHN READ A BOOK) = P(John|Start)*P(read|John)...
# Let's assume the standard start -> end path.
# However, the report question asks for: "Dickens read a book"
# Path: (eos) Dickens read a book (eos)
# But looking at counts:
# (eos) -> Dickens: 0 count
# Dickens -> read: 0 count
# read -> a: 600 count
# a -> book: 300 count
# book -> (eos): 300 count

sentence_sequence = [
    ("(eos)", "Dickens"),
    ("Dickens", "read"),
    ("read", "a"),
    ("a", "book"),
    ("book", "(eos)")
]

def get_count(w1, w2):
    """Refers to bigram count"""
    return bigram_counts_table.get(w1, {}).get(w2, 0)

def get_unigram_count(w1):
    return unigram_counts_table.get(w1, 0)

# ==========================================
# Smoothing Functions
# ==========================================

def unsmoothed_probability(w1, w2):
    c_w1_w2 = get_count(w1, w2)
    c_w1 = get_unigram_count(w1)
    if c_w1 == 0: return 0
    return c_w1_w2 / c_w1

def add_one_smoothing(w1, w2):
    c_w1_w2 = get_count(w1, w2)
    c_w1 = get_unigram_count(w1)
    # P = (C + 1) / (N + V)
    return (c_w1_w2 + 1) / (c_w1 + V)

def add_delta_smoothing(w1, w2, delta=0.02):
    c_w1_w2 = get_count(w1, w2)
    c_w1 = get_unigram_count(w1)
    # P = (C + delta) / (N + delta*V)
    return (c_w1_w2 + delta) / (c_w1 + (delta * V))

# ==========================================
# Main Execution
# ==========================================
def main():
    print("=========================================")
    print("      Experiment 4: N-Gram Smoothing     ")
    print("=========================================")
    print("Calculating probability for sentence sequence:\nS = '(eos) Dickens read a book (eos)'\n")

    print(f"{'Bigram (w1, w2)':<25} | {'Count(w1)':<10} | {'Count(w1,w2)':<12} | {'Unsmoothed':<12} | {'Add-One':<12} | {'Add-Delta':<12}")
    print("-" * 100)

    prob_unsmoothed_total = 1.0
    prob_add_one_total = 1.0
    prob_add_delta_total = 1.0

    for w1, w2 in sentence_sequence:
        c1 = get_unigram_count(w1)
        c12 = get_count(w1, w2)
        
        p_u = unsmoothed_probability(w1, w2)
        p_1 = add_one_smoothing(w1, w2)
        p_d = add_delta_smoothing(w1, w2, delta=0.02)
        
        prob_unsmoothed_total *= p_u
        prob_add_one_total *= p_1
        prob_add_delta_total *= p_d

        print(f"{str((w1, w2)):<25} | {c1:<10} | {c12:<12} | {p_u:<12.5f} | {p_1:<12.5f} | {p_d:<12.5f}")

    print("-" * 100)
    print(f"{'TOTAL PROBABILITY (P)':<51} | {prob_unsmoothed_total:<12.5g} | {prob_add_one_total:<12.5g} | {prob_add_delta_total:<12.5g}")
    print("\nObservations:")
    print("1. Unsmoothed: Probability is 0 because '(eos) Dickens' and 'Dickens read' never occurred in training.")
    print("2. Add-One: Assigns some probability mass to unseen bigrams, estimating P > 0.")
    print("3. Add-Delta: Uses a smaller δ (0.02) to assign less mass to unseen events, often better for sparse data.")
    print("=========================================")

if __name__ == "__main__":
    main()
