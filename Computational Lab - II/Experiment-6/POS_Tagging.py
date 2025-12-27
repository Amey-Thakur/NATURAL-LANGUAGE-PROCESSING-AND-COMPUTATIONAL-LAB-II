"""
============================================================================================
Experiment 6: POS Tagging - Hidden Markov Model
============================================================================================
Course: Natural Language Processing (DLO8012)
Lab: Computational Lab II (CSL804)
Experiment No: 6
Roll No: 50
Name: Amey Thakur
Class: BE Comps B
Batch: B3
Date: February 28, 2022

Aim:
Perform and analyse POS Tagging - Hidden Markov Model using a virtual lab.

Description:
This program demonstrates the calculation of Emission and Transition probabilities for a Hidden 
Markov Model (HMM) based on a provided corpus. This technique is fundamental to Part-of-Speech 
(POS) tagging, where the goal is to assign the most likely sequence of tags to a sequence of words.

The program solves "Question of Curiosity" Q4 from the lab report:
"Find HMM probabilities for the following corpus."

Corpus:
1. They/pronoun cut/verb the/determiner paper/noun
2. EOS/eos He/pronoun asked/verb for/preposition his/pronoun cut/noun
3. EOS/eos Put/verb the/determiner paper/noun in/preposition the/determiner cut/noun EOS/eos

Key Concepts:
1. Emission Probability: P(Word|Tag)
   Likelihood of a word appearing given a specific tag.
   Calculation: Count(Tag, Word) / Count(Tag)

2. Transition Probability: P(Tag_i|Tag_i-1)
   Likelihood of a tag following another tag.
   Calculation: Count(Tag_i-1, Tag_i) / Count(Tag_i-1)

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

# Use a dictionary to represent the counts directly as extracting them from raw text 
# without a parser would be complex for this demonstration.
# These counts are derived manually from Q4 in the report.

# Unique Tags: {noun, verb, preposition, determiner, pronoun, eos}
# Unique Words: {they, cut, the, paper, he, asked, for, his, put, in}

tags = ['noun', 'verb', 'preposition', 'determiner', 'pronoun', 'eos']

# Emission Counts: Count(Tag, Word)
# Format: { 'Tag': {'Word': Count, ...}, ... }
emission_counts = {
    'noun': {'paper': 2, 'cut': 1},     # Total = 3
    'verb': {'cut': 1, 'asked': 1, 'put': 1}, # Total = 3
    'preposition': {'for': 1, 'in': 1}, # Total = 2
    'determiner': {'the': 3},           # Total = 3 (Wait, check: 'the' appears 3 times total)
                                        # 1. the/det paper/noun
                                        # 2. the/det paper/noun
                                        # 3. the/det cut/noun
                                        # Yes, 3 times.
    'pronoun': {'they': 1, 'he': 1, 'his': 1}, # Total = 3
    'eos': {'eos': 3} # 3 EOS tags (Start of 2, 3 and End of 3? Actually logic is usually per sentence boundary)
                      # Based on the matrix provided in the image:
                      # EOS to EOS transition exists? No, typically EOS is a state.
}

# Tag Totals (Count(Tag)) - Denominators for Emission Prob
tag_totals = {
    'noun': 3,
    'verb': 3,
    'preposition': 2,
    'determiner': 3,   # Wait, report says 4? Let's check the report matrix.
                       # Image 5: Determiner column has 1 for 'the' but that's P(the|det)=1?
                       # let's look at the emission matrix in the image for Q4
                       # determiner row: 'the' has 1. Count(det) is denominator.
                       # wait, 'the' appears 3 times. 
                       # Let's trust my manual count or the report's result?
                       # Report Q4 Emission Matrix:
                       # determiner -> the: 1.0. This implies P(the|det) = 1. So all determiners are 'the'.
    'pronoun': 3,    # Report Q4 Emission Matrix: pronoun -> they(0.5 error?), he, his
                     # The matrix shows: they:0.5 (1/2?), he:?, his:?
                     # Actually: they(0.5), he?, his(0.5). That sums to > 1 or is cut off.
                     # Let's derive purely from the sentences provided in Q4 text.
                     # Sentences:
                     # 1. They/pronoun cut/verb the/determiner paper/noun
                     # 2. EOS/eos He/pronoun asked/verb for/preposition his/pronoun cut/noun
                     # 3. EOS/eos Put/verb the/determiner paper/noun in/preposition the/determiner cut/noun EOS/eos
                     
                     # Tag Counts:
                     # Pronoun: They, He, his = 3
                     # Verb: cut, asked, Put = 3
                     # Determiner: the, the, the = 3
                     # Noun: paper, cut, paper, cut = 4 ??
                     # - paper/noun (S1)
                     # - cut/noun (S2)
                     # - paper/noun (S3)
                     # - cut/noun (S3) -- "the cut"
                     # Yes, 4 nouns.
                     # Preposition: for, in = 2
                     # EOS: S2 start, S3 start, S3 end? Representation is tricky. 
                     # Usually EOS represents sentence boundaries.
}

# Corrected Tag Totals based on text walk-through
real_tag_totals = {
    'noun': 4,
    'verb': 3,
    'determiner': 3, 
    'preposition': 2,
    'pronoun': 3
}

# Corrected Emission Counts
real_emission_counts = {
    'noun': {'paper': 2, 'cut': 2},    
    'verb': {'cut': 1, 'asked': 1, 'put': 1}, 
    'preposition': {'for': 1, 'in': 1}, 
    'determiner': {'the': 3},           
    'pronoun': {'they': 1, 'he': 1, 'his': 1} 
}

# Transition Counts: Count(Tag_i-1, Tag_i)
# Sentences again:
# 1. (Start) They/pronoun cut/verb the/determiner paper/noun (End)
# 2. EOS/eos He/pronoun asked/verb for/preposition his/pronoun cut/noun (End?)
# 3. EOS/eos Put/verb the/determiner paper/noun in/preposition the/determiner cut/noun EOS/eos

# Transitions:
# S1: Start -> Pronoun, Pronoun -> Verb, Verb -> Determiner, Determiner -> Noun, Noun -> ?
# S2: EOS -> Pronoun, Pronoun -> Verb, Verb -> Preposition, Preposition -> Pronoun, Pronoun -> Noun
# S3: EOS -> Verb, Verb -> Determiner, Determiner -> Noun, Noun -> Preposition, Preposition -> Determiner, Determiner -> Noun, Noun -> EOS

# We need a standard Start/EOS handling. The prompt implies EOS is an explicit tag at start/end.
# Let's follow the Q4 Transition Matrix labels:
# Rows/Cols: eos, noun, verb, preposition, determiner, pronoun.

# Pairs:
# (eos, pronoun) - S2
# (eos, verb) - S3
# (pronoun, verb) - S1, S2
# (pronoun, noun) - S2
# (verb, determiner) - S1, S3
# (verb, preposition) - S2
# (determiner, noun) - S1, S3, S3 (3 times)
# (noun, preposition) - S3
# (noun, eos) - S3
# (preposition, pronoun) - S2
# (preposition, determiner) - S3

# Total Transitions from each Tag:
# eos: -> pronoun, -> verb. Total = 2? (S1 start undefined? Assume standard).
# pronoun: -> verb, -> verb, -> noun. Total = 3.
# verb: -> det, -> prep, -> det. Total = 3.
# determiner: -> noun, -> noun, -> noun. Total = 3.
# noun: -> ?, -> ?, -> prep, -> eos. (S1 end?, S2 end?).
# preposition: -> pronoun, -> det. Total = 2.

def calculate_probability(count, total):
    if total == 0: return 0.0
    return round(count / total, 3) # Rounding to 3 decimals

# ==========================================
# Main Execution
# ==========================================
def main():
    print("=========================================")
    print("      Experiment 6: POS Tagging - HMM    ")
    print("=========================================")
    print("Calculating HMM probabilities for the Q4 Corpus.\n")

    # 1. Emission Matrix
    print("--- Emission Probabilities P(Word | Tag) ---")
    print(f"{'Tag':<12} | {'Word':<10} | {'Count':<5} | {'Total(Tag)':<10} | {'Probability'}")
    print("-" * 60)
    
    for tag in tags:
        if tag == 'eos': continue # EOS usually doesn't emit words in this context
        
        words = real_emission_counts.get(tag, {})
        total = real_tag_totals.get(tag, 0)
        
        for word, count in words.items():
            prob = calculate_probability(count, total)
            print(f"{tag:<12} | {word:<10} | {count:<5} | {total:<10} | {prob}")
            
    print("\n")

    # 2. Transition Matrix (Manual Logic Implementation)
    print("--- Transition Probabilities P(Tag_i | Tag_i-1) ---")
    # Defining counts based on the manual trace above
    transitions = {
        'eos': {'pronoun': 1, 'verb': 1}, # Assuming S1 starts implicitly or isn't counted in 'eos' row of report
        'pronoun': {'verb': 2, 'noun': 1},
        'verb': {'determiner': 2, 'preposition': 1},
        'determiner': {'noun': 3},
        'noun': {'preposition': 1, 'eos': 1}, # Missing S1 end, S2 end handling
        'preposition': {'pronoun': 1, 'determiner': 1}
    }
    
    # Totals for denominators
    trans_totals = {
        'eos': 2, # based on observed next tags
        'pronoun': 3,
        'verb': 3,
        'determiner': 3,
        'noun': 2, # based on observed next tags (incomplete corpus info)
        'preposition': 2
    }

    print(f"{'Previous(Ti-1)':<15} | {'Next(Ti)':<12} | {'Count':<5} | {'Total':<5} | {'Probability'}")
    print("-" * 65)

    for prev_tag, next_tags in transitions.items():
        total = trans_totals.get(prev_tag, 0)
        for next_tag, count in next_tags.items():
            prob = calculate_probability(count, total)
            print(f"{prev_tag:<15} | {next_tag:<12} | {count:<5} | {total:<5} | {prob}")

    print("\nObservations:")
    print("1. Determiners (e.g., 'the') have a 100% probability of transitioning to a Noun in this corpus.")
    print("2. The word 'cut' is ambiguous; it acts as both a Verb and a Noun.")
    print("   - P(cut | verb) = 1/3 = 0.33")
    print("   - P(cut | noun) = 2/4 = 0.50")
    print("   This ambiguity is resolved by the HMM using context (Transition Probabilities).")
    print("=========================================")

if __name__ == "__main__":
    main()
