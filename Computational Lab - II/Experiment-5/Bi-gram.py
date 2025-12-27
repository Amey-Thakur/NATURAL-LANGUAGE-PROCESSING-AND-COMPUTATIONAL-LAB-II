def readData():
    data = ['This is a  dog','This is a cat','I love my cat','This is my name ']
    dat=[]
    for i in range(len(data)):
        for word in data[i].split():
            dat.append(word)
    print(dat)
    return dat

def createBigram(data):
    listOfBigrams = []
    bigramCounts = {}
    unigramCounts = {}
    for i in range(len(data)-1):
        if i<len(data) - 1 and data[i+1].islower():
            listOfBigrams.append((data[i], data[i + 1]))
        if (data[i], data[i+1]) in bigramCounts:
            bigramCounts[(data[i], data[i + 1])] += 1
        else:
            bigramCounts[(data[i], data[i + 1])] = 1

    if data[i] in unigramCounts:
        unigramCounts[data[i]] += 1
    else:
        unigramCounts[data[i]] = 1
    return listOfBigrams, unigramCounts, bigramCounts


def calcBigramProb(listOfBigrams, unigramCounts, bigramCounts):
    listOfProb = {}
    for bigram in listOfBigrams:
        word1 = bigram[0]
        word2 = bigram[1]
    listOfProb[bigram] = (bigramCounts.get(bigram))/(unigramCounts.get(word1))
    return listOfProb


if __name__ == '__main__':
    data = readData()
listOfBigrams, unigramCounts, bigramCounts = createBigram(data)

print("\n All the possible Bigrams are ")
print(listOfBigrams)

print("\n Bigrams along with their frequency ")
print(bigramCounts)

print("\n Unigrams along with their frequency ")
print(unigramCounts)

bigramProb = calcBigramProb(listOfBigrams, unigramCounts, bigramCounts)

print("\n Bigrams along with their probability ")
print(bigramProb)
inputList="I love my name"
splt=inputList.split()
outputProb1 = 1
bilist=[]
bigrm=[]

for i in range(len(splt) - 1):
    if i<len(splt) - 1:
        bilist.append((splt[i], splt[i + 1]))

print("\n The bigrams in given sentence are ")
print(bilist)
for i in range(len(bilist)):
    if bilist[i] in bigramProb:
        outputProb1 *= bigramProb[bilist[i]]
    else:
        outputProb1 *= 0
print('\n' + 'Probablility of sentence \"I love my name\" = ' + str(outputProb1))

