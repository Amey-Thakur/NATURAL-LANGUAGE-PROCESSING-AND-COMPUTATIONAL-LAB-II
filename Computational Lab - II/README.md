<!-- =========================================================================================
                                     HEADER SECTION
     ========================================================================================= -->
<div align="center">
  
  # Computational Lab II

  ### CSL804 · Semester VIII · Computer Engineering

  [![Curated by](https://img.shields.io/badge/Curated%20by-Amey%20Thakur-blue.svg)](https://github.com/Amey-Thakur)
  [![Documents](https://img.shields.io/badge/Documents-10-yellowgreen.svg)](#experiment-1-word-analysis)
  [![Language](https://img.shields.io/badge/Language-Python-blue.svg)](./)
  [![Type](https://img.shields.io/badge/Type-Code%20%7C%20PDF-brightgreen.svg)](./)

  **A comprehensive collection of laboratory experiments for Natural Language Processing, covering morphology, language modeling, POS tagging, parsing, and semantic analysis.**

  ---

  [How to Use](#how-to-use) &nbsp;·&nbsp; [Learning Path](#learning-path) &nbsp;·&nbsp; [Experiment-1](#experiment-1-word-analysis) &nbsp;·&nbsp; [Experiment-2](#experiment-2-stemming--lemmatization) &nbsp;·&nbsp; [Experiment-3](#experiment-3-n-gram-modelling) &nbsp;·&nbsp; [Experiment-4](#experiment-4-n-gram-smoothing) &nbsp;·&nbsp; [Experiment-5](#experiment-5-bi-gram-model) &nbsp;·&nbsp; [Experiment-6](#experiment-6-pos-tagging) &nbsp;·&nbsp; [Experiment-7](#experiment-7-viterbi-algorithm) &nbsp;·&nbsp; [Experiment-8](#experiment-8-morphological-parsing) &nbsp;·&nbsp; [Experiment-9](#experiment-9-chunking) &nbsp;·&nbsp; [Experiment-10](#experiment-10-semantic-analysis)

</div>

---

> [!NOTE]
> **Environment Configuration**: This repository focuses on NLP implementations using **Python**. Key libraries include `NLTK`, `Spacy`, `TextBlob`, and `NumPy`.

> [!TIP]
> **Virtual Lab**: Many experiments utilize the [IIIT Hyderabad NLP Virtual Lab](http://nlp-iiith.vlabs.ac.in) for interactive simulations and foundational understanding before code implementation.

---

<!-- =========================================================================================
                                     HOW TO USE SECTION
     ========================================================================================= -->
## How to Use

### Viewing Implementation
1. **Navigate** to the specific experiment folder (e.g., `Experiment-7`).
2. **Execute** the script using Python:
   - `python Viterbi_Algorithm.py`
3. **Analyze** the console output to observe linguistic processing and results.

### Development Setup
**Required Tools:**
- **Python 3.x**: Core language for scripts.
- **NLTK**: `pip install nltk` (Run `nltk.download('all')` for corpora).
- **Spacy**: `pip install spacy` (Run `python -m spacy download en_core_web_sm`).

---

<!-- =========================================================================================
                                     LEARNING PATH SECTION
     ========================================================================================= -->
## Learning Path

### Phase 1: Morphology
Understanding the structure of words and their formation.
- **Experiment-1**: Perform word analysis and generation tailored to Indian languages using Virtual Lab.
- **Experiment-2**: Implement Stemming and Lemmatization to reduce words to their base forms.
- **Experiment-8**: Create a Morphological Parser to accept/reject words based on affixes.

### Phase 2: Language Modeling
Predicting probabilities of word sequences.
- **Experiment-3**: Analyze N-Gram probabilities using Virtual Lab.
- **Experiment-4**: Apply Smoothing techniques (Add-1, Good-Turing) to handle unseen data.
- **Experiment-5**: Implement a Bi-gram language model in Python.

### Phase 3: Sequence Labeling & Parsing
Assigning structural and grammatical roles.
- **Experiment-6**: Perform POS Tagging using HMMs via Virtual Lab.
- **Experiment-7**: Implement the Viterbi Algorithm for optimal sequence decoding.
- **Experiment-9**: Perform Chunking (Shallow Parsing) to identify Noun Phrases.

### Phase 4: Advanced Analysis
Deriving meaning and insights from text.
- **Experiment-10**: Analyze Semantic Analysis techniques from a research perspective.

---

<!-- =========================================================================================
                                     EXPERIMENT-1
     ========================================================================================= -->
## Experiment-1: Word Analysis

Perform Word analysis and word generation to study morphology using Virtual Lab.

**Date:** January 19, 2022

| # | Program | Description | Source Code |
|:-:|:---|:---|:-:|
| 1 | Word_Analysis.py | Word analysis script | [View](Experiment-1/Word_Analysis.py) |
| 2 | Word_Generator.py | Word generation script | [View](Experiment-1/Word_Generator.py) |
| — | Lab Report (PDF) | Detailed experiment report | [View](Experiment-1/AMEY_B-50_NLP_EXPERIMENT-1.pdf) |

---

<!-- =========================================================================================
                                     EXPERIMENT-2
     ========================================================================================= -->
## Experiment-2: Stemming & Lemmatization

Implement stemming and lemmatization operations for a corpus.

**Date:** January 31, 2022

| # | Program | Description | Source Code |
|:-:|:---|:---|:-:|
| 1 | Stemming_Lemmatization.py | Stemming and Lemmatization logic | [View](Experiment-2/Stemming_Lemmatization.py) |
| — | Lab Report (PDF) | Detailed experiment report | [View](Experiment-2/AMEY_B-50_NLP_EXPERIMENT-2.pdf) |

---

<!-- =========================================================================================
                                     EXPERIMENT-3
     ========================================================================================= -->
## Experiment-3: N-Gram Modelling

Perform and analyse an n-gram modelling for corpuses using Virtual Lab.

**Date:** February 07, 2022

| # | Program | Description | Source Code |
|:-:|:---|:---|:-:|
| 1 | N_Gram_Modelling.py | Bigram probability calculation | [View](Experiment-3/N_Gram_Modelling.py) |
| — | Lab Report (PDF) | Detailed experiment report | [View](Experiment-3/AMEY_B-50_NLP_EXPERIMENT-3.pdf) |

---

<!-- =========================================================================================
                                     EXPERIMENT-4
     ========================================================================================= -->
## Experiment-4: N-Gram Smoothing

Perform and analyse smoothing operations for n-gram models using the virtual lab.

**Date:** February 14, 2022

| # | Program | Description | Source Code |
|:-:|:---|:---|:-:|
| 1 | Smoothing.py | N-Gram smoothing techniques | [View](Experiment-4/Smoothing.py) |
| — | Lab Report (PDF) | Detailed experiment report | [View](Experiment-4/AMEY_B-50_NLP_EXPERIMENT-4.pdf) |

---

<!-- =========================================================================================
                                     EXPERIMENT-5
     ========================================================================================= -->
## Experiment-5: Bi-gram Model

Implement a bi-gram model for 3 sentences using python or NLTK.

**Date:** February 21, 2022

| # | Program | Description | Source Code |
|:-:|:---|:---|:-:|
| 1 | Bi_Gram_Model.py | Bi-gram language model | [View](Experiment-5/Bi_Gram_Model.py) |
| — | Lab Report (PDF) | Detailed experiment report | [View](Experiment-5/AMEY_B-50_NLP_EXPERIMENT-5.pdf) |

---

<!-- =========================================================================================
                                     EXPERIMENT-6
     ========================================================================================= -->
## Experiment-6: POS Tagging

Perform and analyse POS Tagging - Hidden Markov Model using a virtual lab.

**Date:** February 28, 2022

| # | Program | Description | Source Code |
|:-:|:---|:---|:-:|
| 1 | POS_Tagging.py | HMM Emission/Transition probabilities | [View](Experiment-6/POS_Tagging.py) |
| — | Lab Report (PDF) | Detailed experiment report | [View](Experiment-6/AMEY_B-50_NLP_EXPERIMENT-6.pdf) |

---

<!-- =========================================================================================
                                     EXPERIMENT-7
     ========================================================================================= -->
## Experiment-7: Viterbi Algorithm

Implement the Viterbi algorithm using python or NLTK.

**Date:** April 01, 2022

| # | Program | Description | Source Code |
|:-:|:---|:---|:-:|
| 1 | Viterbi_Algorithm.py | Viterbi algorithm implementation | [View](Experiment-7/Viterbi_Algorithm.py) |
| — | Lab Report (PDF) | Detailed experiment report | [View](Experiment-7/AMEY_B-50_NLP_EXPERIMENT-7.pdf) |

---

<!-- =========================================================================================
                                     EXPERIMENT-8
     ========================================================================================= -->
## Experiment-8: Morphological Parsing

Implement morphological parser to accept and reject given string.

**Date:** April 01, 2022

| # | Program | Description | Source Code |
|:-:|:---|:---|:-:|
| 1 | Morphological_Parser.py | Parser logic (spacy/stemming) | [View](Experiment-8/Morphological_Parser.py) |
| — | Lab Report (PDF) | Detailed experiment report | [View](Experiment-8/AMEY_B-50_NLP_EXPERIMENT-8.pdf) |

---

<!-- =========================================================================================
                                     EXPERIMENT-9
     ========================================================================================= -->
## Experiment-9: Chunking

Perform and analyse chunking operations using the virtual lab.

**Date:** April 01, 2022

| # | Program | Description | Source Code |
|:-:|:---|:---|:-:|
| 1 | Chunking.py | Shallow Parsing (NP Chunking) | [View](Experiment-9/Chunking.py) |
| — | Lab Report (PDF) | Detailed experiment report | [View](Experiment-9/AMEY_B-50_NLP_EXPERIMENT-9.pdf) |

---

<!-- =========================================================================================
                                     EXPERIMENT-10
     ========================================================================================= -->
## Experiment-10: Semantic Analysis

Case Study: Research Paper Analysis - Semantic Analysis of NLP.

**Date:** April 14, 2022

| # | Program | Description | Source Code |
|:-:|:---|:---|:-:|
| 1 | Semantic_Analysis.py | Tokenization, NER, Sentiment Analysis | [View](Experiment-10/Semantic_Analysis.py) |
| — | Lab Report (PDF) | Detailed experiment report | [View](Experiment-10/AMEY_B-50_NLP_CASE_STUDY.pdf) |

---

<!-- =========================================================================================
                                     FOOTER SECTION
     ========================================================================================= -->
<div align="center">

  <!-- Footer Navigation -->
  [↑ Back to Top](#computational-lab-ii)

  [How to Use](#how-to-use) &nbsp;·&nbsp; [Learning Path](#learning-path) &nbsp;·&nbsp; [Experiment-1](#experiment-1-word-analysis) &nbsp;·&nbsp; [Experiment-2](#experiment-2-stemming--lemmatization) &nbsp;·&nbsp; [Experiment-3](#experiment-3-n-gram-modelling) &nbsp;·&nbsp; [Experiment-4](#experiment-4-n-gram-smoothing) &nbsp;·&nbsp; [Experiment-5](#experiment-5-bi-gram-model) &nbsp;·&nbsp; [Experiment-6](#experiment-6-pos-tagging) &nbsp;·&nbsp; [Experiment-7](#experiment-7-viterbi-algorithm) &nbsp;·&nbsp; [Experiment-8](#experiment-8-morphological-parsing) &nbsp;·&nbsp; [Experiment-9](#experiment-9-chunking) &nbsp;·&nbsp; [Experiment-10](#experiment-10-semantic-analysis)

  <br>

  🏠 **[Back to Main Repository](../)**

</div>

---

<div align="center">

  ### [Natural Language Processing and Computational Lab II](../)

  **CSL804 · Semester VIII · Computer Engineering**

  *University of Mumbai · Curated by [Amey Thakur](https://github.com/Amey-Thakur)*

</div>
