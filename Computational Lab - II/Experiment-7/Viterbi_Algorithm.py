"""
============================================================================================
Experiment 7: Sequence Labeling using Viterbi Algorithm
============================================================================================
Course: Natural Language Processing (DLO8012)
Lab: Computational Lab II (CSL804)
Experiment No: 7
Roll No: 50
Name: Amey Thakur
Class: BE Comps B
Batch: B3
Date: April 01, 2022

Aim:
Implement the Viterbi algorithm using Python or NLTK.

Description:
This program implements the Viterbi Algorithm, a dynamic programming algorithm for finding the 
most likely sequence of hidden states (called the Viterbi path) that results in a sequence of 
observed events, especially in the context of Hidden Markov Models (HMM).

Key Components:
1. State Space (S): The set of hidden states (e.g., POS tags).
2. Observation Space (O): The set of observable outputs (e.g., words).
3. Transition Matrix (A): Probabilities of moving from one state to another.
4. Emission Matrix (B): Probabilities of an observation being generated from a state.
5. Initial Probability Distribution (C): Probabilities of starting in each state.

Algorithm Steps:
1. Initialization: Calculate probability of starting in each state given the first observation.
2. Recursion: For each subsequent observation, calculate the maximum probability of reaching 
   each state from any possible previous state.
3. Termination: Find the highest probability for the final state.
4. Path Backtracking: Trace back the path that yielded the maximum probabilities to find the 
   optimal sequence of states.

Dependencies:
- numpy: For matrix operations.
- numba: For JIT compilation to speed up the loop execution (optional but used here).
============================================================================================
Repositories:
- NLP Lab: https://github.com/Amey-Thakur/NATURAL-LANGUAGE-PROCESSING-AND-COMPUTATIONAL-LAB-II
- Main: https://github.com/Amey-Thakur/COMPUTER-ENGINEERING
- Profile: https://github.com/Amey-Thakur
============================================================================================
"""

import numpy as np
from numba import jit

@jit(nopython=True) 
def viterbi(A, C, B, O):
    """
    Computes the optimal state sequence using the Viterbi Algorithm.
    
    Args:
        A (numpy.ndarray): Transition probability matrix (IxI).
        C (numpy.ndarray): Initial state probability matrix (I).
        B (numpy.ndarray): Emission probability matrix (IxK).
        O (numpy.ndarray): Observation sequence (N).
        
    Returns:
        tuple: (S_opt, D, E)
            S_opt: Optimal state sequence.
            D: DP Table (Probabilities).
            E: Backpointer Table (Indices).
    """
    I = A.shape[0]    # Number of states
    N = len(O)        # Length of observation sequence

    # Initialize tables
    D = np.zeros((I, N))
    E = np.zeros((I, N-1)).astype(np.int32)
    
    # Initialization step (t=0)
    D[:, 0] = np.multiply(C, B[:, O[0]])

    # Recursion step (t=1 to N-1)
    for n in range(1, N): 
        for i in range(I):
            # Calculate probability candidates from all previous states
            temp_product = np.multiply(A[:, i], D[:, n-1]) 
            
            # Maximize: P(Si) = max(P(Sj) * A[j,i]) * B[i, On]
            D[i, n] = np.max(temp_product) * B[i, O[n]] 
            
            # Store backpointer (index of previous state yielding max prob)
            E[i, n-1] = np.argmax(temp_product)

    # Termination: Find the best final state
    S_opt = np.zeros(N).astype(np.int32) 
    S_opt[-1] = np.argmax(D[:, -1])
    
    # Backtracking: Path reconstruction
    for n in range(N-2, -1, -1):
        S_opt[n] = E[int(S_opt[n+1]), n] 

    return S_opt, D, E

# ==========================================
# Main Execution Block
# ==========================================
if __name__ == "__main__":
    print("=========================================")
    print("      Experiment 7: Viterbi Algorithm    ")
    print("=========================================")
    
    # 1. Define Model Parameters
    # Transition Matrix (A): 3 States
    # State 0 -> [0.8, 0.1, 0.1]
    # State 1 -> [0.2, 0.7, 0.1]
    # State 2 -> [0.1, 0.3, 0.6]
    A = np.array([[0.8, 0.1, 0.1], [0.2, 0.7, 0.1], [0.1, 0.3, 0.6]])
    
    # Initial Probabilities (C)
    C = np.array([0.6, 0.2, 0.2])
    
    # Emission Matrix (B): 3 States x 3 Observation Symbols
    # State 0 emits -> [0.7, 0.0, 0.3]
    B = np.array([[0.7, 0.0, 0.3], [0.1, 0.9, 0.0], [0.0, 0.2, 0.8]])

    # 2. Define Observation Sequence
    # Sequence of indices corresponding to observed symbols
    O = np.array([0, 2, 0, 2, 2, 1]).astype(np.int32) 

    print("\nModel Parameters:")
    print("Transition Matrix (A):\n", A)
    print("Initial Probabilities (C):\n", C)
    print("Emission Matrix (B):\n", B)
    print("Observation Sequence (O):\n", O)

    # 3. aRun Viterbi Algorithm
    S_opt, D, E = viterbi(A, C, B, O)

    # 4. Results
    print("\n-----------------------------------------")
    print("Results:")
    print("-----------------------------------------")
    print('Observation sequence O:', O)
    print('Optimal state sequence S_opt:', S_opt) 

    # Formatting for cleaner output
    np.set_printoptions(formatter={'float': "{: 7.4f}".format}) 
    print('\nDP Table (D) [Probabilities]:')
    print(D)
    
    np.set_printoptions(formatter={'float': "{: 7.0f}".format}) 
    print('\nBackpointer Table (E) [State Indices]:')
    print(E)
    print("=========================================")