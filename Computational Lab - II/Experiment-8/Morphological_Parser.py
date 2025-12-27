import spacy
sp = spacy.load('en_core_web_sm')
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
flag=0
ps = PorterStemmer()

# choose some words to be stemmed
words=["programming"]
for w in words:
    ps.stem(w)
print("Before parsing : ", words[0])
print("After parsing : ", ps.stem(w))
if ps.stem(w) == words[0]:
    flag=1
else:
    flag=0
if flag==1:
    print("Reject")
else:
    print("Accepted")
    
# pos tagging
sen = sp(str(words[0]))
for word in sen:
    print(f'{word.text:{12}} {word.pos_:{10}} {spacy.explain(word.tag_)}')
