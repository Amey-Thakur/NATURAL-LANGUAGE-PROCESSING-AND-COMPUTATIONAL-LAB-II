"""
============================================================================================
Experiment 5: N-Gram (Bi-gram) Language Modeling
============================================================================================
Course: Natural Language Processing (DLO8012)
Lab: Computational Lab II (CSL804)
Experiment No: 5
Roll No: 50
Name: Amey Thakur
Class: BE Comps B
Batch: B3
Date: February 21, 2022

Aim:
Implement a bi-gram model for 3 sentences using Python or NLTK.

Description:
This program implements a Bigram Language Model from scratch without using NLTK's built-in 
ngrams function. It calculates the conditional probability of a sequence of words based on 
the bigram probabilities learned from a small training corpus.

Key Concepts:
1. Bigram: A sequence of two adjacent elements from a string of tokens.
2. Training Corpus: A set of sentences used to calculate the frequency of word pairs.
3. Probability Calculation:
   P(Wn | Wn-1) = Count(Wn-1, Wn) / Count(Wn-1)

Algorithm:
1. Read the training corpus (list of sentences).
2. Preprocess and tokenize the corpus into a linear list of words.
3. Generate all possible Bigrams from the tokenized list.
4. Calculate frequencies:
   - Bigram Frequency: How often word pairs appear together.
   - Unigram Frequency: How often individual words appear.
5. Compute Bigram Probabilities using the frequency counts.
6. Test the model:
   - Input a test sentence (e.g., "I love my name").
   - Generate bigrams for the test sentence.
   - Calculate the total probability of the sentence by multiplying the probabilities 
     of its constituent bigrams (simplistic Markov assumption).
============================================================================================
Repositories:
- NLP Lab: https://github.com/Amey-Thakur/NATURAL-LANGUAGE-PROCESSING-AND-COMPUTATIONAL-LAB-II
- Main: https://github.com/Amey-Thakur/COMPUTER-ENGINEERING
- Profile: https://github.com/Amey-Thakur
============================================================================================
"""

# ==========================================
# Function definitions
# ==========================================

def read_data():
    """
    Initializes the training corpus.
    Returns a flat list of tokens from the corpus.
    """
    # Training sentences
    data = [
        'This is a  dog',
        'This is a cat',
        'I love my cat',
        'This is my name '
    ]
    
    print("--- Training Corpus ---")
    for sent in data:
        print(f"\"{sent}\"")
        
    # Flattening the list of sentences into a list of words
    dat = []
    for sentence in data:
        for word in sentence.split():
            dat.append(word)
    
    print(f"\nTokenized Training Data: {dat}\n")
    return dat

def create_bigram(data):
    """
    Generates bigrams and calculates frequencies from the token list.
    
    Args:
        data (list): List of tokens.
        
    Returns:
        tuple: (list_of_bigrams, unigram_counts, bigram_counts)
    """
    list_of_bigrams = []
    bigram_counts = {}
    unigram_counts = {}

    for i in range(len(data) - 1):
        # Constraint to ensure we don't bridge sentences incorrectly if simple flattening is used
        # The logic here assumes if the NEXT word is lowercase, it belongs to the same sentence flow.
        # Ideally, padding should be used, but we follow the original logic provided.
        if i < len(data) - 1 and data[i+1].islower():
            list_of_bigrams.append((data[i], data[i + 1]))
            
            # Count Bigrams
            if (data[i], data[i+1]) in bigram_counts:
                bigram_counts[(data[i], data[i + 1])] += 1
            else:
                bigram_counts[(data[i], data[i + 1])] = 1

        # Count Unigrams (Basic logic for the denominator)
        if data[i] in unigram_counts:
            unigram_counts[data[i]] += 1
        else:
            unigram_counts[data[i]] = 1
            
    return list_of_bigrams, unigram_counts, bigram_counts

def calc_bigram_prob(list_of_bigrams, unigram_counts, bigram_counts):
    """
    Calculates the conditional probability for each bigram.
    P(w2|w1) = Count(w1, w2) / Count(w1)
    """
    list_of_prob = {}
    for bigram in list_of_bigrams:
        word1 = bigram[0]
        word2 = bigram[1]
        
        # Avoid division by zero if logic is sound
        if word1 in unigram_counts:
            list_of_prob[bigram] = (bigram_counts.get(bigram)) / (unigram_counts.get(word1))
        else:
            list_of_prob[bigram] = 0.0
            
    return list_of_prob

# ==========================================
# Main Execution Block
# ==========================================
if __name__ == '__main__':
    print("=========================================")
    print("      Experiment 5: Bi-gram Model        ")
    print("=========================================")

    # Step 1: Read Data
    data = read_data()

    # Step 2: Create Bigrams and Counts
    list_of_bigrams, unigram_counts, bigram_counts = create_bigram(data)

    print("All possible Bigrams formed (filtered by lower-case logic):")
    print(list_of_bigrams)

    print("\nBigrams with their Frequency:")
    print(bigram_counts)

    print("\nUnigrams with their Frequency:")
    print(unigram_counts)

    # Step 3: Calculate Probabilities
    bigram_prob = calc_bigram_prob(list_of_bigrams, unigram_counts, bigram_counts)

    print("\nBigrams with their Probability P(w2|w1):")
    print(bigram_prob)

    # Step 4: Test on a new sentence
    input_sentence = "I love my name"
    print(f"\n-----------------------------------------\nTesting Sentence: \"{input_sentence}\"")
    
    splt = input_sentence.split()
    output_prob = 1.0
    bilist = []

    # Generate bigrams for the test sentence
    for i in range(len(splt) - 1):
         bilist.append((splt[i], splt[i + 1]))

    print("Bigrams in test sentence:")
    print(bilist)

    # Calculate Total Probability
    for i in range(len(bilist)):
        if bilist[i] in bigram_prob:
            prob = bigram_prob[bilist[i]]
            print(f"P({bilist[i]}) = {prob}")
            output_prob *= prob
        else:
            print(f"P({bilist[i]}) = 0 (Unseen)")
            output_prob *= 0

    print(f"\nFinal Probability of sentence \"{input_sentence}\" = {str(output_prob)}")
    print("=========================================")
